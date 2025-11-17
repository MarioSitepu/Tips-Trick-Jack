# AI Daily Summary Generator

Proyek ini menghasilkan ringkasan harian secara otomatis dengan AI yang dijalankan di server lokal. GitHub Actions hanya meng-commit perubahan setiap 30 menit.

## 🎯 Keunggulan

- ✅ **Aman dari limit GitHub Actions** - Workflow hanya commit, tidak menjalankan AI
- ✅ **Tidak ada commit spam** - Hanya commit jika ada perubahan
- ✅ **AI dapat berjalan terus-menerus** - Tanpa batas karena jalan di server sendiri
- ✅ **Hanya perubahan yang benar-benar di-commit** - Batch commit setiap 30 menit
- ✅ **Rate limit aman** - Maksimal 48 commit per hari (sangat aman)
- ✅ **AI-Powered HTML/CSS Generation** - Generate HTML/CSS unik dengan AI (OpenAI, Ollama, dll)

## 🚀 Cara Kerja

1. **AI Worker** (jalan di server/laptop):
   - Generate proyek HTML/CSS setiap 30 menit
   - Membuat folder baru dengan nama berdasarkan tanggal (format: `YYYY-MM-DD-HH-MM`)
   - Setiap folder berisi `index.html` dan `style.css`
   - Menyimpan tracking ke `data/daily_summary.md`
   - Tidak langsung commit/push

2. **GitHub Actions** (jalan di GitHub):
   - Run setiap 30 menit
   - Cek apakah ada perubahan di folder `data/` atau `projects/`
   - Jika ada folder/proyek baru → commit sekali
   - Jika tidak berubah → skip (100% aman)

3. **GitHub Repo**:
   - Commit rapi dan terorganisir
   - History bersih dan jelas
   - Tidak kena limit

## 📁 Struktur Proyek

```
ai-daily-project/
│
├─ ai_worker/             ← Script AI di server/laptop
│   ├─ generate.py        ← Console version
│   └─ generate_gui.py    ← GUI version (system tray)
│
├─ data/
│   └─ daily_summary.md   ← hasil generate AI (tracking)
│
├─ projects/              ← Folder proyek HTML/CSS
│   └─ YYYY-MM-DD-HH-MM/  ← Folder per generate (berdasarkan tanggal)
│       ├─ index.html     ← File HTML
│       └─ style.css      ← File CSS
│
├─ .github/
│   └─ workflows/
│       └─ auto-commit.yml
│
├─ requirements.txt
└─ README.md
```

## 💻 Versi EXE (Windows Background App)

**NEW!** Sekarang tersedia versi EXE yang berjalan di background dengan system tray!

### Quick Start EXE Version:

1. **Build EXE:**
   ```bash
   # Windows: Double-click build.bat
   # atau jalankan:
   python build_exe.py
   ```

2. **Jalankan:**
   - Double-click `dist/AI-Daily-Summary.exe`
   - Icon akan muncul di system tray (dekat jam)
   - Right-click icon untuk akses menu

3. **Fitur:**
   - ✅ Berjalan di background (tidak mengganggu)
   - ✅ System tray icon untuk kontrol
   - ✅ Status window untuk monitoring
   - ✅ Start/Stop worker dari tray menu
   - ✅ Auto-generate summary setiap 30 menit

📖 **Panduan lengkap:** 
- [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md) - Panduan build EXE
- [EXE_SETUP.md](EXE_SETUP.md) - **Setup EXE dengan Gemini API** ⭐

---

## 🔧 Setup

### 1. Setup AI Worker (Server/Laptop)

**Opsi A: Console Version (Original)**

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan AI worker (console version)
cd ai_worker
python generate.py
```

**Opsi B: GUI Version (System Tray)**
```bash
# Install dependencies (sudah include GUI deps)
pip install -r requirements.txt

# Jalankan GUI version
cd ai_worker
python generate_gui.py
```

AI worker akan:
- Generate proyek HTML/CSS setiap 30 menit
- Membuat folder baru di `projects/` dengan nama berdasarkan tanggal
- Setiap folder berisi `index.html` dan `style.css` (proyek lengkap)
- Menyimpan tracking ke `data/daily_summary.md`
- **Console version:** Berjalan terus sampai dihentikan (Ctrl+C)
- **GUI version:** Berjalan di background dengan system tray icon

### 2. Setup GitHub Actions

GitHub Actions sudah dikonfigurasi di `.github/workflows/auto-commit.yml`.

**Setup Token:**

**Opsi A: GITHUB_TOKEN (Default - Paling Mudah)** ⭐
- ✅ Tidak perlu setup manual
- ✅ Otomatis tersedia
- ✅ Cukup untuk branch yang tidak protected

**Opsi B: Fine-grained Personal Access Token**
- Diperlukan jika branch default adalah **protected branch**
- Buat PAT di: https://github.com/settings/tokens
- Tambahkan ke Repository Secrets sebagai `GITHUB_TOKEN_PAT`

📖 **Panduan lengkap:** Lihat [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md)

**Setelah setup, workflow akan:**
- Otomatis run setiap 30 menit
- Commit jika ada perubahan
- Skip jika tidak ada perubahan

### 3. Setup AI untuk Generate HTML/CSS (Optional)

**NEW!** Sekarang bisa menggunakan AI untuk generate HTML/CSS secara dinamis!

**Quick Setup:**

1. **Install AI Provider:**
   ```bash
   # Untuk Gemini 2.5 Flash (Default - Recommended & Gratis!)
   pip install google-generativeai
   export GEMINI_API_KEY=your-api-key
   
   # Atau untuk OpenAI
   pip install openai
   export OPENAI_API_KEY=your-api-key
   
   # Atau untuk Ollama (Gratis, Lokal)
   pip install ollama
   ollama pull llama3.2
   ```

2. **Enable AI:**
   Edit `ai_worker/generate.py`:
   ```python
   USE_AI = True
   AI_PROVIDER = "gemini"  # Default, atau "openai", "ollama", "anthropic", "auto"
   ```

3. **Customize:**
   ```python
   THEME = "modern"  # "modern", "classic", "minimal", "dark", dll
   STYLE = "gradient"  # "gradient", "solid", "glassmorphism", dll
   ```

📖 **Panduan lengkap:** 
- [AI_SETUP.md](AI_SETUP.md) - Setup AI providers
- [GEMINI_SETUP.md](GEMINI_SETUP.md) - **Panduan lengkap setup Gemini API Key** ⭐

### 4. Kustomisasi AI Worker

Edit `ai_worker/generate.py` untuk:
- Enable/disable AI generation
- Mengganti AI provider (OpenAI, Ollama, Anthropic)
- Mengubah theme dan style
- Menyesuaikan interval waktu

## ⚙️ Konfigurasi

### Mengubah Interval Waktu

**AI Worker:**
```python
time.sleep(1800)  # 30 menit = 1800 detik
```

**GitHub Actions:**
```yaml
schedule:
  - cron: "*/30 * * * *"   # 30 menit
```

Format cron: `menit jam hari bulan hari-minggu`

### Mengubah Folder Output

Edit di `ai_worker/generate.py`:
```python
file_path = "../data/daily_summary.md"  # Ganti path sesuai kebutuhan
```

Edit di `.github/workflows/auto-commit.yml`:
```yaml
git add data/  # Ganti folder sesuai kebutuhan
```

## 🛡️ Keamanan & Limit

### Kenapa Sistem Ini Aman?

1. **GitHub Actions Limit:**
   - Workflow hanya 1-3 menit per run
   - Maksimal 48 commit/hari (sangat aman)
   - Tidak menjalankan AI berat di Actions

2. **Commit Strategy:**
   - Batch commit (1 kali per run)
   - Hanya commit jika ada perubahan
   - Tidak commit ribuan file

3. **AI Execution:**
   - AI jalan di server sendiri
   - Tidak terbatas oleh GitHub Actions
   - Bisa jalan 24/7 tanpa masalah

## 📊 Monitoring

Untuk melihat status:
- **AI Worker:** Cek console output
- **GitHub Actions:** Cek tab "Actions" di GitHub
- **Commits:** Cek commit history di GitHub

## 🔥 Variasi Proyek

Template ini bisa dikembangkan untuk:

- 🖼️ **AI Image Generator** - Generate gambar setiap X menit
- 💻 **AI Code Generator** - Generate code snippets
- 📊 **AI Dataset Generator** - Generate dataset training
- 🎓 **AI Model Trainer** - Auto train model dengan data baru

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

**Made with ❤️ for safe AI automation on GitHub**

