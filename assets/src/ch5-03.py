# ch5 그림 — QC 바이올린 플롯 (assets/ch5-03-qc-violin-plots.png)
# 데이터 출처: pbmc_10k_preprocessed.h5mu (figshare, doi:10.6084/m9.figshare.28555748,
#   CC BY 4.0, 2025; 원자료 10x Genomics PBMC 10k Multiome). 자세한 내용은 ch5_common.py.
# 장 본문 코드(adata.var["mt"] = ...startswith("MT-"); sc.pp.calculate_qc_metrics(
#   adata, qc_vars=["mt"], out=False))로 계산한 필터 전 전체 12,012 세포의 지표.
# 주의: 이 파일에는 MT- 유전자가 없어 pct_counts_mt 는 모두 0 이고,
#   RNA 카운트가 0 인 4,004 세포(ATAC 전용)는 pct_counts_mt 가 NaN 이라 빠진다.
#   n_genes_by_counts·total_counts 의 0 근처 덩어리는 이 4,004 세포다.
import numpy as np
from matplotlib.ticker import FuncFormatter, MaxNLocator

import ch5_common as c

bp = c.bookplot()
plt = bp.use()

obs = c.load_rna().obs
panels = [
    ("n_genes_by_counts", "검출 유전자 수(개)"),
    ("total_counts", "총 UMI 수(개)"),
    ("pct_counts_mt", "미토콘드리아 유전자 비율(%)"),
]

rng = np.random.default_rng(0)
fig, axes = plt.subplots(1, 3, figsize=(7.2, 3.6), gridspec_kw={"wspace": 0.75})
for ax, (key, label) in zip(axes, panels):
    v = obs[key].to_numpy(dtype=float)
    v = v[~np.isnan(v)]
    # 개별 세포(지터) — sc.pl.violin 기본 모양과 같게
    ax.scatter(rng.uniform(-0.28, 0.28, v.size), v, s=0.6, color=bp.DARKGRAY,
               alpha=0.25, linewidths=0, rasterized=True, zorder=1)
    if np.ptp(v) > 0:
        parts = ax.violinplot(v, positions=[0], widths=0.85, showextrema=False,
                              bw_method=0.15)
        for b in parts["bodies"]:
            b.set_facecolor(bp.PRIMARY)
            b.set_edgecolor(bp.PRIMARY)
            b.set_alpha(0.45)
            b.set_zorder(2)
        q1, med, q3 = np.percentile(v, [25, 50, 75])
        ax.vlines(0, q1, q3, color=bp.DARKGRAY, lw=4, zorder=3)
        ax.scatter([0], [med], s=14, color="white", edgecolor=bp.DARKGRAY,
                   linewidths=0.8, zorder=4)
        ax.set_ylim(0, v.max() * 1.04)
    else:  # 값이 모두 같으면(KDE 불가) 가로선으로 표시
        ax.hlines(v[0], -0.42, 0.42, color=bp.PRIMARY, lw=2.2, zorder=2)
        ax.set_ylim(0, 25)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5, integer=True, min_n_ticks=4))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:,.0f}"))
    ax.set_xlim(-0.6, 0.6)
    ax.set_xticks([])
    ax.set_ylabel(label)
    bp.despine(ax)
    bp.grid_y(ax)
    ax.spines["bottom"].set_visible(False)

bp.save(fig, c.ASSETS / "ch5-03-qc-violin-plots.png")
