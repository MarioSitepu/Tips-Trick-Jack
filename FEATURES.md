# 🎨 Fitur: Auto-Generate HTML/CSS Projects

## 📋 Deskripsi

Setiap kali AI Worker berjalan (setiap 30 menit), sistem akan:
1. ✅ Membuat folder baru dengan nama berdasarkan tanggal
2. ✅ Generate proyek HTML/CSS lengkap di dalam folder
3. ✅ Setiap folder berisi `index.html` dan `style.css`
4. ✅ GitHub Actions akan auto-commit folder baru ke repository

## 📁 Struktur Folder

```
projects/
│
├─ 2025-01-17-14-30/     ← Format: YYYY-MM-DD-HH-MM
│   ├─ index.html
│   └─ style.css
│
├─ 2025-01-17-15-00/     ← Generate berikutnya
│   ├─ index.html
│   └─ style.css
│
└─ 2025-01-17-15-30/     ← Dan seterusnya...
    ├─ index.html
    └─ style.css
```

## 🎯 Format Nama Folder

**Format:** `YYYY-MM-DD-HH-MM`

**Contoh:**
- `2025-01-17-14-30` → 17 Januari 2025, jam 14:30
- `2025-01-17-15-00` → 17 Januari 2025, jam 15:00
- `2025-01-18-09-15` → 18 Januari 2025, jam 09:15

## 📄 Isi Proyek

### index.html
- HTML5 structure lengkap
- Responsive design
- Modern layout dengan cards
- Informasi tentang proyek dan tanggal generate

### style.css
- Modern CSS styling
- Gradient background
- Card-based layout
- Hover effects
- Responsive untuk mobile

## 🔧 Kustomisasi

### Mengubah Template HTML/CSS

Edit fungsi `generate_html_css_project()` di:
- `ai_worker/generate.py` (console version)
- `ai_worker/generate_gui.py` (GUI version)

**Contoh kustomisasi:**
```python
def generate_html_css_project(self, project_dir, date_str):
    # Ganti template HTML sesuai kebutuhan
    html_content = f"""<!DOCTYPE html>
    <html>
    <!-- Template custom Anda -->
    </html>
    """
    
    # Ganti template CSS sesuai kebutuhan
    css_content = """/* CSS custom Anda */"""
    
    # ... rest of code
```

### Mengubah Format Nama Folder

Edit di fungsi `generate_summary()`:

```python
# Format saat ini: YYYY-MM-DD-HH-MM
project_folder_name = f"{date_str}-{time_str}"

# Contoh format lain:
# Hanya tanggal: project_folder_name = date_str  # 2025-01-17
# Dengan timestamp: project_folder_name = f"{date_str}-{now.strftime('%H%M%S')}"
```

## 📊 Statistik

Dengan generate setiap 30 menit:
- **Per hari:** ~48 folder/proyek
- **Per bulan:** ~1.440 folder/proyek
- **Per tahun:** ~17.520 folder/proyek

## 🚀 Cara Menggunakan Proyek

1. **Buka di Browser:**
   - Buka folder project (contoh: `projects/2025-01-17-14-30/`)
   - Double-click `index.html`
   - Atau drag & drop ke browser

2. **Edit Proyek:**
   - Edit `index.html` untuk mengubah konten
   - Edit `style.css` untuk mengubah styling
   - Bisa ditambahkan JavaScript jika perlu

3. **Deploy:**
   - Upload folder ke web hosting
   - Atau gunakan GitHub Pages
   - Atau deploy ke Netlify/Vercel

## 💡 Ide Pengembangan

Template HTML/CSS bisa dikembangkan untuk:
- 🎨 Portfolio pages
- 📝 Blog posts
- 🎯 Landing pages
- 📊 Dashboard templates
- 🎮 Game interfaces
- 📱 Mobile app mockups

## 🔄 Integrasi dengan AI

Template bisa di-generate dengan AI untuk:
- Konten yang lebih dinamis
- Styling yang lebih variatif
- Konten berdasarkan data eksternal
- Personalisasi berdasarkan tanggal/event

---

**Selamat membuat proyek HTML/CSS otomatis! 🎉**

