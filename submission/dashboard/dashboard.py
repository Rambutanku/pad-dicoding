import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Config Halaman Dashboard
st.set_page_config(page_title="Bike Sharing Analysis Dashboard", layout="wide")

# Load Data untuk Dashboard menggunakan relative path
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "main_data.csv")

    if not os.path.exists(csv_path):
        csv_path = "dashboard/main_data.csv"

    main_df = pd.read_csv(csv_path)

    # Fallback: Jika kolom 'hr' tidak ditemukan di main_data.csv, muat dari data/hour.csv
    if 'hr' not in main_df.columns:
        root_dir = os.path.dirname(base_dir)
        hour_path = os.path.join(root_dir, "data", "hour.csv")
        if not os.path.exists(hour_path):
            hour_path = "submission/data/hour.csv"
        
        if os.path.exists(hour_path):
            main_df = pd.read_csv(hour_path)

    main_df['dteday'] = pd.to_datetime(main_df['dteday'])
    return main_df

main_df = load_data()

# Judul Utama & Deskripsi
st.title("🚲 Bike Sharing Data Analysis Dashboard")
st.markdown("Dashboard interaktif untuk menganalisis pengaruh musim/cuaca serta pola jam penyewaan sepeda.")

# Sidebar Filter Tanggal
st.sidebar.header("Filter Rentang Waktu")
min_date = main_df['dteday'].min().date()
max_date = main_df['dteday'].max().date()

try:
    date_range = st.sidebar.date_input(
        "Pilih Rentang Tanggal:",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = main_df[(main_df['dteday'].dt.date >= start_date) &
                              (main_df['dteday'].dt.date <= end_date)]
    else:
        filtered_df = main_df
except Exception:
    filtered_df = main_df

# KPI Metrics Utama
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan (cnt)", value=f"{filtered_df['cnt'].sum():,}")
with col2:
    st.metric("Pengguna Terdaftar (registered)", value=f"{filtered_df['registered'].sum():,}")
with col3:
    st.metric("Pengguna Kasual (casual)", value=f"{filtered_df['casual'].sum():,}")

st.markdown("---")

# Mapping Kategori dan Label untuk Visualisasi
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
weather_map = {1: 'Clear/Partly Cloudy', 2: 'Misty/Cloudy', 3: 'Light Snow/Rain', 4: 'Severe Weather'}

df_plot = filtered_df.copy()
df_plot['season_label'] = df_plot['season'].map(season_map)
df_plot['weather_label'] = df_plot['weather_label'] if 'weather_label' in df_plot.columns else df_plot['weathersit'].map(weather_map)

# Tata Letak Visualisasi 2 Kolom
col_left, col_right = st.columns(2)

# ==============================================================================
# VISUALISASI PERTANYAAN 1: Grouped Bar Chart (Registered vs Season & Weather)
# ==============================================================================
with col_left:
    st.subheader("1. Penyewaan Pengguna Terdaftar (Registered)")
    st.caption("Berdasarkan Kombinasi Musim dan Kondisi Cuaca")

    # Agregasi Rerata Registered per Musim dan Cuaca
    group_p1 = df_plot.groupby(['season_label', 'weather_label'])['registered'].mean().reset_index()
    
    season_order = ['Spring', 'Summer', 'Fall', 'Winter']
    
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=group_p1,
        x='season_label',
        y='registered',
        hue='weather_label',
        order=season_order,
        ax=ax1,
        palette='Set2',
        errorbar=None
    )
    ax1.set_title("Rata-Rata Penyewaan Registered per Musim & Cuaca", fontsize=10, fontweight='bold')
    ax1.set_xlabel("Musim (Season)", fontsize=9)
    ax1.set_ylabel("Rata-Rata Penyewaan (Registered)", fontsize=9)
    ax1.legend(title="Kondisi Cuaca", loc='upper right', fontsize=8, title_fontsize=8)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    st.pyplot(fig1)

    # Detail Insight Pertanyaan 1
    with st.expander("📌 Lihat Detail Insight Pertanyaan 1"):
        st.write("""
        - **Kombinasi Puncak:** Rata-rata penyewaan pengguna terdaftar tertinggi terjadi pada **Musim Gugur (Fall)** dengan cuaca **Clear/Partly Cloudy** (4643.367647 sepeda/hari).
        - **Kombinasi Terendah:** Penyewaan terendah terjadi pada **Musim Semi (Spring)** dengan cuaca **Light Snow/Rain** (2317.000000 sepeda/hari).
        - **Dampak Cuaca:** Pada Musim Gugur (Fall), penurunan penyewaan dari cuaca Cerah ke Hujan/Salju Ringan mencapai **50.10%**.
        """)

# ==============================================================================
# VISUALISASI PERTANYAAN 2: Line Chart (Hourly Pattern: Workingday vs Non-Workingday)
# ==============================================================================
with col_right:
    st.subheader("2. Pola Penyewaan Sepeda Per Jam (cnt)")
    st.caption("Perbandingan Hari Kerja (Workingday) vs Non-Workingday")

    if 'hr' in df_plot.columns:
        df_plot['day_type'] = df_plot['workingday'].map({1: 'Workingday', 0: 'Non-Workingday'})
        
        # Agregasi Rerata Total Penyewaan (cnt) per jam dan jenis hari
        group_p2 = df_plot.groupby(['hr', 'day_type'])['cnt'].mean().reset_index()

        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.lineplot(
            data=group_p2,
            x='hr',
            y='cnt',
            hue='day_type',
            palette={'Workingday': '#2ecc71', 'Non-Workingday': '#e74c3c'},
            marker='o',
            linewidth=2,
            ax=ax2
        )
        ax2.set_title("Pola Jam Penyewaan: Workingday vs Non-Workingday", fontsize=10, fontweight='bold')
        ax2.set_xlabel("Jam (00:00 - 23:00)", fontsize=9)
        ax2.set_ylabel("Rata-Rata Penyewaan Total (cnt)", fontsize=9)
        ax2.set_xticks(range(0, 24, 2))
        ax2.legend(title="Jenis Hari", loc='upper left', fontsize=8, title_fontsize=8)
        ax2.grid(axis='both', linestyle='--', alpha=0.5)
        st.pyplot(fig2)

        # Detail Insight Pertanyaan 2
        with st.expander("📌 Lihat Detail Insight Pertanyaan 2"):
            st.write("""
            - **Workingday:** Membentuk pola dua puncak (*bimodal*) pada pukul **08:00** dan pukul **17:00**.
            - **Non-Workingday:** Membentuk pola puncak tunggal (*unimodal*) di siang hari yaitu pukul **13:00**.
            """)
    else:
        st.error("Data jam ('hr') tidak ditemukan. Pastikan file hour.csv tersedia di direktori data/.")
