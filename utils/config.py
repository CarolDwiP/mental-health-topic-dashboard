from pathlib import Path

# ==========================================================
# KONFIGURASI DIREKTORI
# ==========================================================

# Folder utama project
BASE_DIR = Path(__file__).resolve().parent.parent

# Folder data
DATA_DIR = BASE_DIR / "data"

# Folder visualisasi
VISUAL_DIR = BASE_DIR / "visualisasi"

# Folder charts
CHART_DIR = VISUAL_DIR / "charts"

# Folder pyLDAvis
PYLDAVIS_DIR = VISUAL_DIR / "pyldavis"

# Folder assets
ASSET_DIR = BASE_DIR / "assets"

CSS_FILE = ASSET_DIR / "css" / "style.css"

# ==========================================================
# FILE DATA
# ==========================================================

DATA_BERSIH = DATA_DIR / "data_bersih.csv"
DATA_FINAL = DATA_DIR / "data_final_dengan_topik.csv"

# ==========================================================
# FILE VISUALISASI
# ==========================================================

COHERENCE = CHART_DIR / "grafik_coherence_perplexity.png"

EDA = CHART_DIR / "eda_distribusi.png"

DISTRIBUSI_TOPIK = CHART_DIR / "distribusi_topik.png"

PREPROCESSING = CHART_DIR / "preprocessing_kata_frekuensi.png"

WORDCLOUD_TOPIK = CHART_DIR / "wordcloud_per_topik.png"

PYLDAVIS = PYLDAVIS_DIR / "pyldavis_interaktif.html"

# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

APP_TITLE = (
    "Dashboard Analisis Dinamika Topik Percakapan Publik "
    "Mengenai Kesehatan Mental Remaja "
    "di Platform X/Twitter Menggunakan LDA"
)

APP_ICON = "🧠"

AUTHOR = "Carol"

UNIVERSITAS = "Universitas Muhammadiyah Kalimantan Timur"

MODEL = "Latent Dirichlet Allocation (LDA)"

JUMLAH_DATA = "8.804 Tweet"

JUMLAH_TOPIK = "11"

COHERENCE_SCORE = "0.4762"

METODOLOGI = "CRISP-DM"