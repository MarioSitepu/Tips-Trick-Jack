# 🎨 Setup Showcase Repo & Website Gallery

Panduan lengkap untuk setup repo showcase terpisah dan website gallery untuk menampilkan semua hasil generate AI.

> 💡 **Struktur Folder:** Generator dan showcase sudah dipisah menjadi 2 folder. Lihat [FOLDER_STRUCTURE.md](FOLDER_STRUCTURE.md) untuk detail struktur.

## 🎯 Konsep

Dengan fitur ini, setiap project yang di-generate akan:
1. ✅ Disimpan di repo utama (seperti biasa, opsional)
2. ✅ **OTOMATIS di-copy ke repo showcase terpisah**
3. ✅ **Website gallery otomatis di-generate** untuk menampilkan semua project
4. ✅ **Auto push ke repo showcase** (jika enabled)

## 📋 Keuntungan Repo Terpisah

- ✅ **Separation of Concerns** - Generator dan showcase terpisah
- ✅ **Repo showcase clean** - Hanya berisi projects + gallery (tidak ada source code)
- ✅ **GitHub Pages optimal** - Deploy lebih ringan & cepat
- ✅ **Portfolio ready** - Bisa share showcase tanpa expose source code
- ✅ **Professional** - Struktur lebih rapi dan terorganisir
- ✅ **History commit bersih** - Generator commits terpisah dari showcase commits
- ✅ **Website gallery otomatis** - Index.html otomatis di-generate dengan semua project
- ✅ **Auto-update** - Gallery otomatis update setiap ada project baru

---

## 🚀 Setup Showcase Repo

### Step 1: Folder Showcase Sudah Dibuat ✅

Folder `ai-showcase/` sudah dibuat di parent directory (sama level dengan `AiCommitBot/`).

**Struktur:**
```
Documents/Belajar/
├─ AiCommitBot/          ← Generator
└─ ai-showcase/          ← Showcase (sudah dibuat)
```

### Step 2: Repo Showcase di GitHub ✅

Repo showcase sudah dibuat di GitHub:
- **URL Repository:** `https://github.com/MarioSitepu/Jack-s-Cards`
- **HTTPS:** `https://github.com/MarioSitepu/Jack-s-Cards.git`
- **SSH:** `git@github.com:MarioSitepu/Jack-s-Cards.git`

3. **Initialize Git di folder showcase (opsional):**
   ```bash
   cd ../ai-showcase
   git init
   git remote add origin https://github.com/username/ai-showcase.git
   ```
   
   Atau biarkan kosong, akan di-clone otomatis jika `SHOWCASE_REPO_URL` diset.

### Step 3: Konfigurasi Environment Variables

**Opsi A: Via Environment Variables (Recommended)**

```bash
# Windows (PowerShell)
$env:PUSH_TO_SHOWCASE = "true"
$env:SHOWCASE_REPO_PATH = "../ai-showcase"  # Default: sama level dengan AiCommitBot/
$env:SHOWCASE_REPO_URL = "https://github.com/MarioSitepu/Jack-s-Cards.git"
$env:SHOWCASE_BRANCH = "main"
$env:GITHUB_TOKEN = "your-github-token"

# Windows (CMD)
set PUSH_TO_SHOWCASE=true
set SHOWCASE_REPO_PATH=../ai-showcase
set SHOWCASE_REPO_URL=https://github.com/MarioSitepu/Jack-s-Cards.git
set SHOWCASE_BRANCH=main
set GITHUB_TOKEN=your-github-token

# Linux/Mac
export PUSH_TO_SHOWCASE=true
export SHOWCASE_REPO_PATH=../ai-showcase
export SHOWCASE_REPO_URL=https://github.com/MarioSitepu/Jack-s-Cards.git
export SHOWCASE_BRANCH=main
export GITHUB_TOKEN=your-github-token
```

**Opsi B: Edit File `ai_worker/generate.py`**

```python
# Konfigurasi Showcase Repo
PUSH_TO_SHOWCASE = True  # Set True untuk push ke repo showcase terpisah
SHOWCASE_REPO_PATH = "../ai-showcase"  # Path ke folder showcase lokal (sama level dengan AiCommitBot)
SHOWCASE_REPO_URL = "https://github.com/MarioSitepu/Jack-s-Cards.git"  # URL repo showcase GitHub
SHOWCASE_BRANCH = "main"  # Branch untuk showcase repo
```

**Note:** Default path `../ai-showcase` berarti folder showcase ada di parent directory, sama level dengan folder `AiCommitBot/`.

**Opsi C: Edit File `ai_worker/generate_gui.py` (untuk GUI version)**

Sama seperti di atas, atau set via environment variables.

### Step 4: Setup GitHub Token

**Buat Personal Access Token (PAT):**

1. Buka: https://github.com/settings/tokens
2. Klik "Generate new token" → "Generate new token (classic)"
3. Beri nama: `AI-Showcase-Bot`
4. Pilih scope:
   - ✅ `repo` (Full control of private repositories)
5. Generate token dan **copy token** (hanya muncul sekali!)

**Set Token:**

```bash
# Windows (PowerShell)
$env:GITHUB_TOKEN = "ghp_your_token_here"

# Windows (CMD)
set GITHUB_TOKEN=ghp_your_token_here

# Linux/Mac
export GITHUB_TOKEN=ghp_your_token_here
```

Atau tambahkan ke file `.env` (jika menggunakan python-dotenv).

---

## 🎨 Cara Kerja

### Alur Otomatis:

```
1. AI Worker generate project baru
   └─> projects/2025-01-17-14-30/
       ├─ index.html
       └─ style.css

2. Copy ke Showcase Repo
   └─> ../ai-showcase/projects/2025-01-17-14-30/
       ├─ index.html
       └─ style.css

3. Generate Gallery Index
   └─> ../ai-showcase/index.html
       (Gallery dengan semua project)

4. Git Commit & Push
   └─> Push ke GitHub showcase repo
```

### Struktur Showcase Repo:

```
ai-showcase/
│
├─ index.html          ← Gallery website (auto-generated)
├─ projects/           ← Semua project
│   ├─ 2025-01-17-14-30/
│   │   ├─ index.html
│   │   └─ style.css
│   ├─ 2025-01-17-15-00/
│   │   ├─ index.html
│   │   └─ style.css
│   └─ ...
└─ README.md           ← (opsional)
```

---

## 🌐 Deploy ke GitHub Pages

Setelah repo showcase di-push ke GitHub, Anda bisa deploy ke GitHub Pages:

### Step 1: Enable GitHub Pages

1. Buka repository showcase di GitHub
2. Settings → Pages
3. Source: Deploy from a branch
4. Branch: `main` (atau branch yang digunakan)
5. Folder: `/ (root)`
6. Save

### Step 2: Akses Website

Website akan tersedia di:
- `https://mariositepu.github.io/Jack-s-Cards/`

**Note:** Butuh beberapa menit untuk pertama kali deploy.

---

## 🔧 Konfigurasi Lanjutan

### Mengubah Path Showcase Repo

```python
# Di generate.py atau via environment variable
SHOWCASE_REPO_PATH = "C:/Users/YourName/Documents/ai-showcase"  # Absolute path
# atau
SHOWCASE_REPO_PATH = "../ai-showcase"  # Relative path
```

### Clone Otomatis

Jika repo showcase belum ada di lokal, sistem akan otomatis clone dari `SHOWCASE_REPO_URL` (jika diset).

**Pastikan:**
- `SHOWCASE_REPO_URL` sudah diset
- `GITHUB_TOKEN` sudah diset (untuk clone private repo)

### Custom Branch

```python
SHOWCASE_BRANCH = "gh-pages"  # Untuk GitHub Pages
# atau
SHOWCASE_BRANCH = "main"
```

---

## 📝 Testing

### Test Manual:

1. **Enable showcase push:**
   ```python
   PUSH_TO_SHOWCASE = True
   ```

2. **Jalankan generate:**
   ```bash
   cd ai_worker
   python generate.py
   ```

3. **Cek hasil:**
   - Project ter-copy ke showcase repo?
   - Gallery index.html ter-generate?
   - Push ke GitHub berhasil?

### Test dengan GUI:

1. Set environment variables
2. Jalankan GUI:
   ```bash
   python ai_worker/generate_gui.py
   ```
3. Start worker dari system tray
4. Tunggu generate (atau trigger manual)
5. Cek showcase repo

---

## 🎨 Kustomisasi Gallery

Gallery index.html otomatis di-generate oleh `showcase_helper.py`. 

Untuk kustomisasi, edit fungsi `generate_gallery_index()` di:
- `ai_worker/showcase_helper.py`

**Contoh kustomisasi:**

```python
# Ganti warna background
background: linear-gradient(135deg, #your-color-1 0%, #your-color-2 100%);

# Ganti layout grid
grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));  # Lebih kecil
# atau
grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));  # Lebih besar
```

---

## ⚠️ Troubleshooting

### Error: "Showcase repo not found and no repo_url provided"

**Solusi:**
- Set `SHOWCASE_REPO_URL` di environment variable atau di code
- Atau clone repo showcase manual:
  ```bash
  git clone https://github.com/MarioSitepu/Jack-s-Cards.git ../ai-showcase
  ```

### Error: "Failed to clone showcase repo"

**Solusi:**
- Pastikan `GITHUB_TOKEN` sudah diset
- Pastikan URL repo benar
- Pastikan token punya akses ke repo (untuk private repo)

### Error: "Push failed: Authentication failed"

**Solusi:**
- Pastikan `GITHUB_TOKEN` valid
- Regenerate token jika perlu
- Pastikan token punya permission `repo`

### Gallery tidak update

**Solusi:**
- Cek apakah `generate_gallery_index()` dipanggil
- Cek apakah `index.html` ter-generate di showcase repo
- Cek apakah file ter-commit dan ter-push

### Project tidak muncul di gallery

**Solusi:**
- Pastikan project folder ada di `showcase_repo/projects/`
- Pastikan project folder berisi `index.html`
- Regenerate gallery index manual jika perlu

---

## 📋 Checklist Setup

- [x] Repo showcase sudah dibuat di GitHub (https://github.com/MarioSitepu/Jack-s-Cards)
- [ ] `PUSH_TO_SHOWCASE = True` (atau via env var)
- [ ] `SHOWCASE_REPO_URL` sudah diset
- [ ] `GITHUB_TOKEN` sudah diset
- [ ] Test generate project baru
- [ ] Cek project ter-copy ke showcase repo
- [ ] Cek gallery index.html ter-generate
- [ ] Cek push ke GitHub berhasil
- [ ] (Opsional) Enable GitHub Pages
- [ ] (Opsional) Akses website gallery

---

## 💡 Tips

1. **Gunakan repo public** untuk GitHub Pages gratis
2. **Custom domain** - Bisa set custom domain di GitHub Pages settings
3. **Auto-deploy** - Setiap push otomatis update website
4. **Backup** - Repo showcase juga berfungsi sebagai backup
5. **Portfolio** - Gallery bisa jadi portfolio AI-generated projects

---

## 🎉 Selesai!

Setelah setup, setiap project yang di-generate akan otomatis:
- ✅ Ter-copy ke repo showcase
- ✅ Gallery website ter-update
- ✅ Ter-push ke GitHub
- ✅ Tersedia di GitHub Pages (jika enabled)

**Selamat! Website gallery Anda siap! 🚀**

