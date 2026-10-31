# Proyek Analisis Data - Bike Sharing Dataset

Proyek ini merupakan bagian dari submission akhir untuk kursus **Belajar Analisis Data dengan Python** di Dicoding. Proyek ini bertujuan untuk melakukan analisis data eksploratif (EDA) dan membangun dashboard interaktif menggunakan Streamlit.

## Link Live Dashboard
Aplikasi dashboard interaktif dapat diakses melalui tautan berikut:
- **Streamlit App:** https://pad-dicoding-c3pejk8bpn6p4kxvqcdcuy.streamlit.app/

---

## Deskripsi Proyek
Proyek ini menganalisis dataset **Bike Sharing Dataset** untuk menjawab beberapa pertanyaan bisnis utama:
1. **Pertanyaan Bisnis 1:** Bagaimana pengaruh kombinasi musim (season) dan kondisi cuaca (weathersit) terhadap rata-rata jumlah penyewaan harian oleh pengguna terdaftar (registered)?
2. **Pertanyaan Bisnis 2:** Bagaimana perbedaan pola rata-rata penyewaan sepeda (cnt) per jam (hr) antara hari kerja (workingday) dan hari non-kerja (non-workingday)?

---

## Struktur Direktori
```text
.
submission
├── dashboard
│   ├── dashboard.py
│   └── main_data.csv
├── data
│   ├── data_1.csv
│   └── data_2.csv
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
git clone https://github.com/Rambutanku/pad-dicoding.git
cd pad-dicoding
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
