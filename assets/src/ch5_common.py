"""5장 단일세포 그림(ch5-03/04/05) 공용 모듈 — 데이터 다운로드 + 장 본문의 Scanpy 파이프라인.

데이터 출처
  pbmc_10k_preprocessed.h5mu (figshare, doi:10.6084/m9.figshare.28555748, CC BY 4.0, 2025)
  = 10x Genomics "PBMC from a Healthy Donor - No Cell Sorting (10k)" Multiome 데이터를
    scvi-tools MultiVI 튜토리얼 방식으로 전처리한 파일.
  내려받기: https://ndownloader.figshare.com/files/54794234

이 파일의 실제 구성(2026-11-24 확인)
  - modality 이름은 "rna"/"atac" 이 아니라 "rna_subset"/"atac_subset"
  - RNA: 12,012 세포 x 4,000 유전자(seurat_v3 HVG 로 이미 축소). .X 는 정수 원시 UMI 카운트
  - "MT-" 유전자 0개 -> pct_counts_mt 는 모두 0(총 카운트 0 인 세포는 NaN)
  - CD3E(그리고 CD3D)는 4,000 유전자에 없음. 같은 CD3 복합체의 CD3G 는 있음
  - 마지막 4,004 세포(인덱스 8008-12011)는 RNA 카운트가 전부 0
    (MultiVI 튜토리얼이 'ATAC 전용' 세포를 흉내 내려고 RNA 를 지운 세포)

파이프라인은 장 본문 코드를 그대로 따르되, modality 키만 "rna_subset" 으로 바꾼다.
필터는 본문 'Claude Code로 단일세포 분석하기' 의 지시(미토콘드리아 20% 이상,
유전자 수 200 미만 제거), 이후 정규화 -> HVG 2000 -> PCA 50 -> neighbors -> UMAP -> Leiden.

실행(저장소 루트에서):
  uv run --python 3.13 --with "scanpy[leiden]==1.13.*" --with mudata \
      --with matplotlib --with pillow python assets/src/ch5-03.py
데이터 폴더는 CH5_DATA_DIR 로 바꿀 수 있다(기본 ~/.cache/vibe-bioinformatics/ch5).
"""
from __future__ import annotations

import os
import sys
import urllib.request
from pathlib import Path

DATA_URL = "https://ndownloader.figshare.com/files/54794234"
DATA_NAME = "pbmc_10k_preprocessed.h5mu"
DATA_SIZE = 49_508_200
CACHE_TAG = "v1"

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent
DATA_DIR = Path(os.environ.get("CH5_DATA_DIR",
                               Path.home() / ".cache/vibe-bioinformatics/ch5"))

MARKERS_CHAPTER = ["CD3E", "CD14", "MS4A1", "NKG7"]
# CD3E 가 이 파일에 없으므로 같은 T 세포 수용체 CD3 복합체의 CD3G 로 대체
MARKERS = ["CD3G", "CD14", "MS4A1", "NKG7"]


def bookplot():
    """교재 스타일 모듈(bookplot)을 불러온다. 폰트는 bioinformatics-book/latex 의 TTF."""
    skill = Path.home() / "bioinformatics-book/.claude/skills/textbook-plot"
    sys.path.insert(0, str(skill))
    if not (Path.home() / "bioinformatics-book/latex/KoPubWorld Dotum Medium.ttf").exists():
        os.environ.setdefault("BOOKPLOT_FONT_DIR",
                              str(Path.home() / ".local/share/fonts/kopub"))
    import bookplot as bp
    return bp


def data_path() -> Path:
    p = DATA_DIR / DATA_NAME
    if not p.exists() or p.stat().st_size != DATA_SIZE:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        print("downloading", DATA_URL, "->", p)
        urllib.request.urlretrieve(DATA_URL, p)
    return p


def load_rna():
    """h5mu 에서 RNA AnnData 를 꺼내 장 본문의 QC 지표를 계산한다(필터 전, 전체 세포)."""
    import mudata as md
    import scanpy as sc

    mdata = md.read_h5mu(data_path())
    adata = mdata.mod["rna_subset"].copy()  # 본문은 mdata.mod["rna"] — 이 파일엔 없는 키

    # --- 장 본문 코드 그대로 ---
    adata.var["mt"] = adata.var_names.str.startswith("MT-")
    sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], out=False)
    return adata


def processed():
    """필터 -> 정규화 -> HVG -> PCA -> neighbors -> UMAP -> Leiden 결과(캐시 사용)."""
    import anndata as ad
    import scanpy as sc

    cache = DATA_DIR / f"ch5_processed_{CACHE_TAG}.h5ad"
    if cache.exists():
        return ad.read_h5ad(cache)

    adata = load_rna()
    # 본문 지시: 미토콘드리아 비율 20% 이상, 유전자 수 200개 미만 세포 제거
    keep = (adata.obs["n_genes_by_counts"] >= 200) & ~(adata.obs["pct_counts_mt"] >= 20)
    adata = adata[keep.values].copy()

    adata.layers["counts"] = adata.X.copy()
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)
    sc.pp.pca(adata, n_comps=50)

    # --- 장 본문 코드 그대로 ---
    sc.pp.neighbors(adata)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=0.5, flavor="igraph", n_iterations=2)
    sc.tl.rank_genes_groups(adata, groupby="leiden")

    adata.write_h5ad(cache)
    return adata
