# ch5 그림 — 마커 유전자별 UMAP (assets/ch5-05-umap-marker-genes.png)
# 데이터 출처: pbmc_10k_preprocessed.h5mu (figshare, doi:10.6084/m9.figshare.28555748,
#   CC BY 4.0, 2025; 원자료 10x Genomics PBMC 10k Multiome). 자세한 내용은 ch5_common.py.
# 색 = log1p(정규화 발현량), sc.pl.umap(color=[...]) 와 같은 값(adata.X).
# 본문의 CD3E 는 이 파일(4,000 유전자)에 없어, 같은 CD3 복합체의 CD3G 로 대신 그렸다.
import numpy as np
import scanpy as sc
from matplotlib.colors import LinearSegmentedColormap

import ch5_common as c

bp = c.bookplot()
plt = bp.use()

adata = c.processed()
xy = adata.obsm["X_umap"]
genes = [g for g in c.MARKERS if g in adata.var_names]
assert genes == c.MARKERS, genes

cmap = LinearSegmentedColormap.from_list(
    "book_teal", ["#E6E6E6", bp.TEAL_RAMP[4], bp.TEAL_RAMP[3], bp.TEAL_RAMP[2],
                  bp.TEAL_RAMP[1], bp.TEAL_RAMP[0]])

fig, axes = plt.subplots(2, 2, figsize=(7.2, 6.4),
                         gridspec_kw={"wspace": 0.12, "hspace": 0.12})
for ax, g in zip(axes.ravel(), genes):
    v = sc.get.obs_df(adata, keys=[g])[g].to_numpy()
    o = np.argsort(v, kind="stable")  # 발현이 높은 세포를 위에
    sca = ax.scatter(xy[o, 0], xy[o, 1], c=v[o], cmap=cmap, vmin=0, vmax=v.max(),
                     s=2.0, linewidths=0, rasterized=True)
    ax.text(0.03, 0.97, g, transform=ax.transAxes, ha="left", va="top",
            fontsize=11, color=bp.DARKGRAY, weight="bold")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal", adjustable="datalim")
    bp.despine(ax)
    cb = fig.colorbar(sca, ax=ax, fraction=0.045, pad=0.02, shrink=0.8)
    cb.outline.set_visible(False)
    cb.ax.tick_params(labelsize=9, length=2)
    cb.locator = plt.MaxNLocator(nbins=4, integer=True)
    cb.update_ticks()
    if ax in axes[:, 1]:
        cb.set_label("발현량(log 정규화)", fontsize=10.5)
for ax in axes[1]:
    ax.set_xlabel("UMAP1")
for ax in axes[:, 0]:
    ax.set_ylabel("UMAP2")

bp.save(fig, c.ASSETS / "ch5-05-umap-marker-genes.png")
