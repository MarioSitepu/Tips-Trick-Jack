# 🔧 Troubleshooting: Git Commit & Push ke Repository

Panduan untuk mengatasi masalah commit dan push ke repository showcase.

## 🔍 Checklist Troubleshooting

### 1. Cek Apakah Project-Showcase adalah Git Repository

Jalankan script:
```batch
check_git_status.bat
```

Atau manual:
```bash
cd ..\Project-Showcase
git status
```

**Jika bukan git repo:**
```bash
cd ..\Project-Showcase
git init
git remote add origin https://github.com/MarioSitepu/Jack-s-Cards.git
git branch -M main
```

---

### 2. Cek GitHub Token

**Cek environment variable:**
```powershell
# PowerShell
echo $env:GITHUBTOKENPAT
echo $env:GITHUB_TOKEN_PAT
echo $env:GITHUB_TOKEN
```

**Jika tidak ada, set token:**
```powershell
$env:GITHUBTOKENPAT="your-token-here"
```

**Atau set permanent:**
1. `Win + R` → `sysdm.cpl`
2. Environment Variables → New
3. Name: `GITHUBTOKENPAT`
4. Value: `your-token-here`

---

### 3. Cek Path Showcase Repository

**Default path:** `../Project-Showcase` (sama level dengan AiCommitBot)

**Struktur yang benar:**
```
JacksPlayCards/
├── AiCommitBot/
│   └── ai_worker/
│       └── generate.py
└── Project-Showcase/  ← Harus ada di sini
    ├── .git/          ← Harus ada (git repo)
    ├── projects/
    └── ...
```

**Jika path berbeda, set environment variable:**
```powershell
$env:SHOWCASE_REPO_PATH="C:\path\to\Project-Showcase"
```

---

### 4. Cek Remote Repository

```bash
cd ..\Project-Showcase
git remote -v
```

**Harus menampilkan:**
```
origin  https://github.com/MarioSitepu/Jack-s-Cards.git (fetch)
origin  https://github.com/MarioSitepu/Jack-s-Cards.git (push)
```

**Jika tidak ada remote:**
```bash
git remote add origin https://github.com/MarioSitepu/Jack-s-Cards.git
```

---

### 5. Cek Branch

```bash
cd ..\Project-Showcase
git branch --show-current
```

**Default:** `main`

**Jika berbeda, set environment variable:**
```powershell
$env:SHOWCASE_BRANCH="master"  # atau branch lain
```

---

### 6. Cek File yang Akan Di-commit

```bash
cd ..\Project-Showcase
git status
```

**Harus ada file baru di:**
- `projects/YYYY-MM-DD-HH-MM/index.html`
- `projects/YYYY-MM-DD-HH-MM/style.css`
- `index.html` (gallery index)

---

## 🐛 Masalah Umum & Solusi

### Problem 1: "Showcase path is not a git repository"

**Solusi:**
```bash
cd ..\Project-Showcase
git init
git remote add origin https://github.com/MarioSitepu/Jack-s-Cards.git
```

---

### Problem 2: "Push failed: Authentication failed"

**Penyebab:** GitHub token tidak terdeteksi atau invalid

**Solusi:**
1. Cek token di environment variable
2. Pastikan token memiliki permission "Contents: Read and write"
3. Regenerate token jika perlu
4. Update environment variable dengan token baru

---

### Problem 3: "No changes to commit"

**Penyebab:** File sudah di-commit sebelumnya

**Solusi:**
- Ini normal jika file sudah di-commit
- Cek dengan: `git log --oneline` untuk melihat commit history

---

### Problem 4: "Push failed: Permission denied"

**Penyebab:** Token tidak memiliki permission atau branch protected

**Solusi:**
1. Pastikan token memiliki permission "Contents: Read and write"
2. Jika branch protected, pastikan token memiliki permission untuk push ke protected branch
3. Atau disable branch protection sementara untuk testing

---

### Problem 5: "Remote URL tidak ter-update dengan token"

**Penyebab:** Remote URL sudah memiliki credentials atau format berbeda

**Solusi:**
```bash
cd ..\Project-Showcase
git remote set-url origin https://x-access-token:YOUR_TOKEN@github.com/MarioSitepu/Jack-s-Cards.git
```

---

## 📊 Debug Mode

Untuk melihat detail proses commit/push, jalankan aplikasi dan lihat output console. Sekarang akan menampilkan:

- ✅ Showcase repo path
- ✅ Git status
- ✅ Commit message
- ✅ Remote URL
- ✅ Push result
- ❌ Error details (jika ada)

---

## ✅ Verifikasi Setelah Fix

1. **Jalankan aplikasi** (EXE atau Python script)
2. **Generate project baru**
3. **Cek output console** untuk melihat proses commit/push
4. **Cek GitHub repository:**
   - Buka: https://github.com/MarioSitepu/Jack-s-Cards
   - Tab "Commits" → Harus ada commit baru
   - Tab "Code" → Folder `projects/` harus ada project baru

---

## 🔍 Script Bantuan

### check_git_status.bat
Script untuk cek status git di Project-Showcase:
- Cek apakah ini git repo
- Cek remote URL
- Cek status file
- Cek last commit
- Cek current branch

**Jalankan:**
```batch
check_git_status.bat
```

---

## 📝 Logging yang Diperbaiki

Sekarang aplikasi akan menampilkan:
- ✅ Path showcase repo
- ✅ Git status sebelum commit
- ✅ Commit message
- ✅ Remote URL (dengan token jika ada)
- ✅ Push result (success atau error dengan detail)
- ❌ Error details lengkap jika gagal

Semua informasi ini akan muncul di:
- Console output (jika run dari Python)
- System tray status window (jika run dari EXE)

---

**Jika masih ada masalah, cek output console untuk detail error yang lebih lengkap!**

