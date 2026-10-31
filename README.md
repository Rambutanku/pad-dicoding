# Proyek Analisis Data - [Nama Dataset / Topik Proyek]

Proyek ini merupakan bagian dari submission akhir untuk kursus **Belajar Analisis Data dengan Python** di Dicoding. Proyek ini bertujuan untuk melakukan analisis data eksploratif (EDA) dan membangun dashboard interaktif menggunakan Streamlit.

## Link Live Dashboard
Aplikasi dashboard interaktif dapat diakses melalui tautan berikut:
- **Streamlit App:** [Masukkan URL Streamlit Community Cloud Anda di sini]

---

## Deskripsi Proyek
Proyek ini menganalisis dataset **[Nama Dataset]** untuk menjawab beberapa pertanyaan bisnis utama:
1. **Pertanyaan 1:** [Tuliskan pertanyaan bisnis pertama Anda]
2. **Pertanyaan 2:** [Tuliskan pertanyaan bisnis kedua Anda]

---

## Struktur Direktori
```text
.
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── [file_data_1].csv
│   └── [file_data_2].csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## Cara Menjalankan Dashboard Secara Lokal

### 1. Prasyarat (Prerequisites)
Pastikan Anda telah menginstal **Python 3.8+** di perangkat Anda.

### 2. Clone atau Unduh Repositori
```bash
git clone https://github.com/[username-anda]/[nama-repo].git
cd [nama-repo]
```

### 3. Buat dan Aktifkan Virtual Environment (Opsional tetapi Disarankan)
* **Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Instal Dependency
Instal seluruh library yang dibutuhkan dengan menjalankan perintah berikut:
```bash
pip install -r requirements.txt
```

### 5. Jalankan Aplikasi Streamlit
Masuk ke direktori `dashboard` (jika file `dashboard.py` berada di dalam folder tersebut) atau jalankan langsung perintah:
```bash
streamlit run dashboard/dashboard.py
```
Aplikasi akan secara otomatis terbuka di peramban (browser) default Anda di alamat `http://localhost:8501`.
