# ⚡ Quick Start Guide

Panduan cepat untuk menjalankan AI Daily Summary Generator.

## 🎯 Pilih Metode

### 1️⃣ EXE Version (Paling Mudah - Windows)

**Untuk pengguna yang ingin aplikasi berjalan di background tanpa terminal:**

```bash
# Step 1: Build EXE
build.bat

# Step 2: Jalankan
# Double-click dist/AI-Daily-Summary.exe
# Icon akan muncul di system tray
```

✅ **Keuntungan:**
- Tidak perlu buka terminal
- Berjalan di background
- Mudah diakses via system tray
- Bisa auto-start dengan Windows

---

### 2️⃣ GUI Version (Python)

**Untuk pengguna yang ingin test sebelum build EXE:**

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan
python ai_worker/generate_gui.py
```

✅ **Keuntungan:**
- Mudah di-test
- System tray icon
- Status window

---

### 3️⃣ Console Version (Original)

**Untuk pengguna yang suka terminal/command line:**

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan
python ai_worker/generate.py
```

✅ **Keuntungan:**
- Simple dan ringan
- Cocok untuk server/headless
- Log langsung di terminal

---

## 📋 Checklist Setup

- [ ] Python 3.8+ terinstall (untuk versi Python)
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Folder `data/` ada (akan dibuat otomatis)
- [ ] GitHub Actions sudah dikonfigurasi (untuk auto-commit)

## 🚀 Langkah Selanjutnya

1. **Kustomisasi AI Model:**
   - Edit `ai_worker/generate_gui.py` atau `generate.py`
   - Ganti fungsi `generate_summary()` dengan model AI Anda
   - Lihat `ai_worker/example_integrations.py` untuk contoh

2. **Setup GitHub Actions:**
   - Push ke GitHub
   - Actions akan otomatis aktif
   - Commit setiap 30 menit jika ada perubahan

3. **Auto-Start (Opsional):**
   - Copy EXE ke Windows Startup folder
   - Aplikasi akan jalan otomatis saat boot

---

## ❓ Troubleshooting

**Q: EXE tidak muncul di system tray?**
- Cek hidden icons (klik arrow ^ di system tray)
- Restart aplikasi

**Q: File tidak terbuat?**
- Pastikan folder `data/` ada di directory yang sama dengan EXE
- Cek permission write

**Q: Build error?**
- Pastikan Python terinstall
- Install dependencies: `pip install -r requirements.txt`
- Lihat [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md)

---

**Selamat menggunakan! 🎉**

