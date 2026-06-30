import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Preprocessing",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Tahap Preprocessing Data")

st.caption("""
Tahap preprocessing merupakan bagian dari fase Data Preparation
dalam metodologi CRISP-DM. Pada tahap ini, data mentah hasil
pengumpulan dari platform X (Twitter) dibersihkan dan
distandardisasi agar siap digunakan pada proses Topic Modeling
menggunakan algoritma Latent Dirichlet Allocation (LDA).
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Tweet", "8.804")

with col2:
    st.metric("Bahasa", "Indonesia")

with col3:
    st.metric("Tahapan", "6 Proses")
    
st.markdown("---")

st.subheader("🔄 Pipeline Preprocessing")

tahapan = [
    (
        "1️⃣ Data Cleansing",
        "Menghapus URL, mention, hashtag, emoji, angka, tanda baca, dan karakter yang tidak diperlukan."
    ),
    (
        "2️⃣ Case Folding",
        "Mengubah seluruh huruf menjadi huruf kecil (lowercase) agar penulisan konsisten."
    ),
    (
        "3️⃣ Slang Normalization",
        "Mengubah kata-kata tidak baku atau bahasa gaul menjadi bentuk baku menggunakan kamus leksikon hibrida."
    ),
    (
        "4️⃣ Tokenizing",
        "Memecah setiap kalimat menjadi kumpulan kata (token)."
    ),
    (
        "5️⃣ Stopword Removal",
        "Menghapus kata-kata umum yang tidak memiliki makna topik, seperti 'dan', 'yang', 'di', dan sebagainya."
    ),
    (
        "6️⃣ Stemming",
        "Mengubah setiap kata menjadi bentuk dasar menggunakan algoritma Sastrawi."
    ),
]

for judul, isi in tahapan:
    with st.expander(judul):
        st.write(isi)
        
st.markdown("---")

st.subheader("📈 Visualisasi Hasil Preprocessing")

gambar = Path(
    "visualisasi/charts/preprocessing_kata_frekuensi.png"
)

if gambar.exists():

    st.image(
        str(gambar),
        use_container_width=True
    )

else:

    st.warning(
        "Visualisasi preprocessing tidak ditemukan."
    )
    
st.markdown("---")

st.subheader("📝 Interpretasi")

st.write("""
Visualisasi menunjukkan kata-kata yang paling sering muncul setelah
seluruh tahapan preprocessing selesai dilakukan.

Tahapan preprocessing berhasil mengurangi noise pada data,
menghilangkan kata-kata yang tidak informatif,
serta mempertahankan istilah-istilah yang memiliki makna penting
terhadap topik kesehatan mental remaja.

Dengan demikian, data menjadi lebih representatif
untuk digunakan pada proses Topic Modeling menggunakan
algoritma Latent Dirichlet Allocation (LDA).
""")

st.markdown("---")

st.subheader("💡 Insight")

st.info("""
Tahap preprocessing merupakan fondasi utama dalam penelitian berbasis
Natural Language Processing (NLP).

Kualitas hasil Topic Modeling sangat dipengaruhi oleh kualitas data
hasil preprocessing. Oleh karena itu, proses pembersihan dan
standardisasi teks dilakukan secara sistematis sebelum proses
pemodelan menggunakan algoritma LDA.
""")

st.markdown("---")

st.caption("""
Tahap preprocessing mengacu pada fase Data Preparation dalam
metodologi CRISP-DM dan menghasilkan dataset yang siap
digunakan untuk proses pemodelan topik.
""")