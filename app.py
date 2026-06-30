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
    with open(CSS_FILE) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(
        "https://streamlit.io/images/brand/streamlit-mark-color.png",
        width=80
    )

    st.title("Topic Modeling")

    st.caption("Deployment CRISP-DM")

    st.divider()

    st.success(
        """
Dashboard siap digunakan.

Silakan gunakan menu di sebelah kiri
untuk berpindah halaman.
"""
    )

# =====================================================
# HERO
# =====================================================

st.title("🧠 Dashboard Topic Modeling")

st.subheader(
    """
Analisis Dinamika Topik Percakapan Publik Mengenai
Kesehatan Mental Remaja di Platform X/Twitter
Menggunakan Latent Dirichlet Allocation (LDA)
"""
)

st.divider()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Jumlah Tweet",
        "8.804"
    )

with col2:
    st.metric(
        "Jumlah Topik",
        "11"
    )

with col3:
    st.metric(
        "Coherence Score",
        "0.4762"
    )

with col4:
    st.metric(
        "Model",
        "LDA"
    )
    
st.markdown("---")

st.header("📖 Ringkasan Penelitian")

st.write(
"""
Penelitian ini bertujuan untuk menganalisis dinamika topik
percakapan publik mengenai kesehatan mental remaja di
platform X/Twitter menggunakan algoritma Latent Dirichlet
Allocation (LDA).

Melalui pendekatan CRISP-DM, sebanyak 8.804 tweet berhasil
diproses hingga diperoleh model terbaik dengan 11 topik
dan nilai Coherence Score sebesar 0.4762.

Dashboard ini dikembangkan sebagai tahap Deployment agar
hasil pemodelan dapat dieksplorasi secara interaktif
melalui antarmuka web berbasis Streamlit.
"""
)

st.markdown("---")

st.header("🎯 Tujuan Penelitian")

st.markdown("""
- Mengaplikasikan algoritma **Latent Dirichlet Allocation (LDA)** untuk menemukan topik laten dari percakapan publik mengenai kesehatan mental remaja.

- Menentukan jumlah topik optimal menggunakan metrik **Coherence Score (Cv)** sehingga menghasilkan model yang representatif.
""")

st.markdown("---")

st.header("🔄 Tahapan Penelitian (CRISP-DM)")

with st.expander("Business Understanding"):
    st.write(
        "Memahami fenomena kesehatan mental remaja dan menentukan tujuan penelitian."
    )

with st.expander("Data Understanding"):
    st.write(
        "Mengumpulkan dan mengeksplorasi dataset Twitter."
    )

with st.expander("Data Preparation"):
    st.write(
        "Melakukan preprocessing seperti cleansing, case folding, tokenizing, stopword removal, slang normalization, dan stemming."
    )

with st.expander("Modeling"):
    st.write(
        "Membangun model Topic Modeling menggunakan algoritma LDA."
    )

with st.expander("Evaluation"):
    st.write(
        "Menentukan model terbaik menggunakan Coherence Score dan Perplexity."
    )

with st.expander("Deployment"):
    st.write(
        "Mengimplementasikan hasil penelitian ke dalam dashboard Streamlit."
    )
    
st.markdown("---")

st.header("📌 Panduan Dashboard")

st.info("""
Gunakan menu navigasi di sidebar sebelah kiri untuk menjelajahi setiap tahapan penelitian.

Dashboard ini menyajikan hasil Topic Modeling mulai dari dataset, proses pemodelan, visualisasi interaktif pyLDAvis, Word Cloud, distribusi topik, hingga interpretasi hasil penelitian.
""")

st.markdown("---")

st.caption(
"""
Dashboard Topic Modeling

Program Studi Teknik Informatika

Universitas Muhammadiyah Sukabumi

Deployment CRISP-DM • 2026
"""
)