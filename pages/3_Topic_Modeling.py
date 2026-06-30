import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Topic Modeling",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Topic Modeling Menggunakan LDA")

st.caption("""
Halaman ini menjelaskan proses pemodelan topik menggunakan algoritma
Latent Dirichlet Allocation (LDA), termasuk proses penentuan jumlah
topik optimal berdasarkan evaluasi Coherence Score dan Perplexity.
""")

st.divider()

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Jumlah Tweet",
        "8.804"
    )

with col2:
    st.metric(
        "Topik Optimal",
        "11"
    )

with col3:
    st.metric(
        "Coherence",
        "0.4762"
    )

with col4:
    st.metric(
        "Perplexity",
        "-7.3441"
    )
    
st.markdown("---")

st.subheader("📖 Apa itu Latent Dirichlet Allocation (LDA)?")

st.write("""
Latent Dirichlet Allocation (LDA) merupakan algoritma Topic Modeling
berbasis probabilistik yang termasuk dalam kategori
Unsupervised Learning.

LDA bekerja dengan mengasumsikan bahwa setiap dokumen merupakan
kombinasi dari beberapa topik, sedangkan setiap topik terdiri
atas kumpulan kata yang memiliki probabilitas kemunculan tertentu.

Melalui pendekatan tersebut, LDA mampu menemukan pola topik
tersembunyi (latent topics) tanpa memerlukan proses pelabelan data
secara manual.
""")

st.markdown("---")

st.subheader("📈 Evaluasi Model")

gambar = Path(
    "visualisasi/charts/grafik_coherence_perplexity.png"
)

if gambar.exists():

    st.image(
        str(gambar),
        use_container_width=True
    )

else:

    st.warning(
        "Grafik evaluasi model belum ditemukan."
    )
    
st.markdown("---")

st.subheader("📝 Interpretasi Hasil")

st.write("""
Pengujian dilakukan terhadap beberapa jumlah topik (K) untuk
menemukan model yang paling representatif.

Evaluasi menggunakan dua metrik utama, yaitu Coherence Score dan
Perplexity.

Model terbaik diperoleh pada jumlah topik sebanyak 11 karena
menghasilkan nilai Coherence Score tertinggi sebesar 0,4762,
dengan nilai Perplexity sebesar -7,3441.

Hasil tersebut menunjukkan bahwa model memiliki keseimbangan yang
baik antara kualitas interpretasi topik dan kemampuan generalisasi.
""")

st.markdown("---")

st.subheader("🎯 Mengapa Memilih 11 Topik?")

st.success("""
Jumlah topik sebanyak 11 dipilih karena memberikan nilai
Coherence Score tertinggi selama proses pengujian.

Pada jumlah topik yang lebih kecil,
beberapa tema masih bercampur sehingga sulit diinterpretasikan.

Sedangkan pada jumlah topik yang lebih besar,
topik mulai terpecah menjadi kelompok yang terlalu spesifik
(overlapping).

Oleh karena itu, K=11 dipilih sebagai jumlah topik optimal
untuk merepresentasikan percakapan kesehatan mental remaja
di platform X (Twitter).
""")

st.markdown("---")

st.subheader("💡 Insight Penelitian")

st.info("""
Pemilihan jumlah topik yang tepat merupakan salah satu faktor
terpenting dalam Topic Modeling.

Model akhir berhasil mengidentifikasi sebelas tema utama yang
merepresentasikan dinamika percakapan mengenai kesehatan mental
remaja di media sosial.

Topik-topik tersebut selanjutnya divisualisasikan secara interaktif
menggunakan pyLDAvis agar hubungan antar topik dan kata kunci
dapat dianalisis lebih mendalam.
""")

st.markdown("---")

st.caption("""
Model Topic Modeling dibangun menggunakan algoritma
Latent Dirichlet Allocation (LDA)
berdasarkan kerangka kerja CRISP-DM.
""")