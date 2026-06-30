import streamlit as st
from data.topic_data import TOPICS

st.set_page_config(
    page_title="Interpretasi Topik",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Interpretasi 11 Topik Laten")

st.caption("""
Halaman ini menyajikan interpretasi hasil Topic Modeling menggunakan
algoritma Latent Dirichlet Allocation (LDA). Setiap topik dianalisis
berdasarkan kata kunci dominan serta makna psikologis yang ditemukan
pada percakapan mengenai kesehatan mental remaja di platform X (Twitter).
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Jumlah Topik", "11")

with col2:
    st.metric("Klaster Besar", "2")

with col3:
    st.metric("Topik Dominan", "Topik 1")

with col4:
    st.metric("Novelty", "Fandom")
    
st.markdown("---")

st.subheader("📊 Pola Klasterisasi Makro")

st.info("""
Berdasarkan analisis lintas topik, sebelas topik hasil pemodelan
dapat dikelompokkan menjadi dua klaster besar.

Klaster pertama merepresentasikan **Ekspresi Tekanan (Distress)**,
sedangkan klaster kedua merepresentasikan
**Mekanisme Koping (Coping Mechanism)**.

Pengelompokan ini memperlihatkan bahwa percakapan mengenai kesehatan
mental remaja tidak hanya berisi keluhan psikologis,
tetapi juga strategi bertahan yang digunakan remaja
dalam menghadapi tekanan tersebut.
""")

left, right = st.columns(2)

with left:
    st.error("""
### 🔴 Distress

Topik yang menggambarkan sumber tekanan psikologis.

• Topik 1 — Kecemasan Klinis & Stigma Mental

• Topik 2 — Psikosomatis & Gangguan Tidur

• Topik 4 — Krisis Eksistensial

• Topik 5 — Burnout Akademik

• Topik 7 — Validasi Sosial

• Topik 8 — Konflik Asmara
""")

with right:
    st.success("""
### 🟢 Coping

Topik yang menggambarkan mekanisme bertahan.

• Topik 3 — Escapism via Fandom

• Topik 6 — Cry for Help

• Topik 9 — Media Hiburan

• Topik 10 — Religius

• Topik 11 — Rutinitas Harian
""")
    
st.markdown("---")

st.subheader("📚 Interpretasi Tiap Topik")

for t in TOPICS:
    with st.expander(f"{t['kategori']} Topik {t['id']} — {t['judul']}"):
        st.markdown(f"### 📊 Persentase Dominasi\n{t['persentase']}")
        
        st.markdown("---")
        
        st.markdown("### 🔑 Kata Kunci Dominan")
        st.write(", ".join(t["kata_kunci"]))
        
        st.markdown("---")
        
        st.markdown("### 📖 Interpretasi")
        st.write(t["interpretasi"])
        
        st.markdown("---")
        
        st.markdown("### 🧠 Makna terhadap Kesehatan Mental")
        st.write(t["makna"])
        
        st.markdown("---")
        
        st.success(f"**Kesimpulan:**\n\n{t['kesimpulan']}")
        
st.markdown("---")

st.subheader("💡 Temuan Utama Penelitian")

st.success("""
Penelitian ini menunjukkan bahwa percakapan mengenai kesehatan mental
remaja di platform X tidak hanya didominasi oleh ekspresi tekanan
psikologis, tetapi juga memperlihatkan beragam mekanisme koping.

Temuan yang paling menonjol adalah munculnya budaya fandom sebagai
ruang perlindungan emosional (digital sanctuary), yang menjadi salah
satu bentuk mekanisme koping modern bagi Generasi Z.

Selain itu, hasil penelitian juga menunjukkan bahwa stigma sosial
masih menjadi hambatan utama remaja dalam mencari bantuan terhadap
permasalahan kesehatan mental.
""")