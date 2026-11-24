# ch5 그림 — Leiden 군집 UMAP (assets/ch5-04-umap-clusters.png)
# 데이터 출처: pbmc_10k_preprocessed.h5mu (figshare, doi:10.6084/m9.figshare.28555748,
#   CC BY 4.0, 2025; 원자료 10x Genomics PBMC 10k Multiome). 자세한 내용은 ch5_common.py.
# 파이프라인: 유전자 수 200 미만 제거(7,179 세포) -> normalize_total(1e4) + log1p
#   -> HVG 2000 -> PCA 50 -> sc.pp.neighbors -> sc.tl.umap
#   -> sc.tl.leiden(resolution=0.5, flavor="igraph", n_iterations=2)
# UMAP 좌표는 선형 척도의 양이 아니므로 0 시작 규칙을 적용하지 않고, scanpy 처럼 눈금 없이 그린다.
import numpy as np
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D

import ch5_common as c

bp = c.bookplot()
plt = bp.use()

adata = c.processed()
xy = adata.obsm["X_umap"]
cats = list(adata.obs["leiden"].cat.categories)
lab = adata.obs["leiden"].to_numpy()

# 교재 범주형 6색 + 구분되는 악센트 확장
palette = bp.CATEGORICAL + ["#7E5AA8", "#8DAA3B", "#8C5A2B", "#E59AB8", "#C9A227",
                            "#2B4C7E", "#D4553A"]
assert len(cats) <= len(palette), f"군집 {len(cats)}개 > 색 {len(palette)}개"
colors = dict(zip(cats, palette))

fig, ax = plt.subplots(figsize=(6.4, 5.2))
order = np.random.default_rng(0).permutation(len(lab))  # 큰 군집이 작은 군집을 덮지 않게
ax.scatter(xy[order, 0], xy[order, 1], s=2.5, c=[colors[k] for k in lab[order]],
           linewidths=0, rasterized=True)
for k in cats:
    mx, my = np.median(xy[lab == k], axis=0)
    ax.text(mx, my, k, ha="center", va="center", fontsize=10, color=bp.DARKGRAY,
            weight="bold",
            path_effects=[pe.withStroke(linewidth=2.5, foreground="white")])

handles = [Line2D([], [], ls="", marker="o", ms=6, color=colors[k], label=k) for k in cats]
ax.legend(handles=handles, title="Leiden 군집", loc="center left",
          bbox_to_anchor=(1.01, 0.5), handletextpad=0.3, labelspacing=0.35,
          title_fontsize=11)
ax.set_xlabel("UMAP1")
ax.set_ylabel("UMAP2")
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect("equal", adjustable="datalim")
bp.despine(ax)

bp.save(fig, c.ASSETS / "ch5-04-umap-clusters.png")
