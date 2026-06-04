import streamlit as st
import json
import os
import datetime
from pathlib import Path

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Research Portal — Dewi Pika Lumbanbatu, S.H., M.H",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Data Storage ─────────────────────────────────────────────────────────────
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def load_json(filename):
    path = DATA_DIR / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_json(filename, data):
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_dict(filename):
    path = DATA_DIR / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_dict(filename, data):
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Nunito:wght@300;400;600;700&display=swap');

:root {
    --rose:     #c9507a;
    --rose-lt:  #f7d6e3;
    --gold:     #b8935a;
    --gold-lt:  #f5ecd7;
    --navy:     #1a2744;
    --cream:    #fdf8f4;
    --blush:    #fce8ef;
    --text:     #2d2d2d;
    --muted:    #7a7a7a;
    --card-bg:  #ffffff;
    --border:   #e8ddd5;
}

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
    background-color: var(--cream);
    color: var(--text);
}

/* ── Sidebar ──────────────────────── */
[data-testid="stSidebar"] {
    background: linear-gradient(175deg, #1a2744 0%, #2e3f6b 60%, #c9507a 100%) !important;
}
[data-testid="stSidebar"] * { color: #ffffff !important; }
[data-testid="stSidebar"] .stRadio label { 
    font-size: 0.95rem; 
    padding: 6px 0; 
    cursor: pointer;
}

/* ── Titles ───────────────────────── */
h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif;
}

/* ── Cards ───────────────────────── */
.card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 20px;
    box-shadow: 0 4px 24px rgba(201,80,122,0.07);
}

.hero-banner {
    background: linear-gradient(135deg, #1a2744 0%, #2e3f6b 50%, #c9507a 100%);
    border-radius: 20px;
    padding: 48px 40px;
    color: white;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: "❤";
    position: absolute;
    right: 40px; top: 30px;
    font-size: 120px;
    opacity: 0.08;
}
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.8rem;
    font-weight: 300;
    line-height: 1.2;
    margin: 0 0 8px 0;
}
.hero-subtitle {
    font-size: 1.05rem;
    opacity: 0.85;
    margin: 0 0 4px 0;
}
.hero-credit {
    font-size: 0.82rem;
    opacity: 0.55;
    margin-top: 16px;
    font-style: italic;
}

/* ── Motivation Box ───────────────── */
.motivation-box {
    background: linear-gradient(135deg, var(--blush) 0%, var(--gold-lt) 100%);
    border-left: 4px solid var(--rose);
    border-radius: 12px;
    padding: 20px 24px;
    margin: 16px 0;
}
.motivation-quote {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem;
    font-style: italic;
    color: var(--navy);
    line-height: 1.6;
}
.motivation-author {
    font-size: 0.82rem;
    color: var(--rose);
    font-weight: 600;
    margin-top: 8px;
}

/* ── Badges ───────────────────────── */
.badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 99px;
    font-size: 0.78rem;
    font-weight: 700;
    margin: 2px;
}
.badge-rose   { background: var(--rose-lt); color: var(--rose); }
.badge-gold   { background: var(--gold-lt); color: #8a6930; }
.badge-navy   { background: #e3e8f5; color: var(--navy); }

/* ── Section Header ───────────────── */
.section-header {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.9rem;
    color: var(--navy);
    border-bottom: 2px solid var(--rose-lt);
    padding-bottom: 8px;
    margin-bottom: 24px;
}

/* ── Log Item ─────────────────────── */
.log-item {
    background: var(--cream);
    border-left: 3px solid var(--gold);
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    margin-bottom: 12px;
}
.log-date {
    font-size: 0.78rem;
    color: var(--muted);
    font-weight: 600;
}
.log-content {
    font-size: 0.95rem;
    margin-top: 4px;
    color: var(--text);
}

/* ── Stat Boxes ───────────────────── */
.stat-box {
    background: linear-gradient(135deg, var(--navy) 0%, #2e3f6b 100%);
    color: white;
    border-radius: 14px;
    padding: 22px 20px;
    text-align: center;
}
.stat-number {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.4rem;
    font-weight: 600;
    line-height: 1;
}
.stat-label {
    font-size: 0.8rem;
    opacity: 0.75;
    margin-top: 4px;
}

/* ── Data Table ───────────────────── */
.data-row {
    background: white;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 10px;
    transition: box-shadow .2s;
}
.data-row:hover { box-shadow: 0 4px 16px rgba(201,80,122,0.10); }
.data-row-title {
    font-weight: 700;
    color: var(--navy);
    font-size: 1.0rem;
}
.data-row-meta {
    font-size: 0.8rem;
    color: var(--muted);
    margin-top: 3px;
}

/* ── Divider ──────────────────────── */
.divider {
    height: 1px;
    background: linear-gradient(to right, transparent, var(--rose-lt), transparent);
    margin: 28px 0;
}

/* ── Footer ───────────────────────── */
.footer {
    text-align: center;
    padding: 28px 0 12px;
    font-size: 0.8rem;
    color: var(--muted);
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

# ─── Motivational Quotes ───────────────────────────────────────────────────────
MOTIVATIONS = [
    ("Pendidikan adalah senjata paling ampuh yang dapat Anda gunakan untuk mengubah dunia.",
     "Nelson Mandela"),
    ("Jangan berhenti belajar, karena hidup tidak berhenti mengajar. Setiap halaman yang kamu baca membawa kamu lebih dekat ke versi terbaik dirimu.",
     "Ralph Waldo Emerson"),
    ("Penelitian adalah melihat apa yang semua orang lihat, namun memikirkan apa yang belum pernah dipikirkan siapapun.",
     "Albert Szent-Györgyi"),
    ("Keberhasilan bukan tentang seberapa cepat kamu sampai di tujuan, melainkan tentang seberapa kuat kamu bertahan dalam perjalanan.",
     "Winston Churchill"),
    ("Seorang ahli hukum yang baik bukan hanya memahami teks hukum, tetapi juga jiwa dari keadilan itu sendiri.",
     "Oliver Wendell Holmes"),
    ("Ilmu tanpa semangat adalah buku yang tak pernah dibuka. Teruslah bersemangat, Ibu — karya besarmu sedang dalam proses! 💗",
     "Dedikasi Khusus"),
]

import random

def get_motivation():
    return random.choice(MOTIVATIONS)

# ─── Sidebar Navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:20px 0 10px'>
        <div style='font-size:2.4rem'>⚖️</div>
        <div style='font-family:Cormorant Garamond,serif; font-size:1.2rem; 
                    font-weight:600; line-height:1.3; margin-top:6px'>
            Research Portal
        </div>
        <div style='font-size:0.72rem; opacity:.6; margin-top:4px'>
            Dewi Pika Lumbanbatu, S.H., M.H
        </div>
        <hr style='border-color:rgba(255,255,255,0.2); margin:16px 0'>
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "Navigasi",
        ["🏠  Beranda",
         "📚  Penelitian I",
         "📖  Penelitian II",
         "📋  Kuesioner",
         "✏️  Revisi Artikel",
         "📓  Log Harian",
         "🗂️  Arsip Tugas"],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border-color:rgba(255,255,255,0.2)'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.7rem; opacity:.5; text-align:center; padding-bottom:12px'>
        💻 Dibuat dengan ❤️ oleh<br>
        <b>Gita Oktaviani Sitorus</b>
    </div>
    """, unsafe_allow_html=True)

page = menu

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: BERANDA
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠  Beranda":

    # Hero
    now = datetime.datetime.now()
    greeting = "SELAMAT DATANG IBU PERI" if now.hour < 11 else ("SELAMAT DATANG IBU PERI" if now.hour < 15 else ("SELAMAT DATANG IBU PERI" if now.hour < 18 else "SELAMAT DATANG IBU PERI"))
    st.markdown(f"""
    <div class="hero-banner">
        <div class="hero-title">✨ {greeting}, Ibu Dewi!</div>
        <div class="hero-subtitle">Dewi Pika Lumbanbatu, S.H., M.H</div>
        <div class="hero-subtitle" style="opacity:.65; font-size:.9rem">
            {now.strftime("%A, %d %B %Y · %H:%M")}
        </div>
        <div class="hero-credit">Portal Penelitian Pribadi · Dirancang penuh cinta oleh Gita Oktaviani Sitorus 💗</div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    p1 = load_json("penelitian1.json")
    p2 = load_json("penelitian2.json")
    kuesioner = load_json("kuesioner.json")
    revisi = load_json("revisi.json")
    log_data = load_json("log.json")
    tugas = load_json("tugas.json")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{len(p1)+len(p2)}</div>
            <div class="stat-label">Total Data Penelitian</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{len(kuesioner)}</div>
            <div class="stat-label">Entri Kuesioner</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{len(revisi)}</div>
            <div class="stat-label">Revisi Artikel</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="stat-box">
            <div class="stat-number">{len(log_data)}</div>
            <div class="stat-label">Catatan Log</div></div>""", unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Motivation
    col_m, col_r = st.columns([2, 1])
    with col_m:
        st.markdown("<div class='section-header'>💌 Pesan Semangat Hari Ini</div>", unsafe_allow_html=True)
        quote, author = get_motivation()
        st.markdown(f"""
        <div class="motivation-box">
            <div class="motivation-quote">"{quote}"</div>
            <div class="motivation-author">— {author}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style='background:#fdf0f5; border-radius:12px; padding:16px 20px; margin-top:12px;
                    border:1px dashed #c9507a; font-size:.92rem; color:#1a2744; line-height:1.7'>
            🌹 <b>Ibu Dewi</b>, setiap halaman penelitian yang Ibu tulis adalah warisan ilmu 
            yang tak ternilai. Perjalanan akademis Ibu adalah inspirasi bagi banyak orang. 
            Tetap semangat, tetap bersinar! <b> Awak Gita selalu mendukung Ibu.</b> 💗
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown("<div class='section-header'>📌 Log Terbaru</div>", unsafe_allow_html=True)
        recent = log_data[-4:][::-1] if log_data else []
        if recent:
            for item in recent:
                st.markdown(f"""
                <div class="log-item">
                    <div class="log-date">📅 {item.get('tanggal','')}</div>
                    <div class="log-content">{item.get('catatan','')[:90]}{'...' if len(item.get('catatan',''))>90 else ''}</div>
                </div>""", unsafe_allow_html=True)
        else:
            st.info("Belum ada log. Mulai catat aktivitas Ibu! ✍️")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: PENELITIAN I
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📚  Penelitian I":
    st.markdown("<div class='section-header'>📚 Data Penelitian I</div>", unsafe_allow_html=True)

    quote, author = get_motivation()
    st.markdown(f"""
    <div class="motivation-box">
        <div class="motivation-quote">"{quote}"</div>
        <div class="motivation-author">— {author}</div>
    </div>""", unsafe_allow_html=True)

    # Form tambah
    with st.expander("➕ Tambah Data Penelitian I", expanded=False):
        with st.form("form_p1", clear_on_submit=True):
            st.markdown("#### Isi Data Baru")
            col1, col2 = st.columns(2)
            with col1:
                judul    = st.text_input("📌 Judul / Topik")
                responden = st.text_input("👤 Nama Responden / Informan")
                tanggal  = st.date_input("📅 Tanggal Pengambilan Data")
            with col2:
                lokasi   = st.text_input("📍 Lokasi / Instansi")
                kategori = st.selectbox("🏷️ Kategori", ["Wawancara","Observasi","Dokumentasi","Studi Kepustakaan","Lainnya"])
                status   = st.selectbox("✅ Status", ["Proses","Selesai","Perlu Tindak Lanjut"])
            deskripsi = st.text_area("📝 Deskripsi / Hasil")
            catatan   = st.text_area("🗒️ Catatan Tambahan")

            if st.form_submit_button("💾 Simpan Data", use_container_width=True):
                if judul:
                    data = load_json("penelitian1.json")
                    data.append({
                        "id": len(data)+1,
                        "judul": judul, "responden": responden,
                        "tanggal": str(tanggal), "lokasi": lokasi,
                        "kategori": kategori, "status": status,
                        "deskripsi": deskripsi, "catatan": catatan,
                        "dibuat": datetime.datetime.now().isoformat()
                    })
                    save_json("penelitian1.json", data)
                    st.success("✅ Data Penelitian I berhasil disimpan!")
                    st.balloons()
                else:
                    st.warning("Judul wajib diisi.")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Display
    data = load_json("penelitian1.json")
    if data:
        # Filter
        col_s, col_f = st.columns([3, 1])
        with col_s:
            search = st.text_input("🔍 Cari...", placeholder="Ketik judul atau nama responden")
        with col_f:
            filter_kat = st.selectbox("Filter", ["Semua","Wawancara","Observasi","Dokumentasi","Studi Kepustakaan","Lainnya"])

        filtered = [d for d in data if
                    (search.lower() in d.get("judul","").lower() or search.lower() in d.get("responden","").lower() or not search)
                    and (filter_kat == "Semua" or d.get("kategori") == filter_kat)]

        st.markdown(f"**{len(filtered)} data ditemukan**")
        for i, d in enumerate(reversed(filtered)):
            color_map = {"Selesai": "#27ae60", "Proses": "#f39c12", "Perlu Tindak Lanjut": "#e74c3c"}
            color = color_map.get(d.get("status",""), "#888")
            with st.expander(f"📌 {d.get('judul','—')}  ·  {d.get('tanggal','')}"):
                c1, c2 = st.columns(2)
                with c1:
                    st.write(f"**Responden:** {d.get('responden','-')}")
                    st.write(f"**Lokasi:** {d.get('lokasi','-')}")
                    st.write(f"**Kategori:** {d.get('kategori','-')}")
                with c2:
                    st.markdown(f"**Status:** <span style='color:{color};font-weight:700'>{d.get('status','-')}</span>", unsafe_allow_html=True)
                    st.write(f"**Tanggal:** {d.get('tanggal','-')}")
                st.write(f"**Deskripsi:** {d.get('deskripsi','-')}")
                if d.get("catatan"):
                    st.write(f"**Catatan:** {d.get('catatan')}")

                if st.button(f"🗑️ Hapus", key=f"del_p1_{i}"):
                    idx = data.index(d)
                    data.pop(idx)
                    save_json("penelitian1.json", data)
                    st.rerun()
    else:
        st.info("Belum ada data. Silakan tambah data penelitian pertama Ibu! 💗")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: PENELITIAN II
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📖  Penelitian II":
    st.markdown("<div class='section-header'>📖 Data Penelitian II</div>", unsafe_allow_html=True)

    quote, author = get_motivation()
    st.markdown(f"""
    <div class="motivation-box">
        <div class="motivation-quote">"{quote}"</div>
        <div class="motivation-author">— {author}</div>
    </div>""", unsafe_allow_html=True)

    with st.expander("➕ Tambah Data Penelitian II", expanded=False):
        with st.form("form_p2", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                judul    = st.text_input("📌 Judul / Topik")
                responden = st.text_input("👤 Nama Responden / Informan")
                tanggal  = st.date_input("📅 Tanggal")
            with col2:
                lokasi   = st.text_input("📍 Lokasi / Instansi")
                kategori = st.selectbox("🏷️ Kategori", ["Wawancara","Observasi","Dokumentasi","Analisis Normatif","Lainnya"])
                status   = st.selectbox("✅ Status", ["Proses","Selesai","Perlu Tindak Lanjut"])
            variabel  = st.text_input("📊 Variabel Penelitian")
            deskripsi = st.text_area("📝 Deskripsi / Hasil Temuan")
            catatan   = st.text_area("🗒️ Catatan Tambahan")

            if st.form_submit_button("💾 Simpan Data", use_container_width=True):
                if judul:
                    data = load_json("penelitian2.json")
                    data.append({
                        "id": len(data)+1,
                        "judul": judul, "responden": responden,
                        "tanggal": str(tanggal), "lokasi": lokasi,
                        "kategori": kategori, "status": status,
                        "variabel": variabel, "deskripsi": deskripsi,
                        "catatan": catatan,
                        "dibuat": datetime.datetime.now().isoformat()
                    })
                    save_json("penelitian2.json", data)
                    st.success("✅ Data Penelitian II berhasil disimpan!")
                    st.balloons()
                else:
                    st.warning("Judul wajib diisi.")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    data = load_json("penelitian2.json")
    if data:
        search = st.text_input("🔍 Cari data...", key="s2")
        filtered = [d for d in data if search.lower() in d.get("judul","").lower() or not search]
        st.markdown(f"**{len(filtered)} data ditemukan**")
        for i, d in enumerate(reversed(filtered)):
            with st.expander(f"📖 {d.get('judul','—')}  ·  {d.get('tanggal','')}"):
                c1, c2 = st.columns(2)
                with c1:
                    st.write(f"**Responden:** {d.get('responden','-')}")
                    st.write(f"**Lokasi:** {d.get('lokasi','-')}")
                    st.write(f"**Variabel:** {d.get('variabel','-')}")
                with c2:
                    st.write(f"**Kategori:** {d.get('kategori','-')}")
                    st.write(f"**Status:** {d.get('status','-')}")
                st.write(f"**Deskripsi:** {d.get('deskripsi','-')}")
                if d.get("catatan"):
                    st.write(f"**Catatan:** {d.get('catatan')}")
                if st.button(f"🗑️ Hapus", key=f"del_p2_{i}"):
                    idx = data.index(d)
                    data.pop(idx)
                    save_json("penelitian2.json", data)
                    st.rerun()
    else:
        st.info("Belum ada data penelitian II. Yuk tambahkan! 💪")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: KUESIONER
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📋  Kuesioner":
    st.markdown("<div class='section-header'>📋 Manajemen Kuesioner</div>", unsafe_allow_html=True)

    quote, author = get_motivation()
    st.markdown(f"""
    <div class="motivation-box">
        <div class="motivation-quote">"{quote}"</div>
        <div class="motivation-author">— {author}</div>
    </div>""", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📥 Tambah Entri", "📊 Lihat Data"])

    with tab1:
        with st.form("form_kuesioner", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                nama       = st.text_input("👤 Nama Responden")
                pekerjaan  = st.text_input("💼 Pekerjaan / Jabatan")
                tanggal    = st.date_input("📅 Tanggal Pengisian")
            with col2:
                usia       = st.number_input("🎂 Usia", 18, 100, 30)
                jk         = st.selectbox("⚧ Jenis Kelamin", ["Laki-laki","Perempuan","Lainnya"])
                topik      = st.text_input("📌 Topik Kuesioner")

            st.markdown("**Jawaban Kuesioner:**")
            jawaban = {}
            for i in range(1, 6):
                jawaban[f"pertanyaan_{i}"] = st.text_area(f"Pertanyaan {i}", key=f"q_{i}")

            catatan = st.text_area("📝 Catatan Tambahan")

            if st.form_submit_button("💾 Simpan Kuesioner", use_container_width=True):
                if nama:
                    data = load_json("kuesioner.json")
                    data.append({
                        "id": len(data)+1,
                        "nama": nama, "pekerjaan": pekerjaan,
                        "usia": usia, "jk": jk, "topik": topik,
                        "tanggal": str(tanggal),
                        "jawaban": jawaban, "catatan": catatan,
                        "dibuat": datetime.datetime.now().isoformat()
                    })
                    save_json("kuesioner.json", data)
                    st.success("✅ Data kuesioner tersimpan!")
                    st.balloons()
                else:
                    st.warning("Nama responden wajib diisi.")

    with tab2:
        data = load_json("kuesioner.json")
        if data:
            st.markdown(f"**Total responden: {len(data)}**")
            for i, d in enumerate(reversed(data)):
                with st.expander(f"👤 {d.get('nama','?')} · {d.get('tanggal','')} · {d.get('topik','-')}"):
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write(f"**Pekerjaan:** {d.get('pekerjaan','-')}")
                        st.write(f"**Usia:** {d.get('usia','-')}")
                        st.write(f"**JK:** {d.get('jk','-')}")
                    with c2:
                        st.write(f"**Topik:** {d.get('topik','-')}")
                        st.write(f"**Tanggal:** {d.get('tanggal','-')}")
                    for k, v in d.get("jawaban", {}).items():
                        if v:
                            st.write(f"**{k.replace('_',' ').title()}:** {v}")
                    if d.get("catatan"):
                        st.write(f"**Catatan:** {d.get('catatan')}")
                    if st.button("🗑️ Hapus", key=f"del_k_{i}"):
                        idx = data.index(d)
                        data.pop(idx)
                        save_json("kuesioner.json", data)
                        st.rerun()
        else:
            st.info("Belum ada data kuesioner.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: REVISI ARTIKEL
# ══════════════════════════════════════════════════════════════════════════════
elif page == "✏️  Revisi Artikel":
    st.markdown("<div class='section-header'>✏️ Revisi Artikel</div>", unsafe_allow_html=True)

    quote, author = get_motivation()
    st.markdown(f"""
    <div class="motivation-box">
        <div class="motivation-quote">"{quote}"</div>
        <div class="motivation-author">— {author}</div>
    </div>""", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📝 Tambah Revisi", "📚 Riwayat Revisi"])

    with tab1:
        with st.form("form_revisi", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                judul_artikel = st.text_input("📄 Judul Artikel")
                jurnal        = st.text_input("📰 Nama Jurnal / Konferensi")
                tanggal_rev   = st.date_input("📅 Tanggal Revisi")
            with col2:
                versi         = st.text_input("🔢 Versi (mis: v1, v2, Final)", "v1")
                status_rev    = st.selectbox("📊 Status", ["Draf","Revisi Minor","Revisi Mayor","Menunggu Reviewer","Accepted","Published"])
                reviewer      = st.text_input("👨‍🏫 Nama Reviewer / Pembimbing")

            catatan_rev   = st.text_area("📝 Catatan Revisi / Komentar Reviewer")
            perubahan     = st.text_area("🔄 Perubahan yang Dilakukan")

            if st.form_submit_button("💾 Simpan Revisi", use_container_width=True):
                if judul_artikel:
                    data = load_json("revisi.json")
                    data.append({
                        "id": len(data)+1,
                        "judul_artikel": judul_artikel, "jurnal": jurnal,
                        "tanggal_rev": str(tanggal_rev), "versi": versi,
                        "status_rev": status_rev, "reviewer": reviewer,
                        "catatan_rev": catatan_rev, "perubahan": perubahan,
                        "dibuat": datetime.datetime.now().isoformat()
                    })
                    save_json("revisi.json", data)
                    st.success("✅ Revisi artikel tersimpan!")
                    st.balloons()
                else:
                    st.warning("Judul artikel wajib diisi.")

    with tab2:
        data = load_json("revisi.json")
        if data:
            status_colors = {
                "Accepted": "#27ae60", "Published": "#2980b9",
                "Revisi Mayor": "#e74c3c", "Revisi Minor": "#f39c12",
                "Menunggu Reviewer": "#8e44ad", "Draf": "#95a5a6"
            }
            for i, d in enumerate(reversed(data)):
                color = status_colors.get(d.get("status_rev",""), "#888")
                with st.expander(f"📄 {d.get('judul_artikel','?')} · {d.get('versi','')} · {d.get('tanggal_rev','')}"):
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write(f"**Jurnal:** {d.get('jurnal','-')}")
                        st.write(f"**Reviewer:** {d.get('reviewer','-')}")
                    with c2:
                        st.markdown(f"**Status:** <span style='color:{color};font-weight:700'>{d.get('status_rev','-')}</span>", unsafe_allow_html=True)
                        st.write(f"**Versi:** {d.get('versi','-')}")
                    if d.get("catatan_rev"):
                        st.write(f"**Catatan Reviewer:** {d.get('catatan_rev')}")
                    if d.get("perubahan"):
                        st.write(f"**Perubahan:** {d.get('perubahan')}")
                    if st.button("🗑️ Hapus", key=f"del_r_{i}"):
                        idx = data.index(d)
                        data.pop(idx)
                        save_json("revisi.json", data)
                        st.rerun()
        else:
            st.info("Belum ada riwayat revisi.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: LOG HARIAN
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📓  Log Harian":
    st.markdown("<div class='section-header'>📓 Log Harian Ibu Dewi</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background:linear-gradient(135deg,#fce8ef,#f5ecd7); border-radius:14px; 
                padding:18px 22px; margin-bottom:20px; border:1px dashed #c9507a'>
        🌸 <b>Catatan Kecil dari Gita:</b> Log ini adalah tempat Ibu merekam setiap langkah perjalanan akademis 
        Ibu — besar maupun kecil. Setiap pencapaian layak untuk dikenang. 
        <i>"JANGAN PERNAH MARDANDI BU, TETAP JADI BERKAT DAN DIBERKATI."</i> 💗
    </div>
    """, unsafe_allow_html=True)

    with st.expander("➕ Tambah Catatan Log", expanded=True):
        with st.form("form_log", clear_on_submit=True):
            col1, col2 = st.columns([2, 1])
            with col1:
                catatan = st.text_area("📝 Catatan / Aktivitas Hari Ini", height=100,
                                       placeholder="Apa yang Ibu kerjakan hari ini?")
            with col2:
                tanggal_log = st.date_input("📅 Tanggal")
                kategori_log = st.selectbox("🏷️ Kategori", [
                    "Penelitian", "Menulis", "Bimbingan", "Seminar",
                    "Administrasi", "Rapat", "Lainnya"
                ])
                mood = st.select_slider("😊 Mood", ["😔","😐","🙂","😊","🥰"], value="🙂")

            if st.form_submit_button("📌 Catat Log", use_container_width=True):
                if catatan:
                    data = load_json("log.json")
                    data.append({
                        "id": len(data)+1,
                        "catatan": catatan,
                        "tanggal": str(tanggal_log),
                        "kategori": kategori_log,
                        "mood": mood,
                        "dibuat": datetime.datetime.now().isoformat()
                    })
                    save_json("log.json", data)
                    st.success("✅ Log tersimpan! Terus semangat, Ibu! 💪")
                else:
                    st.warning("Catatan tidak boleh kosong.")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    data = load_json("log.json")
    if data:
        col_s, col_f = st.columns([3, 1])
        with col_s:
            search_log = st.text_input("🔍 Cari log...", key="sl")
        with col_f:
            filter_log = st.selectbox("Kategori", ["Semua","Penelitian","Menulis","Bimbingan","Seminar","Administrasi","Rapat","Lainnya"], key="fl")

        filtered = [d for d in data if
                    (search_log.lower() in d.get("catatan","").lower() or not search_log)
                    and (filter_log == "Semua" or d.get("kategori") == filter_log)]

        st.markdown(f"**{len(filtered)} entri log**")
        for i, d in enumerate(reversed(filtered)):
            kat_colors = {
                "Penelitian": "#1a2744", "Menulis": "#c9507a",
                "Bimbingan": "#b8935a", "Seminar": "#27ae60",
                "Administrasi": "#8e44ad", "Rapat": "#2980b9", "Lainnya": "#888"
            }
            color = kat_colors.get(d.get("kategori",""), "#888")
            st.markdown(f"""
            <div class="log-item" style="border-left-color:{color}">
                <div class="log-date">
                    📅 {d.get('tanggal','')} &nbsp;·&nbsp; 
                    <span style='color:{color};font-weight:700'>{d.get('kategori','-')}</span>
                    &nbsp;·&nbsp; {d.get('mood','🙂')}
                </div>
                <div class="log-content">{d.get('catatan','')}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🗑️", key=f"del_l_{i}", help="Hapus log ini"):
                idx = data.index(d)
                data.pop(idx)
                save_json("log.json", data)
                st.rerun()
    else:
        st.info("Belum ada log. Catat aktivitas disini boleh bu! ✍️")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: ARSIP TUGAS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🗂️  Arsip Tugas":
    st.markdown("<div class='section-header'>🗂️ Arsip Tugas & Pekerjaan</div>", unsafe_allow_html=True)

    quote, author = get_motivation()
    st.markdown(f"""
    <div class="motivation-box">
        <div class="motivation-quote">"{quote}"</div>
        <div class="motivation-author">— {author}</div>
    </div>""", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📥 Tambah Tugas", "📋 Semua Tugas"])

    with tab1:
        with st.form("form_tugas", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                nama_tugas  = st.text_input("📌 Nama Tugas")
                jenis       = st.selectbox("🏷️ Jenis", [
                    "Mengajar", "Bimbingan Mahasiswa", "Penilaian",
                    "Administrasi", "Penelitian", "Pengabdian Masyarakat",
                    "Publikasi", "Lainnya"
                ])
                deadline    = st.date_input("⏰ Deadline")
            with col2:
                prioritas   = st.selectbox("🔥 Prioritas", ["Tinggi", "Sedang", "Rendah"])
                status_t    = st.selectbox("📊 Status", ["Belum Mulai", "Sedang Dikerjakan", "Selesai", "Ditunda"])
                poin        = st.number_input("⭐ Poin Beban SKS / Kredit", 0, 10, 0)
            deskripsi_t = st.text_area("📝 Deskripsi Tugas")
            hasil_t     = st.text_area("✅ Hasil / Output")

            if st.form_submit_button("💾 Simpan Tugas", use_container_width=True):
                if nama_tugas:
                    data = load_json("tugas.json")
                    data.append({
                        "id": len(data)+1,
                        "nama_tugas": nama_tugas, "jenis": jenis,
                        "deadline": str(deadline), "prioritas": prioritas,
                        "status_t": status_t, "poin": poin,
                        "deskripsi_t": deskripsi_t, "hasil_t": hasil_t,
                        "dibuat": datetime.datetime.now().isoformat()
                    })
                    save_json("tugas.json", data)
                    st.success("✅ Tugas tersimpan!")
                    st.balloons()
                else:
                    st.warning("Nama tuga wajib isi, biar bisa simpan berkas ibu.")

    with tab2:
        data = load_json("tugas.json")
        if data:
            # Summary
            total = len(data)
            selesai = sum(1 for d in data if d.get("status_t") == "Selesai")
            proses  = sum(1 for d in data if d.get("status_t") == "Sedang Dikerjakan")
            belum   = sum(1 for d in data if d.get("status_t") == "Belum Mulai")

            c1, c2, c3, c4 = st.columns(4)
            for col, label, val, col_css in [
                (c1, "Total Tugas", total, "#1a2744"),
                (c2, "Selesai", selesai, "#27ae60"),
                (c3, "Dikerjakan", proses, "#f39c12"),
                (c4, "Belum Mulai", belum, "#e74c3c"),
            ]:
                with col:
                    st.markdown(f"""<div class="stat-box" style="background:{col_css}">
                        <div class="stat-number">{val}</div>
                        <div class="stat-label">{label}</div></div>""", unsafe_allow_html=True)

            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

            filter_s = st.selectbox("Filter Status", ["Semua","Belum Mulai","Sedang Dikerjakan","Selesai","Ditunda"])
            filtered = [d for d in data if filter_s == "Semua" or d.get("status_t") == filter_s]

            for i, d in enumerate(sorted(filtered, key=lambda x: x.get("deadline",""), reverse=False)):
                pr_colors = {"Tinggi": "#e74c3c", "Sedang": "#f39c12", "Rendah": "#27ae60"}
                st_colors = {"Selesai": "#27ae60", "Sedang Dikerjakan": "#f39c12",
                             "Belum Mulai": "#e74c3c", "Ditunda": "#95a5a6"}
                pr_c = pr_colors.get(d.get("prioritas",""), "#888")
                st_c = st_colors.get(d.get("status_t",""), "#888")

                with st.expander(f"📌 {d.get('nama_tugas','?')} · Deadline: {d.get('deadline','')}"):
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write(f"**Jenis:** {d.get('jenis','-')}")
                        st.markdown(f"**Prioritas:** <span style='color:{pr_c};font-weight:700'>{d.get('prioritas','-')}</span>", unsafe_allow_html=True)
                    with c2:
                        st.markdown(f"**Status:** <span style='color:{st_c};font-weight:700'>{d.get('status_t','-')}</span>", unsafe_allow_html=True)
                        st.write(f"**Poin SKS:** {d.get('poin',0)}")
                    if d.get("deskripsi_t"):
                        st.write(f"**Deskripsi:** {d.get('deskripsi_t')}")
                    if d.get("hasil_t"):
                        st.write(f"**Hasil:** {d.get('hasil_t')}")
                    if st.button("🗑️ Hapus", key=f"del_t_{i}"):
                        idx = data.index(d)
                        data.pop(idx)
                        save_json("tugas.json", data)
                        st.rerun()
        else:
            st.info("ibu kalo capek tidur, kalo ad tugas kann ada gita! 🎯")

# ─── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    💗 Jangan biarkan orang menjatuhkan ibu karena awak ga terima y bu <b>Gita Oktaviani Sitorus</b><br>
    untuk <b>Ibu Dewi Pika Lumbanbatu, S.H., M.H</b> — semoga karya Ibu selalu jadi berkat ✨
</div>
""", unsafe_allow_html=True)
