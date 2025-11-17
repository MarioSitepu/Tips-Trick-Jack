# 🔧 Setup GitHub Actions untuk Auto-Commit

Panduan lengkap setup GitHub Actions untuk auto-commit proyek HTML/CSS.

## 🔑 Token yang Diperlukan

### Opsi 1: GITHUB_TOKEN (Default - Paling Mudah) ⭐

**GITHUB_TOKEN** adalah token otomatis yang disediakan GitHub Actions. **Tidak perlu setup manual!**

**Keuntungan:**
- ✅ Otomatis tersedia di setiap workflow
- ✅ Tidak perlu membuat token manual
- ✅ Aman (hanya untuk repository yang sama)
- ✅ Cukup untuk kebanyakan kasus

**Keterbatasan:**
- ❌ Tidak bisa push ke **protected branches**
- ❌ Tidak bisa trigger workflow lain
- ❌ Terbatas untuk repository yang sama

**Kapan cukup pakai GITHUB_TOKEN:**
- ✅ Branch default (main/master) tidak protected
- ✅ Hanya commit ke repository yang sama
- ✅ Tidak perlu trigger workflow lain

---

### Opsi 2: Fine-grained Personal Access Token (PAT)

**Diperlukan jika:**
- ❌ Branch default adalah **protected branch**
- ❌ Butuh push ke branch lain
- ❌ Butuh trigger workflow lain
- ❌ Repository private dengan restrictions

---

## 🚀 Setup dengan GITHUB_TOKEN (Recommended)

**Tidak perlu setup apa-apa!** Workflow sudah dikonfigurasi untuk pakai GITHUB_TOKEN.

### Langkah-langkah:

1. **Pastikan branch tidak protected:**
   - Settings → Branches
   - Pastikan branch default (main/master) tidak ada protection rules
   - Atau disable "Require pull request reviews"

2. **Push workflow ke GitHub:**
   ```bash
   git add .github/workflows/auto-commit.yml
   git commit -m "Add GitHub Actions workflow"
   git push
   ```

3. **Enable GitHub Actions:**
   - Settings → Actions → General
   - Pastikan "Allow all actions and reusable workflows" enabled

4. **Test workflow:**
   - Tab "Actions" di GitHub
   - Klik workflow "Auto Commit AI Output"
   - Klik "Run workflow" untuk test manual

**Selesai!** Workflow akan otomatis jalan setiap 30 menit.

---

## 🔐 Setup dengan Fine-grained Personal Access Token

Jika branch protected atau butuh permissions lebih, ikuti langkah ini:

### Step 1: Buat Fine-grained PAT

1. **Buka GitHub Settings:**
   - Klik profile picture → Settings
   - Atau: https://github.com/settings/tokens

2. **Buat Token:**
   - Klik "Developer settings" (kiri bawah)
   - Klik "Personal access tokens" → "Fine-grained tokens"
   - Klik "Generate new token"

3. **Konfigurasi Token:**
   - **Token name:** `AI-Daily-Summary-Actions`
   - **Expiration:** Sesuai kebutuhan (90 days, 1 year, atau no expiration)
   - **Repository access:** 
     - Pilih "Only select repositories"
     - Pilih repository Anda

4. **Set Permissions:**
   - **Repository permissions:**
     - ✅ **Contents:** Read and write
     - ✅ **Metadata:** Read-only
     - ✅ **Pull requests:** Read-only (opsional)
   
   - **Account permissions:** Tidak perlu

5. **Generate Token:**
   - Klik "Generate token"
   - **PENTING:** Copy token sekarang! (hanya muncul sekali)
   - Format: `github_pat_...`

---

### Step 2: Tambahkan Token ke Repository Secrets

1. **Buka Repository Settings:**
   - Repository → Settings → Secrets and variables → Actions

2. **Tambah Secret:**
   - Klik "New repository secret"
   - **Name:** `GITHUB_TOKEN_PAT` (atau nama lain)
   - **Secret:** Paste token yang sudah di-copy
   - Klik "Add secret"

---

### Step 3: Update Workflow

Edit `.github/workflows/auto-commit.yml`:

```yaml
steps:
  - name: Checkout repo
    uses: actions/checkout@v4
    with:
      token: ${{ secrets.GITHUB_TOKEN_PAT }}  # Ganti dengan nama secret Anda
```

Atau gunakan conditional:

```yaml
steps:
  - name: Checkout repo
    uses: actions/checkout@v4
    with:
      token: ${{ secrets.GITHUB_TOKEN_PAT || secrets.GITHUB_TOKEN }}
```

---

## ✅ Verifikasi Setup

### Test Workflow:

1. **Manual Trigger:**
   - Tab "Actions" → "Auto Commit AI Output"
   - Klik "Run workflow"
   - Pilih branch → "Run workflow"

2. **Cek Logs:**
   - Klik run yang baru dibuat
   - Lihat logs untuk error
   - Pastikan commit berhasil

3. **Cek Repository:**
   - Lihat commit history
   - Pastikan ada commit dari "AI-Bot"
   - Cek folder `projects/` dan `data/`

---

## 🐛 Troubleshooting

### Error: "Permission denied"

**Problem:** Workflow tidak bisa push

**Solusi:**
- Pastikan `permissions: contents: write` ada di workflow
- Jika branch protected, gunakan Fine-grained PAT
- Cek branch protection rules

---

### Error: "Resource not accessible by integration"

**Problem:** GITHUB_TOKEN tidak punya permission

**Solusi:**
- Gunakan Fine-grained PAT
- Atau disable branch protection

---

### Workflow tidak jalan otomatis

**Problem:** Schedule tidak trigger

**Solusi:**
- Pastikan repository punya activity (ada commit dalam 60 hari)
- Atau trigger manual dulu untuk activate
- Cek Actions settings → Allow all actions

---

### Commit tidak muncul

**Problem:** Workflow jalan tapi tidak commit

**Solusi:**
- Cek logs untuk error
- Pastikan ada perubahan di folder `data/` atau `projects/`
- Cek git config (user.name dan user.email)

---

## 📋 Checklist Setup

### Dengan GITHUB_TOKEN (Default):
- [ ] Branch default tidak protected
- [ ] Workflow file sudah di-push ke GitHub
- [ ] GitHub Actions enabled
- [ ] Test workflow manual
- [ ] Verifikasi commit muncul

### Dengan Fine-grained PAT:
- [ ] Buat Fine-grained PAT
- [ ] Set permissions (Contents: Read and write)
- [ ] Tambahkan ke Repository Secrets
- [ ] Update workflow untuk pakai PAT
- [ ] Test workflow manual
- [ ] Verifikasi commit muncul

---

## 🔒 Security Best Practices

1. **Jangan commit token ke repository**
   - Selalu pakai Secrets
   - Jangan hardcode di workflow

2. **Minimal permissions**
   - Hanya beri permissions yang diperlukan
   - Fine-grained PAT lebih aman dari Classic PAT

3. **Rotate tokens**
   - Set expiration date
   - Regenerate token secara berkala

4. **Monitor usage**
   - Cek Actions logs
   - Monitor commit activity

---

## 💡 Tips

1. **Untuk testing:**
   - Gunakan `workflow_dispatch` untuk trigger manual
   - Test di branch terpisah dulu

2. **Untuk production:**
   - Set schedule sesuai kebutuhan
   - Monitor commit frequency
   - Pastikan tidak spam commit

3. **Jika branch protected:**
   - Gunakan Fine-grained PAT
   - Atau disable protection untuk branch ini
   - Atau gunakan branch terpisah untuk auto-commit

---

## 📊 Perbandingan Token

| Feature | GITHUB_TOKEN | Fine-grained PAT |
|---------|--------------|------------------|
| Setup | ✅ Otomatis | ❌ Manual |
| Protected Branch | ❌ Tidak bisa | ✅ Bisa |
| Permissions | Terbatas | Customizable |
| Security | ✅ Aman | ✅ Aman |
| Recommended | ✅ Untuk kebanyakan kasus | Untuk protected branch |

---

**Selamat setup GitHub Actions! 🎉**

