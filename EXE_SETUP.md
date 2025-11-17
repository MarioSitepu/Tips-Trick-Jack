# 📦 Setup EXE dengan Gemini API

Panduan lengkap untuk build dan menggunakan EXE dengan Gemini API support.

## 🚀 Build EXE

### Quick Build:
```bash
# Windows: Double-click
build.bat

# Atau manual:
python build_exe.py
```

### Build dengan Dependencies:
```bash
# Install semua dependencies termasuk Gemini
pip install -r requirements.txt

# Build
python build_exe.py
```

---

## 🔑 Setup API Key untuk EXE

EXE akan membaca API key dari **environment variable**. Ada beberapa cara:

### Metode 1: Set Sebelum Run (Sementara)

**Command Prompt:**
```cmd
set GEMINI_API_KEY=your-api-key-here
AI-Daily-Summary.exe
```

**PowerShell:**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
.\AI-Daily-Summary.exe
```

**Batch File (create `run_exe.bat`):**
```batch
@echo off
set GEMINI_API_KEY=your-api-key-here
AI-Daily-Summary.exe
```

---

### Metode 2: System Environment Variable (Permanent) ⭐ Recommended

1. **Buka System Properties:**
   - Tekan `Win + R`
   - Ketik `sysdm.cpl`
   - Enter

2. **Set Environment Variable:**
   - Tab "Advanced"
   - Klik "Environment Variables"
   - Di bagian "User variables", klik "New"
   - Variable name: `GEMINI_API_KEY`
   - Variable value: `your-api-key-here`
   - OK → OK

3. **Restart:**
   - Log off dan log on lagi
   - Atau restart komputer
   - EXE akan otomatis membaca API key

---

### Metode 3: Buat Launcher Script

Buat file `run_with_api_key.bat`:

```batch
@echo off
REM Set API key
set GEMINI_API_KEY=your-api-key-here

REM Run EXE
cd /d "%~dp0"
AI-Daily-Summary.exe
```

Ganti `your-api-key-here` dengan API key Anda.

---

## ✅ Verifikasi Setup

### Test API Key di EXE:

1. **Run EXE:**
   ```cmd
   AI-Daily-Summary.exe
   ```

2. **Cek Status:**
   - Right-click icon di system tray
   - Klik "Show Status"
   - Lihat log messages
   - Jika ada: `✅ Generated with AI (gemini)` → API key bekerja!
   - Jika ada: `⚠️ AI generation failed` → Cek API key

---

## 🐛 Troubleshooting

### EXE tidak bisa generate dengan AI

**Problem:** EXE selalu pakai template, tidak pakai AI

**Solusi:**
1. Pastikan API key sudah di-set:
   ```cmd
   echo %GEMINI_API_KEY%
   ```
   Harus menampilkan API key Anda

2. Restart EXE setelah set environment variable

3. Cek log di Status window untuk error message

---

### Error: "API key not found"

**Solusi:**
- Set environment variable `GEMINI_API_KEY`
- Pastikan sudah restart terminal/EXE setelah set variable
- Gunakan System Environment Variables untuk permanent

---

### EXE tidak muncul di system tray

**Solusi:**
- Cek hidden icons (klik arrow ^ di system tray)
- Restart EXE
- Pastikan tidak ada error saat startup

---

## 📋 Checklist Setup EXE

- [ ] Build EXE: `python build_exe.py`
- [ ] Dapatkan Gemini API key dari https://aistudio.google.com/app/apikey
- [ ] Set environment variable `GEMINI_API_KEY`
- [ ] Test dengan: `echo %GEMINI_API_KEY%` (harus muncul API key)
- [ ] Run EXE: `AI-Daily-Summary.exe`
- [ ] Cek Status window untuk konfirmasi AI generation
- [ ] Verifikasi folder `projects/` terbuat dengan HTML/CSS

---

## 💡 Tips

1. **Untuk Development:**
   - Gunakan Python script langsung: `python ai_worker/generate_gui.py`
   - Lebih mudah debug

2. **Untuk Production:**
   - Build EXE
   - Set API key di System Environment Variables
   - Auto-start dengan Windows (copy ke Startup folder)

3. **Tanpa API Key:**
   - EXE tetap bisa jalan
   - Akan pakai template HTML/CSS (tidak pakai AI)
   - Masih generate proyek setiap 30 menit

---

## 🎯 Quick Start EXE

```cmd
# 1. Build
build.bat

# 2. Set API Key
set GEMINI_API_KEY=your-api-key-here

# 3. Run
cd dist
AI-Daily-Summary.exe
```

---

**Selamat menggunakan EXE dengan Gemini API! 🎉**

