# 🤖 Setup AI untuk Generate HTML/CSS

Panduan lengkap untuk setup AI agar bisa generate HTML/CSS secara otomatis.

## 🎯 Fitur AI Generation

Dengan AI enabled, setiap generate akan:
- ✅ Generate HTML/CSS yang unik setiap kali
- ✅ Variasi design yang berbeda-beda
- ✅ Konten yang lebih dinamis
- ✅ Styling yang lebih kreatif

## 📋 Supported AI Providers

### 1. Google Gemini 2.5 Flash (Default - Recommended) ⭐

**Keuntungan:**
- ✅ Gratis dengan quota generous
- ✅ Sangat cepat (Flash model)
- ✅ Hasil sangat bagus
- ✅ Easy setup

**Setup:**
```bash
# Install
pip install google-generativeai

# Set API Key
# Windows:
set GEMINI_API_KEY=your-api-key-here

# Linux/Mac:
export GEMINI_API_KEY=your-api-key-here

# Atau buat file .env:
GEMINI_API_KEY=your-api-key-here
```

**Dapatkan API Key:**
1. Kunjungi https://aistudio.google.com/app/apikey
2. Buat API key baru (gratis!)
3. Copy dan set sebagai environment variable

**Konfigurasi:**
Edit `ai_worker/generate.py`:
```python
USE_AI = True
AI_PROVIDER = "gemini"  # Default
```

---

### 2. OpenAI

**Keuntungan:**
- Hasil sangat bagus
- Reliable dan cepat
- Support GPT-4, GPT-3.5

**Setup:**
```bash
# Install
pip install openai

# Set API Key
# Windows:
set OPENAI_API_KEY=your-api-key-here

# Linux/Mac:
export OPENAI_API_KEY=your-api-key-here

# Atau buat file .env:
OPENAI_API_KEY=your-api-key-here
```

**Dapatkan API Key:**
1. Kunjungi https://platform.openai.com/api-keys
2. Buat API key baru
3. Copy dan set sebagai environment variable

**Konfigurasi:**
Edit `ai_worker/generate.py`:
```python
USE_AI = True
AI_PROVIDER = "openai"  # atau "auto"
```

---

### 3. Ollama (AI Lokal - Gratis!)

**Keuntungan:**
- ✅ 100% Gratis
- ✅ Berjalan lokal (tidak perlu internet)
- ✅ Privacy terjaga
- ✅ Tidak ada limit API

**Setup:**
```bash
# 1. Install Ollama
# Download dari: https://ollama.ai

# 2. Install model
ollama pull llama3.2
# atau
ollama pull mistral
# atau
ollama pull codellama

# 3. Install Python library
pip install ollama
```

**Konfigurasi:**
Edit `ai_worker/generate.py`:
```python
USE_AI = True
AI_PROVIDER = "ollama"  # atau "auto"
```

**Note:** Pastikan Ollama service berjalan di background.

---

### 4. Anthropic Claude

**Keuntungan:**
- Hasil sangat bagus
- Support Claude 3 models
- Good for creative content

**Setup:**
```bash
# Install
pip install anthropic

# Set API Key
export ANTHROPIC_API_KEY=your-api-key-here
```

**Dapatkan API Key:**
1. Kunjungi https://console.anthropic.com/
2. Buat API key
3. Set sebagai environment variable

**Konfigurasi:**
Edit `ai_worker/generate.py`:
```python
USE_AI = True
AI_PROVIDER = "anthropic"
```

---

## ⚙️ Konfigurasi

### Edit `ai_worker/generate.py`:

```python
# Enable/Disable AI
USE_AI = True  # Set False untuk selalu pakai template

# Pilih Provider
AI_PROVIDER = "auto"  # "openai", "ollama", "anthropic", atau "auto"

# Customize Output
THEME = "modern"  # "modern", "classic", "minimal", "dark", "colorful"
STYLE = "gradient"  # "gradient", "solid", "glassmorphism", "neon"
```

### Edit `ai_worker/generate_gui.py`:

Saat inisialisasi:
```python
worker = AIWorker(
    use_ai=True,
    ai_provider="auto",
    theme="modern",
    style="gradient"
)
```

---

## 🎨 Themes & Styles

### Themes:
- `modern` - Modern, clean design
- `classic` - Classic, traditional
- `minimal` - Minimalist design
- `dark` - Dark mode
- `colorful` - Bright, colorful
- `professional` - Business-like
- `creative` - Artistic, creative

### Styles:
- `gradient` - Gradient backgrounds
- `solid` - Solid colors
- `glassmorphism` - Glass effect
- `neon` - Neon glow effects
- `material` - Material Design
- `flat` - Flat design

---

## 🚀 Quick Start

### 1. Install Dependencies

**Untuk Gemini (Default - Recommended):**
```bash
pip install google-generativeai
export GEMINI_API_KEY=your-api-key
```

**Untuk OpenAI:**
```bash
pip install openai
export OPENAI_API_KEY=your-key
```

**Untuk Ollama:**
```bash
# Install Ollama dari https://ollama.ai
ollama pull llama3.2
pip install ollama
```

### 2. Enable AI

Edit `ai_worker/generate.py`:
```python
USE_AI = True
AI_PROVIDER = "gemini"  # Default, atau "openai", "ollama", "auto", dll
```

### 3. Run

```bash
python ai_worker/generate.py
# atau
python ai_worker/generate_gui.py
```

---

## 🔍 Testing AI

Test apakah AI bekerja:

```python
from ai_worker.ai_html_generator import generate_html_css_with_ai

html, css = generate_html_css_with_ai(
    "2025-01-17",
    ai_provider="openai",  # atau "ollama"
    theme="modern",
    style="gradient"
)

if html and css:
    print("✅ AI generation works!")
    print(f"HTML length: {len(html)}")
    print(f"CSS length: {len(css)}")
else:
    print("❌ AI generation failed, check setup")
```

---

## 🛠️ Troubleshooting

### Error: "OpenAI not installed"
```bash
pip install openai
```

### Error: "API key not found"
- Set environment variable: `export OPENAI_API_KEY=your-key`
- Atau buat file `.env` dengan `OPENAI_API_KEY=your-key`

### Error: "Ollama connection failed"
- Pastikan Ollama service berjalan: `ollama serve`
- Test: `ollama list` (harus return models)

### AI tidak generate, pakai template
- Check `USE_AI = True`
- Check API key sudah di-set
- Check provider tersedia
- Lihat error message di console

### Hasil AI tidak sesuai
- Coba ubah `theme` dan `style`
- Coba provider lain
- Coba model yang berbeda (untuk OpenAI: gpt-4, gpt-3.5-turbo)

---

## 💡 Tips

1. **Untuk hasil terbaik:** Gunakan OpenAI GPT-4
2. **Untuk gratis:** Gunakan Ollama (lokal)
3. **Untuk variasi:** Set `AI_PROVIDER = "auto"` (coba semua)
4. **Untuk konsistensi:** Set provider spesifik
5. **Untuk testing:** Set `USE_AI = False` dulu, test template

---

## 📊 Perbandingan Provider

| Provider | Cost | Quality | Speed | Setup |
|----------|------|---------|-------|-------|
| **Gemini 2.5 Flash** | 🆓 Free* | ⭐⭐⭐⭐⭐ | ⚡⚡⚡⚡ | Easy |
| OpenAI | 💰 Paid | ⭐⭐⭐⭐⭐ | ⚡⚡⚡ | Easy |
| Ollama | 🆓 Free | ⭐⭐⭐⭐ | ⚡⚡ | Medium |
| Anthropic | 💰 Paid | ⭐⭐⭐⭐⭐ | ⚡⚡⚡ | Easy |

*Gemini memiliki free tier yang sangat generus

---

**Selamat menggunakan AI untuk generate HTML/CSS! 🎉**

