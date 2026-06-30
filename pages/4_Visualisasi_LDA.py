import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Visualisasi LDA",
    page_icon="🌐",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title("🌐 Visualisasi Topic Modeling (pyLDAvis)")

st.caption("""
Halaman ini menampilkan visualisasi interaktif hasil Topic Modeling
menggunakan algoritma Latent Dirichlet Allocation (LDA).

Visualisasi pyLDAvis membantu memahami hubungan antar topik,
kata-kata dominan pada setiap topik,
serta tingkat relevansi kata terhadap topik tertentu.
""")

st.divider()

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Jumlah Tweet","8.804")

with col2:
    st.metric("Jumlah Topik","11")

with col3:
    st.metric("Coherence","0.4762")

with col4:
    st.metric("Perplexity","-7.3441")
    
st.markdown("---")

st.subheader("Visualisasi Interaktif")

html_path = Path(
    "visualisasi/pyldavis/pyldavis_interaktif.html"
)

if html_path.exists():

    with open(html_path, "r", encoding="utf-8") as f:

        source = f.read()

    components.html(
        source,
        height=900,
        scrolling=True
    )

else:

    st.error(
        "File pyLDAvis_interaktif.html tidak ditemukan."
    )
    
st.markdown("---")

st.subheader("📖 Cara Membaca Visualisasi")

st.markdown("""

### Panel Kiri

Menampilkan **Intertopic Distance Map**.

- Setiap lingkaran mewakili satu topik.
- Ukuran lingkaran menunjukkan proporsi topik.
- Semakin berjauhan posisi dua lingkaran, semakin berbeda karakteristik topiknya.

---

### Panel Kanan

Menampilkan kata-kata dominan pada topik yang dipilih.

- Semakin panjang batang berwarna merah, semakin tinggi relevansi kata terhadap topik.
- Batang berwarna biru menunjukkan frekuensi kata secara keseluruhan dalam korpus.

---

### Parameter λ (Lambda)

Slider λ digunakan untuk mengatur tingkat relevansi kata.

- λ = 1 menampilkan kata yang paling sering muncul.
- λ mendekati 0 menampilkan kata yang paling khas pada suatu topik.

""")

st.markdown("---")

st.subheader("💡 Insight Penelitian")

st.info("""

Visualisasi pyLDAvis menunjukkan bahwa model akhir berhasil
mengidentifikasi **11 topik laten** dari total **8.804 tweet**
mengenai kesehatan mental remaja di platform X (Twitter).

Pemisahan antar topik pada Intertopic Distance Map menunjukkan
bahwa model mampu membedakan kelompok percakapan berdasarkan
karakteristik kata yang dominan.

Selain itu, panel kata kunci memberikan gambaran mengenai
istilah-istilah yang paling relevan pada masing-masing topik,
sehingga memudahkan proses interpretasi hasil Topic Modeling.

""")

