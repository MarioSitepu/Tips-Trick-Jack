# 📦 Panduan Build EXE

Panduan lengkap untuk mengkonversi aplikasi AI Daily Summary Generator menjadi file `.exe` yang bisa berjalan di background dengan system tray.

## 🎯 Fitur EXE Version

- ✅ Berjalan di background (system tray)
- ✅ Icon di system tray untuk kontrol
- ✅ Tidak ada console window yang mengganggu
- ✅ Mudah diakses via right-click icon
- ✅ Auto-start dengan Windows (opsional)

## 📋 Prerequisites

1. **Python 3.8+** terinstall
2. **Windows OS** (untuk .exe)
3. **Internet connection** (untuk download dependencies)

## 🚀 Cara Build (Metode 1: Otomatis)

### Windows:
```bash
# Double-click file build.bat
# atau jalankan di Command Prompt:
build.bat
```

Script akan otomatis:
1. Install dependencies
2. Build executable
3. Menampilkan lokasi file .exe

## 🛠️ Cara Build (Metode 2: Manual)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Build EXE
```bash
python build_exe.py
```

Atau manual dengan PyInstaller:
```bash
pyinstaller --name=AI-Daily-Summary ^
    --onefile ^
    --windowed ^
    --add-data="data;data" ^
    --hidden-import=pystray ^
    --hidden-import=PIL ^
    --hidden-import=tkinter ^
    ai_worker/generate_gui.py
```

## 📁 Hasil Build

Setelah build selesai, file `.exe` akan ada di:
```
dist/AI-Daily-Summary.exe
```

## 🎮 Cara Menggunakan EXE

### 1. Setup API Key (Untuk AI Generation)

**PENTING:** Jika ingin menggunakan AI untuk generate HTML/CSS, set API key dulu!

**Cara 1: Environment Variable (Recommended)**
```cmd
# Set di Command Prompt sebelum run EXE
set GEMINI_API_KEY=your-api-key-here
AI-Daily-Summary.exe
```

**Cara 2: System Environment Variable (Permanent)**
1. Tekan `Win + R` → ketik `sysdm.cpl` → Enter
2. Tab "Advanced" → "Environment Variables"
3. Klik "New" di User variables
4. Variable name: `GEMINI_API_KEY`
5. Variable value: `your-api-key-here`
6. OK → OK
7. Restart komputer (atau log off/on)
8. Run EXE

**Cara 3: Buat file `.env` (jika EXE support)**
- Buat file `.env` di folder yang sama dengan EXE
- Isi: `GEMINI_API_KEY=your-api-key-here`

📖 **Panduan lengkap:** Lihat [GEMINI_SETUP.md](GEMINI_SETUP.md)

### 2. Jalankan EXE
- Double-click `AI-Daily-Summary.exe`
- Aplikasi akan berjalan di background
- Icon akan muncul di system tray (dekat jam)

### 3. Akses Menu
- **Right-click** icon di system tray
- Menu akan muncul dengan opsi:
  - Status: Running/Stopped
  - Show Status (buka window status)
  - Start Worker / Stop Worker
  - Exit

### 4. Monitor Status
- Klik "Show Status" untuk melihat log
- Window akan menampilkan:
  - Status worker (Running/Stopped)
  - Last update time
  - Log messages
  - Tombol Start/Stop
  - Info apakah AI generation berhasil atau pakai template

## ⚙️ Konfigurasi

### Mengubah Interval Waktu

Edit `ai_worker/generate_gui.py`, cari:
```python
self.interval = 1800  # 30 menit = 1800 detik
```

Ubah sesuai kebutuhan:
- 1 jam = 3600 detik
- 2 jam = 7200 detik
- 15 menit = 900 detik

**Setelah edit, build ulang EXE!**

### Auto-Start dengan Windows

1. Tekan `Win + R`
2. Ketik `shell:startup`
3. Copy shortcut `AI-Daily-Summary.exe` ke folder startup
4. Restart komputer untuk test

## 🔧 Troubleshooting

### Error: "pystray not found"
```bash
pip install pystray pillow
```

### Error: "tkinter not available"
- Windows: tkinter biasanya sudah include dengan Python
- Jika tidak ada, install Python dengan "tcl/tk" option

### EXE tidak muncul di system tray
- Cek icon hidden di system tray
- Klik arrow (^) di system tray untuk show hidden icons
- Restart aplikasi

### EXE tidak bisa write file
- Pastikan folder `data` ada di directory yang sama dengan EXE
- Atau run as Administrator (jika perlu)

### Build error: "ModuleNotFoundError"
```bash
# Install semua dependencies
pip install -r requirements.txt

# Rebuild
python build_exe.py
```

## 📝 File Structure Setelah Build

```
AiCommitBot/
│
├─ dist/
│   └─ AI-Daily-Summary.exe  ← File EXE yang bisa dijalankan
│
├─ build/                     ← Temporary build files (bisa dihapus)
│
├─ ai_worker/
│   ├─ generate.py           ← Script original (console)
│   └─ generate_gui.py       ← Script GUI (system tray)
│
├─ data/
│   └─ daily_summary.md      ← Output file
│
├─ build_exe.py              ← Build script
├─ build.bat                 ← Build script (Windows)
└─ requirements.txt
```

## 🎨 Customization

### Mengubah Icon System Tray

Edit `ai_worker/generate_gui.py`, fungsi `create_icon_image()`:
```python
def create_icon_image(self):
    # Load custom icon
    icon_path = Path(__file__).parent.parent / "icon.ico"
    if icon_path.exists():
        return Image.open(icon_path)
    # ... atau buat custom dengan PIL
```

Kemudian build dengan:
```bash
pyinstaller --icon=icon.ico ...
```

### Mengubah Nama Aplikasi

Edit `build_exe.py`:
```python
"--name=YourAppName",
```

## 📊 Ukuran File

- **EXE size**: ~15-25 MB (termasuk Python runtime)
- **Dependencies**: Sudah include dalam EXE (onefile mode)

## ✅ Checklist Sebelum Distribusi

- [ ] Test EXE di komputer lain (tanpa Python)
- [ ] Pastikan folder `data` bisa dibuat
- [ ] Test start/stop worker
- [ ] Test system tray menu
- [ ] Test status window
- [ ] Verifikasi file output terbuat

## 🚀 Distribusi

Untuk distribusi ke komputer lain:
1. Copy `AI-Daily-Summary.exe`
2. Pastikan folder `data` ada (atau akan dibuat otomatis)
3. Jalankan EXE
4. Tidak perlu install Python atau dependencies!

---

**Tips**: Untuk testing, jalankan `python ai_worker/generate_gui.py` dulu sebelum build EXE.

