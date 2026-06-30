import streamlit as st

st.set_page_config(
    page_title="Temuan Penelitian",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Temuan Penelitian")

st.caption("""
Halaman ini menyajikan hasil analisis utama yang diperoleh
dari proses Topic Modeling menggunakan algoritma
Latent Dirichlet Allocation (LDA).
""")

st.divider()

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Dataset", "8.804 Tweet")

with c2:
    st.metric("Topik", "11")

with c3:
    st.metric("Coherence", "0.4762")

with c4:
    st.metric("Perplexity", "-7.3441")

st.subheader("📌 Temuan Utama")

st.success("""
Penelitian menemukan bahwa percakapan mengenai kesehatan mental
remaja di platform X terbagi menjadi dua kelompok besar.

Kelompok pertama didominasi oleh ekspresi tekanan psikologis,
sedangkan kelompok kedua menunjukkan berbagai mekanisme koping
yang digunakan remaja dalam menghadapi tekanan tersebut.
""")

left,right = st.columns(2)
with left:

    st.error("""
### 🔴 Distress Expression

Topik:

• Kecemasan Klinis

• Psikosomatis

• Krisis Eksistensial

• Burnout Akademik

• Validasi Sosial

• Konflik Asmara

Kelompok ini merepresentasikan berbagai bentuk
tekanan psikologis yang dialami remaja.
""")

with right:

    st.success("""
### 🟢 Coping Mechanism

Topik:

• Fandom

• Cry for Help

• Media Hiburan

• Religius

• Rutinitas Harian

Kelompok ini menunjukkan bagaimana
remaja mencoba bertahan dari tekanan tersebut.
""")
    
st.divider()

st.subheader("⭐ Kebaruan (Novelty)")

st.info("""
Penelitian ini menemukan bahwa budaya fandom,
khususnya komunitas K-Pop,
tidak hanya berfungsi sebagai media hiburan.

Fandom berperan sebagai
digital sanctuary,
yakni ruang aman digital yang membantu remaja
mengurangi tekanan psikologis melalui
dukungan komunitas dan aktivitas bersama.

Temuan ini menjadi salah satu kebaruan utama
dibandingkan penelitian sebelumnya
yang umumnya hanya berfokus pada depresi
atau gangguan kecemasan.
""")

st.divider()

st.subheader("🎯 Kontribusi Penelitian")

st.write("""
Penelitian ini memberikan beberapa kontribusi penting:

• Mengimplementasikan metodologi CRISP-DM
  pada analisis Topic Modeling.

• Menggunakan kamus slang hibrida
  sehingga preprocessing lebih optimal.

• Menghasilkan interpretasi psikologis
  dari 11 topik laten.

• Menyediakan dashboard interaktif
  berbasis Streamlit sebagai media deployment.
""")

st.divider()

st.subheader("🌍 Implikasi Penelitian")

tab1,tab2,tab3 = st.tabs([
    "👥 Masyarakat",
    "🧠 Praktisi",
    "🎓 Akademisi"
])

with tab1:

    st.write("""
Mengurangi stigma terhadap
kesehatan mental remaja
serta meningkatkan kesadaran
masyarakat mengenai pentingnya
dukungan sosial.
""")

with tab2:

    st.write("""
Memberikan wawasan mengenai
mekanisme koping modern
remaja Indonesia
sebagai bahan pertimbangan
dalam proses konseling.
""")

with tab3:

    st.write("""
Metodologi dan proses preprocessing
dapat dijadikan referensi
bagi penelitian NLP
berbahasa Indonesia.
""")
    
st.divider()

st.subheader("📝 Kesimpulan")

st.success("""
Model Latent Dirichlet Allocation (LDA)
berhasil mengidentifikasi
11 topik utama
yang menggambarkan dinamika
percakapan kesehatan mental remaja.

Selain menunjukkan berbagai bentuk
tekanan psikologis,
hasil penelitian juga mengungkap
beragam strategi koping
yang digunakan remaja
untuk menghadapi tekanan tersebut.

Dengan demikian,
dashboard ini tidak hanya
menampilkan hasil pemodelan,
tetapi juga membantu
menginterpretasikan makna
di balik setiap topik yang ditemukan.
""")

