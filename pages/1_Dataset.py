import streamlit as st
import pandas as pd
from pathlib import Path

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Dataset",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

DATA_PATH = Path("data/data_bersih.csv")

df = pd.read_csv(DATA_PATH)

st.title("📊 Dataset Penelitian")

st.caption(
"""
Dataset yang digunakan pada penelitian ini merupakan kumpulan
percakapan publik mengenai kesehatan mental remaja
di platform X (Twitter) yang telah melalui proses
preprocessing sehingga siap digunakan pada tahap
Topic Modeling menggunakan algoritma LDA.
"""
)

st.divider()

jumlah_tweet = len(df)

jumlah_kolom = len(df.columns)

rata_panjang = df["panjang_tweet"].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Jumlah Tweet",
        f"{jumlah_tweet:,}"
    )

with col2:
    st.metric(
        "Jumlah Kolom",
        jumlah_kolom
    )

with col3:
    st.metric(
        "Rata-rata Karakter",
        f"{rata_panjang:.0f}"
    )
    
st.markdown("---")

st.subheader("Informasi Dataset")

kiri, kanan = st.columns(2)

with kiri:

    st.info(
"""
**Sumber Data**

Platform X (Twitter)

**Bahasa**

Bahasa Indonesia

**Jumlah Data**

8.804 Tweet

**Metode**

CRISP-DM
"""
    )

with kanan:

    st.success(
"""
**Algoritma**

Latent Dirichlet Allocation

**Topik**

11

**Evaluasi**

Coherence Score & Perplexity

**Output**

Dashboard Streamlit
"""
    )

st.markdown("---")

st.subheader("Preview Dataset")

st.dataframe(
    df.head(15),
    use_container_width=True
)

st.markdown("---")
st.subheader("📈 Ringkasan Statistik Dataset")

# Menghitung statistik
tweet_terpendek = int(df["panjang_tweet"].min())
tweet_terpanjang = int(df["panjang_tweet"].max())
median_panjang = int(df["panjang_tweet"].median())

jumlah_primer = (df["sumber_data"] == "Primer (Scraping Mandiri)").sum()
jumlah_sekunder = (df["sumber_data"] == "Sekunder (Kaggle Dataset)").sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Tweet Terpendek", f"{tweet_terpendek} karakter")
    st.metric("Median Panjang Tweet", f"{median_panjang} karakter")
    st.metric("Sumber Primer", f"{jumlah_primer:,}")

with col2:
    st.metric("Tweet Terpanjang", f"{tweet_terpanjang} karakter")
    st.metric("Rata-rata Panjang Tweet", f"{rata_panjang:.0f} karakter")
    st.metric("Sumber Sekunder", f"{jumlah_sekunder:,}")

st.markdown("---")

st.subheader("Exploratory Data Analysis")

EDA = Path(
    "visualisasi/charts/eda_distribusi.png"
)

if EDA.exists():

    st.image(
        str(EDA),
        use_container_width=True
    )

else:

    st.warning(
        "Gambar EDA tidak ditemukan."
    )
    
st.markdown("---")

st.subheader("Insight Dataset")

st.write(
"""
Berdasarkan proses eksplorasi data,
dataset terdiri dari **8.804 tweet**
yang membahas kesehatan mental remaja
di platform X (Twitter).

Distribusi panjang tweet menunjukkan
bahwa sebagian besar pengguna
menyampaikan pendapat secara singkat,
sesuai karakteristik media sosial.

Data ini kemudian diproses melalui
tahapan preprocessing sehingga
siap digunakan pada pemodelan
Topic Modeling menggunakan
algoritma Latent Dirichlet Allocation (LDA).
"""
)

