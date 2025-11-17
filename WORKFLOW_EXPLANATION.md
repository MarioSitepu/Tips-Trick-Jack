# 🔄 Alur Kerja Sistem - Penjelasan Lengkap

## ⚠️ PENTING: EXE Tidak Langsung Auto Commit & Push!

### Alur Kerja Saat Ini:

```
┌─────────────────────────────────────────────────────────┐
│  LOKAL (EXE/Python Script)                              │
│                                                          │
│  1. EXE berjalan di laptop/PC                           │
│  2. Generate HTML/CSS setiap 30 menit                   │
│  3. Simpan ke folder: projects/YYYY-MM-DD-HH-MM/       │
│  4. File hanya ada di LOKAL (belum di GitHub)          │
│                                                          │
└──────────────────┬──────────────────────────────────────┘
                   │
                   │ File perlu di-push manual ke GitHub
                   │ (sekali saja untuk setup awal)
                   ▼
┌─────────────────────────────────────────────────────────┐
│  GITHUB REPOSITORY                                      │
│                                                          │
│  File sudah ada di GitHub (setelah push manual)         │
│                                                          │
└──────────────────┬──────────────────────────────────────┘
                   │
                   │ GitHub Actions monitor perubahan
                   ▼
┌─────────────────────────────────────────────────────────┐
│  GITHUB ACTIONS (Cloud)                                 │
│                                                          │
│  1. Run setiap 30 menit                                 │
│  2. Cek perubahan di folder projects/                   │
│  3. Jika ada perubahan → Commit & Push                  │
│  4. Jika tidak ada → Skip                               │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 Dua Skenario Penggunaan

### Skenario 1: EXE di Repository Lokal (Recommended)

**Setup:**
1. Clone repository ke laptop/PC
2. Run EXE di folder repository
3. EXE generate file di `projects/` (di dalam repo)
4. Push manual sekali ke GitHub
5. Setelah itu, GitHub Actions akan auto commit & push perubahan

**Alur:**
```
Lokal: EXE generate → File di projects/ → Push manual (sekali)
GitHub: File sudah ada → GitHub Actions monitor → Auto commit & push perubahan
```

---

### Skenario 2: EXE Standalone (Tidak di Repository)

**Masalah:**
- EXE generate file di folder terpisah
- File tidak otomatis masuk ke GitHub
- Perlu manual copy/push setiap kali

**Solusi:**
- Copy file ke repository lokal
- Atau setup auto-sync (perlu tambahan script)

---

## ✅ Cara Setup yang Benar

### Step 1: Clone Repository

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

### Step 2: Run EXE di Folder Repository

```bash
# Pastikan EXE ada di folder repository
AI-Daily-Summary.exe
```

EXE akan generate file di:
- `projects/YYYY-MM-DD-HH-MM/index.html`
- `projects/YYYY-MM-DD-HH-MM/style.css`

### Step 3: Push Manual (Sekali Saja)

```bash
git add projects/
git commit -m "Initial projects"
git push
```

### Step 4: Setelah Itu Otomatis!

Setelah file pertama di-push:
- GitHub Actions akan monitor folder `projects/`
- Jika EXE generate file baru → GitHub Actions akan auto commit & push
- **TIDAK perlu push manual lagi!**

---

## 🔄 Alur Lengkap Setelah Setup

```
1. EXE generate file baru di lokal
   └─> projects/2025-11-17-21-00/index.html
   └─> projects/2025-11-17-21-00/style.css

2. File ada di lokal (belum di GitHub)

3. GitHub Actions run (setiap 30 menit)
   └─> Checkout repository
   └─> Cek perubahan di projects/
   └─> TIDAK ada perubahan (file belum di-push)

4. User push manual (sekali):
   └─> git add projects/
   └─> git commit -m "..."
   └─> git push

5. File sekarang ada di GitHub

6. GitHub Actions run berikutnya:
   └─> Cek perubahan
   └─> Ada perubahan baru → Commit & Push otomatis!
```

---

## 💡 Rekomendasi

**Untuk Auto Commit & Push Penuh:**

1. **Jalankan EXE di folder repository yang sudah di-clone**
2. **Push manual sekali** untuk sync file pertama
3. **Setelah itu otomatis** - GitHub Actions akan handle commit & push

**Atau:**

Tambahkan fitur auto-push di EXE (perlu tambahan code untuk git push dari EXE)

---

## ❓ FAQ

**Q: Apakah EXE bisa langsung commit & push?**
A: Tidak, EXE hanya generate file. GitHub Actions yang commit & push.

**Q: Apakah perlu push manual setiap kali?**
A: Tidak, hanya sekali untuk setup awal. Setelah itu GitHub Actions akan auto commit & push.

**Q: Bagaimana cara sync file lokal ke GitHub?**
A: Push manual sekali, atau jalankan EXE di folder repository yang sudah di-clone.

---

**Kesimpulan: EXE generate file lokal → Push manual sekali → GitHub Actions auto commit & push selanjutnya! 🎉**

