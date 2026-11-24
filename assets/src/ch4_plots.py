# ch4 그림 — 4장 Matplotlib/Seaborn 예시 그림(ch4-02, ch4-03, ch4-04, ch4-05)
# 데이터 출처: pbmc_10k_preprocessed.h5mu (figshare, doi:10.6084/m9.figshare.28555748,
#   CC BY 4.0, 2025; 원자료 10x Genomics PBMC 10k Multiome). 5장과 같은 파일을 같은
#   파이프라인(ch5_common.processed)으로 처리한 뒤, Leiden 군집을 마커 유전자로 세포 유형에
#   묶었다(0,4: T 세포 / 1,3: NK 세포 / 2,8: 단핵구 / 6,7: B 세포; 그 밖의 군집은 제외).
# 차등 발현: B 세포 vs 나머지 세 유형, scanpy rank_genes_groups(method="wilcoxon").
#   세포가 수천 개면 p값이 0으로 떨어지므로 그룹마다 200개씩 무작위 추출(seed 0)해 비교하고,
#   두 그룹 중 한쪽이라도 세포 10% 이상에서 검출되는 유전자만 남겼다(거의 발현되지 않는 유전자의
#   극단적인 logFC 제거). logFC = log2 배수 변화, pvalue = 원시 p값.
# 실행(저장소 루트에서):
#   uv run --python 3.13 --with "scanpy[leiden]==1.13.*" --with mudata --with seaborn \
#       --with matplotlib --with pillow python assets/src/ch4_plots.py
import numpy as np
import pandas as pd
import scanpy as sc
import seaborn as sns

import ch5_common as c

bp = c.bookplot()
plt = bp.use()

CT = {"0": "T 세포", "4": "T 세포", "1": "NK 세포", "3": "NK 세포",
      "2": "단핵구", "8": "단핵구", "6": "B 세포", "7": "B 세포"}
ORDER = ["T 세포", "B 세포", "NK 세포", "단핵구"]

adata = c.processed()
adata = adata[adata.obs["leiden"].isin(list(CT))].copy()
adata.obs["cell_type"] = pd.Categorical(adata.obs["leiden"].map(CT), categories=ORDER)

# --- 차등 발현 결과(4장 df의 gene_name, logFC, pvalue에 해당) ---
rng = np.random.default_rng(0)
grp = np.where(adata.obs["cell_type"] == "B 세포", "B 세포", "나머지")
idx = np.concatenate([rng.choice(np.flatnonzero(grp == g), 200, replace=False) for g in ["B 세포", "나머지"]])
sub = adata[idx].copy()
sub.obs["grp"] = pd.Categorical(grp[idx])
sc.tl.rank_genes_groups(sub, groupby="grp", groups=["B 세포"], reference="나머지",
                        method="wilcoxon", key_added="b_de", pts=True)
de = sc.get.rank_genes_groups_df(sub, group="B 세포", key="b_de")
pts_rest = sub.uns["b_de"]["pts_rest"]["B 세포"] if "pts_rest" in sub.uns["b_de"] else None
keep = de["pct_nz_group"] >= 0.10
if "pct_nz_reference" in de.columns:
    keep |= de["pct_nz_reference"] >= 0.10
de = de[keep].copy()
# scanpy의 logfoldchanges는 비교군 평균이 0이면 아주 작은 수로 나눠 극단값(±30)이 되므로,
# Seurat와 같이 log2(평균(expm1(x)) + 1)의 차이로 다시 계산한다.
def _mean_counts(a):
    X = a.X.toarray() if hasattr(a.X, "toarray") else np.asarray(a.X)
    return pd.Series(np.expm1(X).mean(axis=0), index=a.var_names)
mB = _mean_counts(sub[sub.obs["grp"] == "B 세포"])
mR = _mean_counts(sub[sub.obs["grp"] == "나머지"])
de["logFC"] = (np.log2(mB + 1) - np.log2(mR + 1)).loc[de["names"]].to_numpy()
de = de.rename(columns={"names": "gene_name", "pvals": "pvalue"})
de = de[np.isfinite(de["logFC"])]
de["neg_log_p"] = -np.log10(de["pvalue"].clip(lower=1e-300))
print("최대 -log10p:", de["neg_log_p"].max())
print(f"유전자 {len(de)}개, logFC 범위 {de.logFC.min():.2f}~{de.logFC.max():.2f}")

XL, YL = "로그 배수 변화(log2FC)", "−log10(p값)"
lim = np.ceil(de["logFC"].abs().quantile(0.999))


def volcano(ax, s):
    ax.scatter(de["logFC"], de["neg_log_p"], s=s, color=bp.PRIMARY, linewidths=0, rasterized=True)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(0, de["neg_log_p"].max() * 1.05)
    ax.set_xlabel(XL)
    ax.set_ylabel(YL)
    bp.despine(ax)


# ch4-02: 기본 volcano plot (본문 코드: plt.scatter 한 가지 색)
fig, ax = plt.subplots(figsize=(6.0, 4.6))
volcano(ax, 6)
bp.save(fig, "assets/ch4-02-matplotlib-volcano.png")

# ch4-03: logFC 히스토그램(bins=50) + volcano(s=1)
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.4))
axes[0].hist(de["logFC"], bins=50, range=(-lim, lim), color=bp.PRIMARY, edgecolor="white", linewidth=0.4)
axes[0].set_xlim(-lim, lim)
axes[0].set_ylim(0, None)
axes[0].set_xlabel(XL)
axes[0].set_ylabel("유전자 수")
bp.despine(axes[0])
bp.grid_y(axes[0])
volcano(axes[1], 2)
fig.tight_layout()
bp.save(fig, "assets/ch4-03-matplotlib-subplot.png")

# ch4-04: 세포 유형별 발현량 박스 플롯 (HLA-DRA: B 세포와 단핵구에서 높음)
gene = "HLA-DRA" if "HLA-DRA" in adata.var_names else "CD74"
x = adata[:, gene].X
x = np.asarray(x.toarray()).ravel() if hasattr(x, "toarray") else np.asarray(x).ravel()
box = pd.DataFrame({"cell_type": adata.obs["cell_type"].to_numpy(), "expression": x})
fig, ax = plt.subplots(figsize=(6.4, 4.4))
sns.boxplot(data=box, x="cell_type", y="expression", order=ORDER, ax=ax,
            palette=bp.CATEGORICAL[:4], hue="cell_type", legend=False,
            fliersize=1.5, linewidth=1)
ax.set_ylim(0, None)
ax.set_xlabel("세포 유형")
ax.set_ylabel(f"{gene} 발현량(log 정규화)")
bp.despine(ax)
bp.grid_y(ax)
bp.save(fig, "assets/ch4-04-seaborn-boxplot.png")
print("boxplot gene:", gene)

# ch4-05: 마커 유전자 x 세포 유형 평균 발현(유전자별 z-점수) 히트맵, RdBu_r, center=0
markers = [g for g in ["CD3G", "IL7R", "CCR7", "MS4A1", "CD79A", "CD74", "NKG7", "GNLY",
                       "PRF1", "CD14", "LYZ", "FCN1"] if g in adata.var_names]
X = adata[:, markers].X
X = X.toarray() if hasattr(X, "toarray") else np.asarray(X)
mean = pd.DataFrame(X, columns=markers).groupby(adata.obs["cell_type"].to_numpy()).mean().loc[ORDER].T
z = mean.sub(mean.mean(axis=1), axis=0).div(mean.std(axis=1), axis=0)
fig, ax = plt.subplots(figsize=(5.6, 5.4))
sns.heatmap(z, cmap="RdBu_r", center=0, ax=ax, linewidths=0.5, linecolor="white",
            cbar_kws={"label": "상대 발현량(z-점수)"})
ax.set_xlabel("")
ax.set_ylabel("")
ax.tick_params(axis="both", length=0)
plt.setp(ax.get_yticklabels(), rotation=0)
bp.save(fig, "assets/ch4-05-seaborn-heatmap.png")
print("heatmap genes:", markers)
