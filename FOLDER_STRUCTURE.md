# 📁 Struktur Folder - Generator & Showcase Terpisah

Dokumen ini menjelaskan struktur folder setelah pemisahan menjadi 2 folder terpisah.

## 🏗️ Struktur Folder

```
Documents/
├─ Belajar/
│   ├─ AiCommitBot/          ← Folder 1: Generator (Commit Push Bot)
│   │   ├─ ai_worker/
│   │   │   ├─ generate.py
│   │   │   ├─ generate_gui.py
│   │   │   ├─ git_helper.py
│   │   │   └─ showcase_helper.py
│   │   ├─ data/
│   │   │   └─ daily_summary.md
│   │   ├─ projects/         ← Projects lokal (opsional, untuk backup)
│   │   ├─ .github/
│   │   ├─ README.md
│   │   └─ requirements.txt
│   │
│   └─ ai-showcase/          ← Folder 2: Showcase Website
│       ├─ index.html        ← Gallery website (auto-generated)
│       ├─ projects/         ← Semua project untuk showcase
│       │   ├─ 2025-01-17-14-30/
│       │   │   ├─ index.html
│       │   │   └─ style.css
│       │   └─ ...
│       ├─ README.md
│       └─ .gitignore
```

## 📋 Penjelasan

### Folder 1: `AiCommitBot/` (Generator)

**Fungsi:**
- Mesin generator AI
- Source code aplikasi
- Configuration & setup
- Generate projects ke folder lokal `projects/`

**Isi:**
- `ai_worker/` - Source code generator
- `data/` - Tracking data
- `projects/` - Projects lokal (opsional, bisa di-commit atau tidak)
- `.github/` - GitHub Actions workflows
- Dokumentasi & setup files

**Repo GitHub:**
- Bisa di-push ke repo: `ai-commit-bot` (atau nama lain)
- Berisi source code generator

### Folder 2: `ai-showcase/` (Showcase Website)

**Fungsi:**
- Website gallery untuk showcase projects
- Hanya berisi projects + gallery
- Siap untuk deploy ke GitHub Pages

**Isi:**
- `index.html` - Gallery website (auto-generated)
- `projects/` - Semua project HTML/CSS
- `README.md` - Dokumentasi showcase

**Repo GitHub:**
- Di-push ke repo: `ai-showcase` (atau nama lain)
- Hanya berisi projects + gallery (tidak ada source code)

## 🔄 Alur Kerja

```
1. Generator (AiCommitBot/)
   └─> Generate project baru
   └─> Simpan ke projects/ (lokal, opsional)

2. Copy ke Showcase (ai-showcase/)
   └─> Copy project ke ../ai-showcase/projects/
   └─> Generate gallery index.html
   └─> Commit & push ke GitHub showcase repo

3. GitHub Pages
   └─> Auto-deploy dari showcase repo
   └─> Website tersedia di: username.github.io/ai-showcase/
```

## ⚙️ Konfigurasi

### Default Path:

```python
# ai_worker/generate.py
SHOWCASE_REPO_PATH = "../ai-showcase"  # Relative path dari AiCommitBot/
```

**Struktur:**
```
AiCommitBot/          ← Current directory
└─ ai_worker/
    └─ generate.py    ← Script ini
../ai-showcase/       ← Parent directory, lalu masuk ai-showcase/
```

### Custom Path:

Jika ingin path berbeda, set environment variable:

```bash
# Windows PowerShell
$env:SHOWCASE_REPO_PATH = "C:/Users/YourName/Documents/Belajar/ai-showcase"

# Linux/Mac
export SHOWCASE_REPO_PATH="/path/to/ai-showcase"
```

## 🚀 Setup

### Step 1: Folder Sudah Dibuat

Folder `ai-showcase/` sudah dibuat di parent directory (sama level dengan `AiCommitBot/`).

### Step 2: Initialize Git di Showcase (Opsional)

Jika ingin push ke GitHub:

```bash
cd ../ai-showcase
git init
git remote add origin https://github.com/username/ai-showcase.git
```

### Step 3: Konfigurasi Generator

Edit `ai_worker/generate.py`:

```python
PUSH_TO_SHOWCASE = True
SHOWCASE_REPO_URL = "https://github.com/username/ai-showcase.git"
```

Atau set environment variable:

```bash
$env:PUSH_TO_SHOWCASE = "true"
$env:SHOWCASE_REPO_URL = "https://github.com/username/ai-showcase.git"
```

### Step 4: Jalankan Generator

```bash
cd AiCommitBot
python ai_worker/generate.py
```

Projects akan otomatis:
- Ter-copy ke `../ai-showcase/projects/`
- Gallery ter-generate di `../ai-showcase/index.html`
- Ter-push ke GitHub (jika enabled)

## 📝 Catatan Penting

1. **Path Relative:**
   - Default: `../ai-showcase` (sama level dengan `AiCommitBot/`)
   - Bisa diubah via environment variable

2. **Git Repo:**
   - Folder showcase bisa di-initialize sebagai git repo terpisah
   - Atau biarkan kosong, akan di-clone otomatis jika `SHOWCASE_REPO_URL` diset

3. **Projects Lokal:**
   - Projects di `AiCommitBot/projects/` tetap ada (untuk backup)
   - Projects di `ai-showcase/projects/` untuk showcase website

4. **Auto-Generate:**
   - Gallery `index.html` otomatis di-generate setiap ada project baru
   - Jangan edit manual, akan di-overwrite

## ✅ Checklist

- [x] Folder `ai-showcase/` sudah dibuat
- [x] README.md sudah dibuat di showcase
- [x] Konfigurasi default path sudah di-update
- [ ] (Opsional) Initialize git di showcase folder
- [ ] (Opsional) Set `PUSH_TO_SHOWCASE = True`
- [ ] (Opsional) Set `SHOWCASE_REPO_URL`
- [ ] Test generate project baru

---

**Struktur folder sudah siap! 🎉**

