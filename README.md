# 🧠 Mental Health Topic Dashboard

Dashboard interaktif berbasis **Streamlit** yang dikembangkan sebagai tahap **Deployment** pada penelitian skripsi berjudul:

> **Analisis Dinamika Topik Percakapan Publik Mengenai Kesehatan Mental Remaja di Platform X/Twitter Menggunakan Latent Dirichlet Allocation (LDA)**

Aplikasi ini memungkinkan pengguna mengeksplorasi hasil *Topic Modeling* secara interaktif melalui visualisasi, interpretasi topik, distribusi topik, Word Cloud, serta visualisasi **pyLDAvis** tanpa perlu menjalankan proses pemodelan ulang.

---

# 🌐 Live Demo

**Dashboard Streamlit**

https://mental-health-topic-dashboard-fx3gkdezpngakcurfc6fmp.streamlit.app/

---

# 📂 Repository

GitHub Repository

https://github.com/CarolDwiP/mental-health-topic-dashboard

---

# 📖 Tentang Penelitian

Penelitian ini bertujuan untuk menganalisis dinamika topik percakapan publik mengenai **kesehatan mental remaja** pada platform **X/Twitter** menggunakan algoritma **Latent Dirichlet Allocation (LDA)**.

Metodologi penelitian mengikuti framework **CRISP-DM (Cross Industry Standard Process for Data Mining)** yang terdiri dari enam tahapan:

- Business Understanding
- Data Understanding
- Data Preparation
- Modeling
- Evaluation
- Deployment

Model terbaik berhasil menghasilkan:

- 📊 Jumlah Tweet : **8.804**
- 🧠 Jumlah Topik : **11**
- 📈 Coherence Score (Cv) : **0.4762**
- 🤖 Algoritma : **Latent Dirichlet Allocation (LDA)**

---

# ✨ Fitur Dashboard

Dashboard terdiri dari beberapa halaman utama, yaitu:

- 🏠 Dashboard Utama
- 📄 Dataset
- 🧹 Preprocessing
- 🧠 Topic Modeling
- 📊 Visualisasi LDA (pyLDAvis)
- 📈 Distribusi Topik
- ☁️ Word Cloud
- 📚 Interpretasi Topik
- 🔍 Temuan Penelitian
- ℹ️ Tentang Penelitian

---

# 🛠️ Teknologi yang Digunakan

Framework

- Streamlit

Bahasa Pemrograman

- Python

Library

- Pandas
- NumPy
- Gensim
- pyLDAvis
- Plotly
- Matplotlib
- WordCloud
- Pillow

Version Control

- Git
- GitHub

Deployment

- Streamlit Community Cloud

---

# 📁 Struktur Project

```text
mental-health-topic-dashboard/
│
├── app.py
├── assets/
│
├── components/
│
├── data/
│   ├── data_bersih.csv
│   ├── data_final_dengan_topik.csv
│   ├── project_info.py
│   └── topic_data.py
│
├── pages/
│   ├── 1_Dataset.py
│   ├── 2_Preprocessing.py
│   ├── 3_Topic_Modeling.py
│   ├── 4_Visualisasi_LDA.py
│   ├── 5_Distribusi_Topik.py
│   ├── 6_Interpretasi_Topik.py
│   ├── 7_Word_Cloud.py
│   ├── 8_Temuan_Penelitian.py
│   └── 9_Tentang_Penelitian.py
│
├── utils/
│
├── visualisasi/
│   ├── charts/
│   └── pyldavis/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Cara Menjalankan Secara Lokal

Clone repository

```bash
git clone https://github.com/CarolDwiP/mental-health-topic-dashboard.git
```

Masuk ke folder project

```bash
cd mental-health-topic-dashboard
```

Install seluruh dependency

```bash
pip install -r requirements.txt
```

Jalankan aplikasi

```bash
streamlit run app.py
```

Aplikasi akan berjalan pada browser secara lokal.

---

# 📊 Hasil Dashboard

Dashboard menyajikan berbagai hasil analisis secara interaktif, di antaranya:

- Ringkasan penelitian
- Statistik dataset
- Tahapan preprocessing
- Evaluasi model LDA
- Visualisasi pyLDAvis
- Distribusi topik
- Word Cloud
- Interpretasi setiap topik
- Temuan penelitian
- Informasi penelitian

---

# 🎓 Tujuan Pengembangan

Dashboard ini dikembangkan sebagai implementasi tahap **Deployment** dalam metodologi **CRISP-DM**, sehingga hasil pemodelan tidak hanya berhenti pada proses analisis, tetapi juga dapat diakses dan dieksplorasi secara interaktif melalui antarmuka web.

---

# 👨‍🎓 Author

**Carol Dwi P**

Program Studi Teknik Informatika

Universitas Muhammadiyah Sukabumi

---

# 📄 Lisensi

Repository ini dibuat untuk keperluan penelitian akademik dan penyusunan skripsi.

Apabila digunakan sebagai referensi, mohon mencantumkan sumber sesuai etika akademik.