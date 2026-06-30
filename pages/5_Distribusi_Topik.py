import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Distribusi Topik",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Distribusi Topik")

st.caption("""
Halaman ini menampilkan distribusi jumlah dokumen pada setiap topik
hasil pemodelan menggunakan algoritma Latent Dirichlet Allocation (LDA).
Distribusi ini memberikan gambaran mengenai dominasi masing-masing topik
dalam keseluruhan korpus penelitian.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Topik", "11")

with col2:
    st.metric("Jumlah Tweet", "8.804")

with col3:
    st.metric("Model", "LDA")
    
st.markdown("---")

st.subheader("📈 Grafik Distribusi Topik")

gambar = Path(
    "visualisasi/charts/distribusi_topik.png"
)

if gambar.exists():

    st.image(
        str(gambar),
        use_container_width=True
    )

else:

    st.warning(
        "Grafik distribusi topik tidak ditemukan."
    )

st.markdown("---")

st.subheader("📝 Interpretasi")

st.write("""
Grafik distribusi topik menunjukkan proporsi jumlah dokumen yang
termasuk ke dalam masing-masing topik hasil pemodelan.

Perbedaan tinggi batang pada grafik menunjukkan bahwa tidak semua
topik memiliki tingkat kemunculan yang sama. Beberapa topik muncul
lebih dominan, sedangkan topik lainnya memiliki proporsi yang lebih
kecil.

Distribusi ini mengindikasikan bahwa percakapan mengenai kesehatan
mental remaja di platform X (Twitter) memiliki fokus yang beragam,
namun tetap didominasi oleh beberapa tema utama.
""")

st.markdown("---")

st.subheader("💡 Insight")

st.info("""
Distribusi topik membantu memahami intensitas kemunculan setiap tema
dalam keseluruhan dataset.

Topik dengan proporsi terbesar menunjukkan isu yang paling banyak
dibicarakan oleh pengguna, sedangkan topik dengan proporsi lebih kecil
tetap memberikan informasi penting mengenai variasi dinamika
percakapan publik mengenai kesehatan mental remaja.
""")

st.markdown("---")

st.caption("""
Distribusi topik dihitung berdasarkan jumlah dokumen dominan pada
masing-masing topik hasil pemodelan Latent Dirichlet Allocation (LDA).
""")