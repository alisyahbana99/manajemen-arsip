Website - Sistem Manajemen Arsip 

Proyek ini dibuat untuk memenuhi kebutuhan pengembangan aplikasi web dan sistem manajemen arsip.

## Fitur Utama (Full CRUD)
![Tampilan Aplikasi](screenshot.png)
* **Create:** Mengunggah file dokumen (PDF/Excel) dan menyimpannya ke database.
* **Read:** Menampilkan daftar arsip beserta kategori dan waktu unggah secara *real-time*.
* **Update:** Mengubah kategori arsip melalui *pop-up modal* yang interaktif.
* **Delete:** Menghapus data arsip dari database sekaligus menghapus file fisiknya dari server.

## Teknologi yang Digunakan
* **Backend:** Python (Flask)
* **Database:** SQL (SQLite)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript

## Cara Menjalankan Secara Lokal
1. Clone repository ini: `git clone https://github.com/alisyahbana99/manajemen-arsip.git`
2. Masuk ke folder: `cd manajemen-arsip`
3. Buat virtual environment: `python -m venv venv`
4. Aktifkan venv (Windows): `.\venv\Scripts\Activate.ps1`
5. Install Flask: `pip install Flask`
6. Buat database: `python database.py`
7. Jalankan aplikasi: `python app.py`
8. Buka `http://127.0.0.1:5000` di browser.
