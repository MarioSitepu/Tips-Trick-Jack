# 📥 Install Git untuk Windows

Panduan lengkap install Git di Windows untuk fitur auto-push.

## 🚀 Cara Install Git

### Metode 1: Download dari Situs Resmi (Recommended)

1. **Download Git:**
   - Buka: https://git-scm.com/download/win
   - Download akan otomatis dimulai
   - Atau klik "Click here to download" jika tidak otomatis

2. **Install Git:**
   - Double-click file installer (misalnya: `Git-2.43.0-64-bit.exe`)
   - Klik "Next" pada semua langkah
   - **PENTING:** Pastikan "Add Git to PATH" dicentang ✅
   - Pilih "Use Git from the Windows Command Prompt" (recommended)
   - Klik "Install"

3. **Verifikasi Install:**
   - Buka PowerShell baru (tutup yang lama, buka yang baru)
   - Jalankan:
     ```powershell
     git --version
     ```
   - Harus muncul: `git version 2.x.x`

---

### Metode 2: Install via Winget (Windows Package Manager)

Jika Anda punya Winget:

```powershell
winget install --id Git.Git -e --source winget
```

Setelah install, buka PowerShell baru dan verifikasi:
```powershell
git --version
```

---

### Metode 3: Install via Chocolatey

Jika Anda punya Chocolatey:

```powershell
choco install git
```

Setelah install, buka PowerShell baru dan verifikasi:
```powershell
git --version
```

---

## ⚠️ Troubleshooting

### Error: "git is not recognized"

**Solusi:**
1. Pastikan Git sudah terinstall
2. **Restart PowerShell** (tutup dan buka lagi)
3. Jika masih error, tambahkan Git ke PATH manual:
   - `Win + R` → `sysdm.cpl` → Enter
   - Tab "Advanced" → "Environment Variables"
   - Di "System variables", cari "Path" → Edit
   - Tambahkan: `C:\Program Files\Git\cmd`
   - OK → OK
   - Restart PowerShell

### Git sudah terinstall tapi tidak dikenali

**Solusi:**
1. Cek lokasi Git:
   ```powershell
   Get-Command git -ErrorAction SilentlyContinue
   ```
2. Jika tidak muncul, tambahkan ke PATH (lihat di atas)
3. Restart PowerShell

---

## ✅ Setelah Install Git

1. **Konfigurasi Git (opsional tapi recommended):**
   ```powershell
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

2. **Test Git:**
   ```powershell
   git --version
   git config --list
   ```

3. **Lanjutkan setup auto-push:**
   - Lihat [AUTO_PUSH_SETUP.md](AUTO_PUSH_SETUP.md)
   - Step 1: ✅ Git sudah terinstall
   - Step 2: Setup GitHub Token
   - Step 3: Set Environment Variable
   - Step 4: Enable Auto-Push

---

## 📋 Checklist

- [ ] Git terinstall (`git --version` berhasil)
- [ ] Git ada di PATH (bisa dipanggil dari PowerShell)
- [ ] Git sudah dikonfigurasi (user.name dan user.email)
- [ ] Siap untuk setup auto-push

---

**Setelah Git terinstall, lanjutkan ke [AUTO_PUSH_SETUP.md](AUTO_PUSH_SETUP.md) untuk setup auto-push! 🚀**

