# 🚀 Setup Auto-Push ke GitHub

Panduan lengkap untuk enable auto-push ke GitHub dari EXE/Python script.

## 🎯 Fitur Auto-Push

Dengan auto-push enabled:
- ✅ EXE akan otomatis commit & push setelah generate file
- ✅ Tidak perlu push manual
- ✅ File langsung muncul di GitHub
- ✅ GitHub Actions tetap berjalan sebagai backup

---

## ⚙️ Setup Auto-Push

### Step 1: Install Git ⚠️ WAJIB

**Git belum terinstall?** Lihat panduan lengkap: [INSTALL_GIT.md](INSTALL_GIT.md)

**Quick Install:**
- Download dari: https://git-scm.com/download/win
- Install dengan default settings
- **PENTING:** Pastikan "Add Git to PATH" dicentang ✅
- Restart PowerShell setelah install

**Verifikasi:**
```powershell
git --version
```

Jika muncul error "git is not recognized", lihat [INSTALL_GIT.md](INSTALL_GIT.md) untuk troubleshooting.

---

### Step 2: Setup GitHub Token

**Buat Fine-grained Personal Access Token:**

1. Buka: https://github.com/settings/tokens
2. Klik "Fine-grained tokens" → "Generate new token"
3. Set permissions:
   - ✅ **Contents:** Read and write
   - ✅ **Metadata:** Read-only
4. Select repository Anda
5. Copy token (format: `github_pat_...`)

---

### Step 3: Set Environment Variable

**Windows (Command Prompt):**
```cmd
set GITHUB_TOKEN_PAT=your-token-here
```

**Windows (PowerShell):**
```powershell
$env:GITHUB_TOKEN_PAT="your-token-here"
```

**Windows (Permanent):**
1. `Win + R` → `sysdm.cpl` → Enter
2. Tab "Advanced" → "Environment Variables"
3. New → Name: `GITHUB_TOKEN_PAT`, Value: `your-token-here`
4. OK → OK

---

### Step 4: Enable Auto-Push

**Opsi A: Edit Code (generate.py)**

Edit `ai_worker/generate.py`:
```python
AUTO_PUSH = True  # Enable auto-push
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") or os.getenv("GITHUB_TOKEN_PAT")
```

**Opsi B: Environment Variable (generate_gui.py)**

Set environment variable:
```powershell
$env:AUTO_PUSH="true"
$env:GITHUB_TOKEN_PAT="your-token-here"
```

**Opsi C: Saat Inisialisasi (generate_gui.py)**

Edit `ai_worker/generate_gui.py`, di fungsi `main()`:
```python
app = SystemTrayApp(auto_push=True, github_token="your-token-here")
```

---

## 🚀 Cara Menggunakan

### Console Version:

```bash
# Edit generate.py: AUTO_PUSH = True
python ai_worker/generate.py
```

### GUI Version:

```bash
# Set environment variable
$env:AUTO_PUSH="true"
$env:GITHUB_TOKEN_PAT="your-token-here"

# Run
python ai_worker/generate_gui.py
```

### EXE Version:

1. Set environment variable (permanent):
   - `AUTO_PUSH=true`
   - `GITHUB_TOKEN_PAT=your-token-here`

2. Run EXE:
   ```bash
   AI-Daily-Summary.exe
   ```

---

## ✅ Verifikasi

Setelah generate file, cek:
1. Console/Status window: `✅ Pushed to GitHub: Successfully pushed to main`
2. GitHub repository: File baru muncul di `projects/`
3. Commit history: Ada commit dari "AI-Bot"

---

## 🐛 Troubleshooting

### Error: "Git not found"

**Solusi:**
- Install Git: https://git-scm.com/download/win
- Pastikan Git ada di PATH
- Restart terminal/EXE

### Error: "Not a git repository"

**Solusi:**
- Pastikan EXE dijalankan di folder repository
- Atau clone repository dulu:
  ```bash
  git clone https://github.com/username/repo.git
  cd repo
  AI-Daily-Summary.exe
  ```

### Error: "Push failed: authentication failed"

**Solusi:**
- Pastikan `GITHUB_TOKEN_PAT` sudah di-set
- Pastikan token memiliki permission "Contents: Read and write"
- Regenerate token jika perlu

### Error: "No remote 'origin' found"

**Solusi:**
- Pastikan repository sudah di-clone dari GitHub
- Atau tambahkan remote:
  ```bash
  git remote add origin https://github.com/username/repo.git
  ```

---

## 📋 Checklist Setup

- [ ] Git terinstall (`git --version`)
- [ ] Repository sudah di-clone
- [ ] Fine-grained PAT sudah dibuat
- [ ] Environment variable `GITHUB_TOKEN_PAT` sudah di-set
- [ ] `AUTO_PUSH = True` di code (atau via env var)
- [ ] Test generate file
- [ ] Verifikasi push berhasil

---

## 🔄 Alur Kerja dengan Auto-Push

```
1. EXE generate file
   └─> projects/2025-11-17-21-00/index.html
   └─> projects/2025-11-17-21-00/style.css

2. Auto commit & push
   └─> git add data/ projects/
   └─> git commit -m "🤖 AI update: New project..."
   └─> git push origin main

3. File langsung muncul di GitHub! ✅

4. GitHub Actions (backup)
   └─> Monitor perubahan
   └─> Jika ada perubahan → commit & push
   └─> Jika tidak ada → skip
```

---

## 💡 Tips

1. **Untuk Development:**
   - Set `AUTO_PUSH = False` untuk test tanpa push
   - Set `AUTO_PUSH = True` untuk production

2. **Untuk EXE:**
   - Set environment variable permanent
   - Atau edit code sebelum build

3. **Security:**
   - Jangan commit token ke repository
   - Gunakan environment variable
   - Regenerate token secara berkala

---

**Selamat! Sekarang EXE bisa auto push ke GitHub! 🎉**

