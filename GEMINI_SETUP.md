# 🔑 Setup Gemini 2.5 Flash API Key

Panduan lengkap step-by-step untuk mendapatkan dan setup API key Google Gemini 2.5 Flash.

## 📋 Langkah-langkah

### Step 1: Dapatkan API Key dari Google AI Studio

1. **Buka Google AI Studio:**
   - Kunjungi: https://aistudio.google.com/app/apikey
   - Atau: https://makersuite.google.com/app/apikey

2. **Login dengan Google Account:**
   - Gunakan akun Google Anda
   - Jika belum punya, buat akun Google dulu

3. **Buat API Key:**
   - Klik tombol **"Create API Key"** atau **"Get API Key"**
   - Pilih project Google Cloud (atau buat baru)
   - API key akan langsung dibuat dan ditampilkan

4. **Copy API Key:**
   - **PENTING:** Copy API key Anda sekarang!
   - Format: `AIzaSy...` (panjang sekitar 39 karakter)
   - Simpan di tempat yang aman

---

### Step 2: Setup API Key di Sistem

Pilih salah satu metode di bawah:

#### **Metode 1: Environment Variable (Recommended)**

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=AIzaSy...your-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="AIzaSy...your-api-key-here"
```

**Windows (Permanent - System Properties):**
1. Tekan `Win + R`
2. Ketik `sysdm.cpl` dan Enter
3. Tab "Advanced" → "Environment Variables"
4. Klik "New" di User variables
5. Variable name: `GEMINI_API_KEY`
6. Variable value: `AIzaSy...your-api-key-here`
7. OK → OK

**Linux/Mac:**
```bash
export GEMINI_API_KEY=AIzaSy...your-api-key-here
```

**Linux/Mac (Permanent - .bashrc/.zshrc):**
```bash
# Edit file
nano ~/.bashrc
# atau
nano ~/.zshrc

# Tambahkan baris ini di akhir file:
export GEMINI_API_KEY=AIzaSy...your-api-key-here

# Save dan reload
source ~/.bashrc
# atau
source ~/.zshrc
```

---

#### **Metode 2: File .env (Alternatif)**

1. **Buat file `.env` di root project:**
   ```
   AiCommitBot/
   ├─ .env          ← Buat file ini
   ├─ ai_worker/
   └─ ...
   ```

2. **Isi file `.env`:**
   ```
   GEMINI_API_KEY=AIzaSy...your-api-key-here
   ```

3. **Install python-dotenv (jika belum):**
   ```bash
   pip install python-dotenv
   ```

4. **Update code untuk load .env:**
   Tambahkan di awal `ai_worker/generate.py`:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

---

#### **Metode 3: Langsung di Code (Tidak Recommended - Hanya untuk Testing)**

⚠️ **Warning:** Jangan commit API key ke Git!

Edit `ai_worker/ai_html_generator.py`:
```python
# Hanya untuk testing, jangan untuk production!
api_key = "AIzaSy...your-api-key-here"  # Ganti dengan API key Anda
```

---

### Step 3: Verifikasi Setup

**Test apakah API key sudah ter-set:**

**Windows:**
```cmd
echo %GEMINI_API_KEY%
```

**Linux/Mac:**
```bash
echo $GEMINI_API_KEY
```

**Python Test:**
```python
import os
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    print(f"✅ API Key found: {api_key[:10]}...")
else:
    print("❌ API Key not found!")
```

---

### Step 4: Install Library

```bash
pip install google-generativeai
```

---

### Step 5: Test Koneksi

Buat file test `test_gemini.py`:

```python
import os
import google.generativeai as genai

# Load API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ GEMINI_API_KEY not found!")
    print("Set dengan: export GEMINI_API_KEY=your-key")
    exit(1)

# Configure
genai.configure(api_key=api_key)

# Test
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Say hello!")
    print("✅ Gemini API works!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ Error: {e}")
```

Jalankan:
```bash
python test_gemini.py
```

---

## 🔒 Keamanan

### ⚠️ Jangan Commit API Key ke Git!

1. **Pastikan `.env` ada di `.gitignore`:**
   ```
   .env
   *.env
   ```

2. **Jangan hardcode API key di code**

3. **Gunakan environment variable**

4. **Jangan share API key ke publik**

---

## 🐛 Troubleshooting

### Error: "API key not found"

**Solusi:**
- Pastikan environment variable sudah di-set
- Restart terminal/command prompt setelah set variable
- Cek dengan `echo $GEMINI_API_KEY` (Linux/Mac) atau `echo %GEMINI_API_KEY%` (Windows)

### Error: "Invalid API key"

**Solusi:**
- Pastikan API key sudah di-copy dengan benar
- Tidak ada spasi di awal/akhir API key
- Cek di Google AI Studio apakah API key masih aktif

### Error: "Quota exceeded"

**Solusi:**
- Gemini free tier memiliki limit
- Tunggu beberapa saat atau upgrade ke paid plan
- Cek quota di Google Cloud Console

### Error: "Module not found: google.generativeai"

**Solusi:**
```bash
pip install google-generativeai
```

---

## 📊 Quota & Limits

**Gemini Free Tier:**
- 15 requests per minute (RPM)
- 1,500 requests per day (RPD)
- Sangat cukup untuk penggunaan normal!

**Upgrade:**
- Kunjungi Google Cloud Console
- Enable billing untuk quota lebih besar

---

## ✅ Checklist Setup

- [ ] Dapatkan API key dari https://aistudio.google.com/app/apikey
- [ ] Set environment variable `GEMINI_API_KEY`
- [ ] Install `google-generativeai`: `pip install google-generativeai`
- [ ] Test dengan `test_gemini.py`
- [ ] Pastikan `.env` ada di `.gitignore` (jika pakai .env)
- [ ] Run aplikasi: `python ai_worker/generate.py`

---

## 🚀 Quick Start (TL;DR)

```bash
# 1. Install
pip install google-generativeai

# 2. Set API Key
export GEMINI_API_KEY=your-api-key-here  # Linux/Mac
# atau
set GEMINI_API_KEY=your-api-key-here     # Windows CMD

# 3. Test
python test_gemini.py

# 4. Run
python ai_worker/generate.py
```

---

**Selamat! API key Gemini sudah siap digunakan! 🎉**

