# 🚀 Setup Auto-Start (Windows Startup)

Panduan untuk menambahkan AI-Daily-Summary.exe ke Windows Startup agar aplikasi otomatis berjalan saat Windows boot.

## 🎯 Metode Setup

### Metode 1: Menggunakan Script Batch (Paling Mudah) ⭐

1. **Jalankan script:**
   ```cmd
   setup_startup.bat
   ```

2. **Script akan:**
   - Mencari `AI-Daily-Summary.exe` di folder `dist/` atau root
   - Membuat shortcut di Windows Startup folder
   - Menampilkan status sukses/error

3. **Selesai!** Aplikasi akan auto-start saat Windows boot.

---

### Metode 2: Menggunakan Python Script

1. **Install dependency (opsional, untuk shortcut yang lebih baik):**
   ```bash
   pip install pywin32
   ```

2. **Jalankan script:**
   ```bash
   python setup_startup.py
   ```

3. **Pilih metode:**
   - `1` = Startup Folder (Recommended)
   - `2` = Windows Registry
   - `3` = Keduanya

4. **Selesai!**

---

### Metode 3: Manual Setup

#### A. Via Startup Folder

1. **Buka Startup folder:**
   - Tekan `Win + R`
   - Ketik: `shell:startup`
   - Enter

2. **Buat shortcut:**
   - Klik kanan di folder Startup
   - New → Shortcut
   - Browse ke `AI-Daily-Summary.exe`
   - Next → Finish

3. **Selesai!**

#### B. Via Registry (Advanced)

1. **Buka Registry Editor:**
   - Tekan `Win + R`
   - Ketik: `regedit`
   - Enter

2. **Navigasi ke:**
   ```
   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
   ```

3. **Buat String Value baru:**
   - Name: `AI-Daily-Summary`
   - Value: `C:\path\to\AI-Daily-Summary.exe`

4. **Selesai!**

---

## ✅ Verifikasi

### Cek Startup Folder:
1. Tekan `Win + R`
2. Ketik: `shell:startup`
3. Pastikan ada shortcut `AI-Daily-Summary.lnk`

### Cek Registry:
1. Tekan `Win + R`
2. Ketik: `regedit`
3. Navigasi ke: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
4. Pastikan ada entry `AI-Daily-Summary`

### Test:
1. Restart komputer
2. Aplikasi harus otomatis berjalan saat Windows boot
3. Cek system tray untuk icon aplikasi

---

## 🗑️ Remove dari Startup

### Menggunakan Script:

**Batch:**
```cmd
setup_startup.bat
```
Pilih `y` ketika ditanya "Remove from startup?"

**Python:**
```bash
python setup_startup.py
```
Script akan detect jika sudah ada dan tanya untuk remove.

### Manual:

**Via Startup Folder:**
1. Tekan `Win + R` → `shell:startup`
2. Hapus shortcut `AI-Daily-Summary.lnk`

**Via Registry:**
1. Tekan `Win + R` → `regedit`
2. Navigasi ke: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
3. Hapus entry `AI-Daily-Summary`

---

## ⚠️ Troubleshooting

### Error: "Access Denied"

**Solusi:**
- Run script sebagai Administrator
- Atau gunakan Startup Folder (tidak perlu admin)

### EXE tidak ditemukan

**Solusi:**
- Pastikan EXE sudah di-build (`build_exe.py` atau `build.bat`)
- Pastikan script dijalankan dari project root directory
- Atau edit script dan set path EXE manual

### Aplikasi tidak auto-start

**Solusi:**
1. Cek apakah shortcut/registry entry sudah dibuat
2. Cek apakah EXE path benar (tidak pindah folder)
3. Cek Windows Startup settings:
   - Settings → Apps → Startup
   - Pastikan aplikasi enabled

### Aplikasi start tapi tidak muncul di system tray

**Solusi:**
- Normal, aplikasi berjalan di background
- Klik kanan di system tray → Show hidden icons
- Atau buka aplikasi dari Start Menu

---

## 📋 Checklist

- [ ] EXE sudah di-build
- [ ] Script setup_startup.bat/py sudah dijalankan
- [ ] Shortcut/Registry entry sudah dibuat
- [ ] Test restart komputer
- [ ] Aplikasi auto-start berhasil

---

## 💡 Tips

1. **Untuk Development:**
   - Jangan set startup saat development
   - Hanya set startup untuk production/EXE

2. **Path EXE:**
   - Jika EXE dipindah folder, update shortcut/registry
   - Atau gunakan absolute path

3. **Multiple Users:**
   - Startup Folder: Per-user (HKEY_CURRENT_USER)
   - Registry: Per-user (HKEY_CURRENT_USER)
   - Untuk all users, gunakan HKEY_LOCAL_MACHINE (perlu admin)

4. **Silent Start:**
   - Aplikasi sudah berjalan di background
   - Tidak muncul window (system tray only)
   - Perfect untuk auto-start!

---

**Selamat! Aplikasi sekarang akan auto-start saat Windows boot! 🎉**

