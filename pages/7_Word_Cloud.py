import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Word Cloud",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ Visualisasi Word Cloud")

st.caption("""
Visualisasi Word Cloud digunakan untuk memberikan gambaran intuitif
mengenai kata-kata dominan yang muncul pada setiap topik hasil
Topic Modeling menggunakan algoritma Latent Dirichlet Allocation (LDA).
""")

st.divider()

st.subheader("📖 Tujuan Visualisasi")

st.info("""
Word Cloud digunakan sebagai visualisasi pendukung untuk membantu
mengidentifikasi kata-kata yang memiliki probabilitas tinggi
dalam setiap topik.

Semakin besar ukuran suatu kata,
semakin tinggi pula bobot probabilitas kata tersebut
pada topik yang bersangkutan.
""")

left, right = st.columns(2)
with left:
    st.success("""
### Cara Membaca

• Ukuran kata menunjukkan tingkat dominasi.

• Semakin besar kata,
semakin sering kata tersebut muncul
pada topik tertentu.

• Warna tidak memiliki arti statistik,
hanya untuk meningkatkan visualisasi.
""")
    
with right:
    st.warning("""
### Insight

Word Cloud menunjukkan bahwa
kata-kata hasil preprocessing
berhasil dikelompokkan secara logis.

Sebagai contoh,
kata "tidur" dan "sakit"
berkumpul pada topik psikosomatis,
sementara kata "dreamies"
berada pada topik fandom.
""")
    
# Implementasi trik kolom [1, 6, 1] untuk meratakan gambar ke tengah
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    image = image = Image.open(
    "visualisasi/charts/wordcloud_per_topik.png"
)
    st.image(
        image,
        use_container_width=True
    )

st.caption("""
Gambar berikut menampilkan Word Cloud dari masing-masing
11 topik hasil pemodelan LDA.

Setiap panel merepresentasikan satu topik laten,
dengan ukuran kata menunjukkan besarnya probabilitas
kata tersebut dalam topik terkait.
""")

st.divider()

st.subheader("📝 Kesimpulan")

st.success("""
Visualisasi Word Cloud memperkuat hasil interpretasi
dengan menunjukkan bahwa algoritma LDA berhasil
mengelompokkan kata-kata yang memiliki hubungan
semantik ke dalam topik yang sesuai.

Hal ini memperlihatkan bahwa proses preprocessing,
normalisasi slang,
serta pemodelan topik telah menghasilkan
representasi topik yang koheren.
""")