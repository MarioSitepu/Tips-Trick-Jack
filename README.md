# AI Daily Summary Generator

Proyek ini menghasilkan ringkasan harian secara otomatis dengan AI yang dijalankan di server lokal. GitHub Actions hanya meng-commit perubahan setiap 30 menit.

## 🎯 Keunggulan

- ✅ **Aman dari limit GitHub Actions** - Workflow hanya commit, tidak menjalankan AI
- ✅ **Tidak ada commit spam** - Hanya commit jika ada perubahan
- ✅ **AI dapat berjalan terus-menerus** - Tanpa batas karena jalan di server sendiri
- ✅ **Hanya perubahan yang benar-benar di-commit** - Batch commit setiap 30 menit
- ✅ **Rate limit aman** - Maksimal 48 commit per hari (sangat aman)

## 🚀 Cara Kerja

1. **AI Worker** (jalan di server/laptop):
   - Generate summary setiap 30 menit
   - Menyimpan hasil ke `data/daily_summary.md`
   - Tidak langsung commit/push

2. **GitHub Actions** (jalan di GitHub):
   - Run setiap 30 menit
   - Cek apakah file `data/daily_summary.md` berubah
   - Jika berubah → commit sekali
   - Jika tidak berubah → skip (100% aman)

3. **GitHub Repo**:
   - Commit rapi dan terorganisir
   - History bersih dan jelas
   - Tidak kena limit

## 📁 Struktur Proyek

```
ai-daily-project/
│
├─ ai_worker/             ← Script AI di server/laptop
│   └─ generate.py
│
├─ data/
│   └─ daily_summary.md   ← hasil generate AI
│
├─ .github/
│   └─ workflows/
│       └─ auto-commit.yml
│
├─ requirements.txt
└─ README.md
```

## 🔧 Setup

### 1. Setup AI Worker (Server/Laptop)

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan AI worker
cd ai_worker
python generate.py
```

AI worker akan:
- Generate summary setiap 30 menit
- Menyimpan ke `data/daily_summary.md`
- Berjalan terus sampai dihentikan (Ctrl+C)

### 2. Setup GitHub Actions

GitHub Actions sudah dikonfigurasi di `.github/workflows/auto-commit.yml`.

**Tidak perlu setup tambahan!** Workflow akan:
- Otomatis run setiap 30 menit
- Commit jika ada perubahan
- Skip jika tidak ada perubahan

### 3. Kustomisasi AI Worker

Edit `ai_worker/generate.py` untuk:
- Mengganti model AI (LLM, API, dll)
- Mengubah format output
- Menyesuaikan interval waktu

**Contoh integrasi dengan AI:**

```python
# Contoh dengan OpenAI API
import openai

def generate_summary():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Generate daily summary"}]
    )
    summary = response.choices[0].message.content
    # ... save to file
```

## ⚙️ Konfigurasi

### Mengubah Interval Waktu

**AI Worker:**
```python
time.sleep(1800)  # 30 menit = 1800 detik
```

**GitHub Actions:**
```yaml
schedule:
  - cron: "*/30 * * * *"   # 30 menit
```

Format cron: `menit jam hari bulan hari-minggu`

### Mengubah Folder Output

Edit di `ai_worker/generate.py`:
```python
file_path = "../data/daily_summary.md"  # Ganti path sesuai kebutuhan
```

Edit di `.github/workflows/auto-commit.yml`:
```yaml
git add data/  # Ganti folder sesuai kebutuhan
```

## 🛡️ Keamanan & Limit

### Kenapa Sistem Ini Aman?

1. **GitHub Actions Limit:**
   - Workflow hanya 1-3 menit per run
   - Maksimal 48 commit/hari (sangat aman)
   - Tidak menjalankan AI berat di Actions

2. **Commit Strategy:**
   - Batch commit (1 kali per run)
   - Hanya commit jika ada perubahan
   - Tidak commit ribuan file

3. **AI Execution:**
   - AI jalan di server sendiri
   - Tidak terbatas oleh GitHub Actions
   - Bisa jalan 24/7 tanpa masalah

## 📊 Monitoring

Untuk melihat status:
- **AI Worker:** Cek console output
- **GitHub Actions:** Cek tab "Actions" di GitHub
- **Commits:** Cek commit history di GitHub

## 🔥 Variasi Proyek

Template ini bisa dikembangkan untuk:

- 🖼️ **AI Image Generator** - Generate gambar setiap X menit
- 💻 **AI Code Generator** - Generate code snippets
- 📊 **AI Dataset Generator** - Generate dataset training
- 🎓 **AI Model Trainer** - Auto train model dengan data baru

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

**Made with ❤️ for safe AI automation on GitHub**

