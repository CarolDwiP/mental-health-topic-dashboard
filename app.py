import streamlit as st
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Dashboard Topic Modeling",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================
# LOAD CSS
# =====================================================

CSS_FILE = Path("assets/css/style.css")

if CSS_FILE.exists():
    with open(CSS_FILE, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("# 🧠")
    st.title("Mental Health")
    st.caption("Topic Modeling Dashboard")

    st.divider()

    st.info(
        """
📌 **Navigasi Dashboard**

Gunakan menu pada sidebar untuk menjelajahi seluruh tahapan penelitian mulai dari Dataset hingga Temuan Penelitian.
"""
    )

    st.divider()

    st.caption(
        """
**Metodologi**

CRISP-DM

**Algoritma**

Latent Dirichlet Allocation (LDA)
"""
    )

# =====================================================
# HERO
# =====================================================

st.title("🧠 Dashboard Topic Modeling")

st.markdown("""
### Analisis Dinamika Topik Percakapan Publik Mengenai Kesehatan Mental Remaja
### di Platform X/Twitter Menggunakan *Latent Dirichlet Allocation* (LDA)
""")

st.caption(
    "Deployment hasil penelitian berbasis Streamlit untuk eksplorasi Topic Modeling secara interaktif."
)

st.divider()

# =====================================================
# METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📊 Jumlah Tweet",
        "8.804"
    )

with col2:
    st.metric(
        "🧩 Jumlah Topik",
        "11"
    )

with col3:
    st.metric(
        "📈 Coherence Score",
        "0.4762"
    )

with col4:
    st.metric(
        "🤖 Algoritma",
        "LDA"
    )

st.markdown("---")

# =====================================================
# OVERVIEW
# =====================================================

st.header("🔍 Gambaran Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 📂 Dataset

Menampilkan karakteristik dataset penelitian, statistik dasar, serta proses eksplorasi data sebelum dilakukan pemodelan.
""")

with col2:
    st.info("""
### 🧠 Topic Modeling

Menyajikan proses pemodelan LDA, evaluasi model, visualisasi interaktif pyLDAvis, serta Word Cloud.
""")

with col3:
    st.warning("""
### 📊 Hasil Analisis

Menyajikan distribusi topik, interpretasi setiap topik, temuan penelitian, dan informasi penelitian.
""")

st.markdown("---")

# =====================================================
# RINGKASAN
# =====================================================

st.header("📖 Ringkasan Penelitian")

st.write("""
Penelitian ini bertujuan untuk menganalisis dinamika topik percakapan publik mengenai kesehatan mental remaja pada platform X/Twitter menggunakan algoritma **Latent Dirichlet Allocation (LDA)**.

Sebanyak **8.804 tweet** diproses melalui tahapan **CRISP-DM**, sehingga diperoleh model terbaik dengan **11 topik** dan **Coherence Score sebesar 0.4762**. Dashboard ini dikembangkan sebagai media *deployment* agar hasil penelitian dapat dieksplorasi secara interaktif melalui antarmuka web.
""")

st.markdown("---")

# =====================================================
# TUJUAN
# =====================================================

st.header("🎯 Tujuan Penelitian")

st.markdown("""
- Mengidentifikasi topik-topik utama percakapan publik mengenai kesehatan mental remaja menggunakan algoritma **Latent Dirichlet Allocation (LDA)**.

- Menentukan model terbaik berdasarkan **Coherence Score** sehingga menghasilkan pemodelan topik yang representatif.

- Menyajikan hasil analisis ke dalam dashboard interaktif yang mudah dieksplorasi oleh pengguna.
""")

st.markdown("---")

# =====================================================
# CRISP-DM
# =====================================================

st.header("🔄 Tahapan Penelitian (CRISP-DM)")

with st.expander("1️⃣ Business Understanding"):
    st.write(
        "Memahami fenomena kesehatan mental remaja serta merumuskan tujuan penelitian."
    )

with st.expander("2️⃣ Data Understanding"):
    st.write(
        "Mengumpulkan, memahami, dan mengeksplorasi dataset hasil crawling platform X/Twitter."
    )

with st.expander("3️⃣ Data Preparation"):
    st.write(
        "Melakukan preprocessing berupa cleansing, case folding, tokenizing, normalisasi slang, stopword removal, dan stemming."
    )

with st.expander("4️⃣ Modeling"):
    st.write(
        "Membangun model Topic Modeling menggunakan algoritma Latent Dirichlet Allocation (LDA)."
    )

with st.expander("5️⃣ Evaluation"):
    st.write(
        "Menentukan model terbaik berdasarkan nilai Coherence Score dan Perplexity."
    )

with st.expander("6️⃣ Deployment"):
    st.write(
        "Mengimplementasikan hasil penelitian ke dalam dashboard web berbasis Streamlit."
    )

st.markdown("---")

# =====================================================
# PANDUAN
# =====================================================

st.header("💡 Cara Menggunakan Dashboard")

st.info("""
Dashboard ini dirancang mengikuti alur metodologi **CRISP-DM**.

Silakan gunakan menu navigasi pada **sidebar** untuk berpindah ke setiap tahapan penelitian, mulai dari Dataset, Preprocessing, Topic Modeling, Visualisasi LDA, Distribusi Topik, Interpretasi Topik, Word Cloud, hingga Temuan Penelitian.
""")

st.markdown("---")

# =====================================================
# FOOTER
# =====================================================

st.caption("""
**Dashboard Topic Modeling Kesehatan Mental Remaja**

Program Studi Teknik Informatika  
Universitas Muhammadiyah Sukabumi  

© 2026 • Deployment menggunakan Streamlit
""")