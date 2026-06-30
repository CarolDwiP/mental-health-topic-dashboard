import streamlit as st
from data.project_info import PROJECT_INFO

st.set_page_config(
    page_title="Tentang Penelitian",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ Tentang Penelitian")

st.caption("""
Dashboard ini merupakan implementasi tahap Deployment
dalam metodologi CRISP-DM untuk penelitian Topic Modeling
menggunakan algoritma Latent Dirichlet Allocation (LDA).
""")

st.divider()

st.subheader("📖 Judul Penelitian")

st.info(PROJECT_INFO["judul"])

left,right = st.columns(2)

with left:

    st.markdown("### 🏫 Identitas")

    st.write(f"**Universitas:** {PROJECT_INFO['universitas']}")
    st.write(f"**Program Studi:** {PROJECT_INFO['prodi']}")
    st.write(f"**Tahun:** {PROJECT_INFO['tahun']}")

    st.write("**Metodologi:** CRISP-DM")

    st.write("**Algoritma:** LDA")
with right:

    st.markdown("### 📊 Statistik Penelitian")

    st.metric("Jumlah Tweet","8.804")

    st.metric("Jumlah Topik","11")

    st.metric("Coherence","0.4762")

    st.metric("Perplexity","-7.3441")

st.divider()

st.subheader("⚙️ Tahapan CRISP-DM")

tabs = st.tabs([
    "1️⃣ Business",
    "2️⃣ Data",
    "3️⃣ Preparation",
    "4️⃣ Modeling",
    "5️⃣ Evaluation",
    "6️⃣ Deployment"
])

with tabs[0]:
    st.write("""
Memahami fenomena kesehatan mental remaja di platform X
serta merumuskan tujuan penelitian untuk memetakan
topik-topik utama percakapan publik.
""")
    
st.divider()

st.subheader("🎯 Tujuan Penelitian")

st.write("""
1. Mengidentifikasi topik laten mengenai kesehatan mental remaja di platform X menggunakan algoritma LDA.

2. Menentukan jumlah topik optimal berdasarkan nilai Coherence Score.

3. Mengimplementasikan hasil pemodelan ke dalam dashboard interaktif berbasis Streamlit.
""")

st.divider()

st.subheader("🌍 Manfaat Penelitian")

tab1,tab2 = st.tabs([
    "📚 Teoritis",
    "💼 Praktis"
])

with tab1:

    st.write("""
Menambah referensi penelitian
Natural Language Processing,
Topic Modeling,
dan Text Mining
berbahasa Indonesia.
""")

with tab2:

    st.write("""
Memberikan wawasan
mengenai dinamika
kesehatan mental remaja
melalui media sosial
sebagai bahan pertimbangan
bagi akademisi,
psikolog,
dan masyarakat.
""")
    
st.divider()

st.subheader("💻 Teknologi yang Digunakan")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.success("Python")

with c2:
    st.success("Google Colab")

with c3:
    st.success("Streamlit")

with c4:
    st.success("pyLDAvis")
    
    st.divider()

st.caption("""
Dashboard ini dikembangkan sebagai implementasi tahap Deployment
dalam metodologi CRISP-DM pada penelitian Topic Modeling
menggunakan algoritma Latent Dirichlet Allocation (LDA).

Universitas Muhammadiyah Sukabumi
Program Studi Teknik Informatika
Tahun 2026
""")