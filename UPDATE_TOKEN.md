# 🔄 Update GitHub PAT Token

Panduan lengkap untuk update GitHub Personal Access Token (PAT) setelah regenerate.

## 📍 Lokasi Token yang Perlu Diupdate

Token GitHub digunakan di 2 tempat:
1. **Environment Variable** (untuk local script/EXE)
2. **GitHub Secrets** (untuk GitHub Actions)

---

## 🔧 Step 1: Update Environment Variable (Local)

Token ini digunakan oleh script Python/EXE yang berjalan di komputer Anda.

### Windows (PowerShell) - Temporary (Sesi Saat Ini)

```powershell
$env:GITHUB_TOKEN_PAT="your-new-token-here"
```

Atau:

```powershell
$env:GITHUB_TOKEN="your-new-token-here"
```

### Windows (Command Prompt) - Temporary

```cmd
set GITHUB_TOKEN_PAT=your-new-token-here
```

Atau:

```cmd
set GITHUB_TOKEN=your-new-token-here
```

### Windows - Permanent (Recommended)

1. Tekan `Win + R`
2. Ketik `sysdm.cpl` dan tekan Enter
3. Tab **"Advanced"** → Klik **"Environment Variables"**
4. Di bagian **"User variables"**, cari:
   - `GITHUB_TOKEN_PAT` atau
   - `GITHUB_TOKEN`
5. Jika ada, klik **"Edit"** → Update value dengan token baru
6. Jika tidak ada, klik **"New"**:
   - **Variable name:** `GITHUB_TOKEN_PAT`
   - **Variable value:** `your-new-token-here`
7. Klik **OK** → **OK**
8. **Restart PowerShell/Command Prompt** untuk apply perubahan

### Linux/Mac

```bash
export GITHUB_TOKEN_PAT="your-new-token-here"
```

Untuk permanent, tambahkan ke `~/.bashrc` atau `~/.zshrc`:

```bash
echo 'export GITHUB_TOKEN_PAT="your-new-token-here"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🔐 Step 2: Update GitHub Secrets (GitHub Actions)

Token ini digunakan oleh GitHub Actions untuk auto-commit/push.

### Update Secret di Repository

1. **Buka Repository di GitHub:**
   - Buka: https://github.com/MarioSitepu/Jack-s-Cards
   - Atau repository showcase Anda

2. **Buka Settings:**
   - Klik tab **"Settings"** (di atas repository)

3. **Buka Secrets:**
   - Di menu kiri, klik **"Secrets and variables"**
   - Klik **"Actions"**

4. **Update Secret:**
   - Cari secret **`GITHUBTOKENPAT`** (atau `GITHUB_TOKEN_PAT` atau `GITHUB_TOKEN`)
   - Klik secret tersebut
   - Klik **"Update"** (atau hapus dan buat baru)
   - Paste token baru
   - Klik **"Update secret"**

   **Note:** Code mendukung beberapa nama secret:
   - `GITHUBTOKENPAT` (tanpa underscore) ✅
   - `GITHUB_TOKEN_PAT` (dengan underscore)
   - `GITHUB_TOKEN` (default)

5. **Verifikasi:**
   - Pastikan secret sudah ter-update
   - Status: ✅ Secret updated

---

## ✅ Step 3: Verifikasi Token

### Test di Local (PowerShell)

```powershell
# Cek apakah token sudah ter-set
echo $env:GITHUB_TOKEN_PAT

# Atau
echo $env:GITHUB_TOKEN
```

Jika muncul token Anda, berarti sudah ter-set dengan benar.

### Test dengan Generate Project

1. Jalankan AI Worker (EXE atau Python script)
2. Generate project baru
3. Cek apakah push ke GitHub berhasil
4. Lihat di terminal/console apakah ada error authentication

### Test GitHub Actions

1. Buka tab **"Actions"** di repository
2. Pilih workflow **"Auto Commit AI Output"**
3. Klik **"Run workflow"** → **"Run workflow"**
4. Cek logs untuk memastikan tidak ada error authentication

---

## 🔍 Troubleshooting

### Token Tidak Terdeteksi

**Problem:** Script tidak bisa push ke GitHub

**Solution:**
1. Pastikan environment variable sudah di-set
2. Restart terminal/PowerShell setelah set environment variable
3. Cek dengan `echo $env:GITHUB_TOKEN_PAT` (PowerShell) atau `echo $GITHUB_TOKEN_PAT` (Linux/Mac)

### GitHub Actions Gagal Push

**Problem:** GitHub Actions error "Permission denied" atau "Authentication failed"

**Solution:**
1. Pastikan secret `GITHUBTOKENPAT` (atau `GITHUB_TOKEN_PAT`) sudah di-update di GitHub Secrets
2. Pastikan token memiliki permission **"Contents: Read and write"**
3. Pastikan token tidak expired
4. Cek logs GitHub Actions untuk detail error
5. Pastikan nama secret sesuai: `GITHUBTOKENPAT`, `GITHUB_TOKEN_PAT`, atau `GITHUB_TOKEN`

### Token Expired

**Problem:** Token sudah expired

**Solution:**
1. Buat token baru di: https://github.com/settings/tokens
2. Update environment variable (Step 1)
3. Update GitHub Secrets (Step 2)

---

## 📝 Catatan Penting

1. **Jangan commit token ke repository!** Token hanya disimpan di:
   - Environment variable (local)
   - GitHub Secrets (cloud)

2. **Token Format:**
   - Fine-grained PAT: `github_pat_...`
   - Classic PAT: `ghp_...`

3. **Permissions yang Diperlukan:**
   - ✅ **Contents:** Read and write
   - ✅ **Metadata:** Read-only

4. **Token Expiration:**
   - Set expiration sesuai kebutuhan
   - Atau set "No expiration" (tidak recommended untuk production)

---

## ✅ Checklist Update Token

- [ ] Environment variable `GITHUB_TOKEN_PAT` atau `GITHUBTOKENPAT` sudah di-update (local)
- [ ] GitHub Secret `GITHUBTOKENPAT` (atau `GITHUB_TOKEN_PAT`) sudah di-update (repository)
- [ ] Terminal/PowerShell sudah di-restart (jika set permanent)
- [ ] Token sudah di-test dengan generate project
- [ ] GitHub Actions sudah di-test dan berhasil

---

**Selesai!** Token baru sudah ter-update dan siap digunakan. 🎉

