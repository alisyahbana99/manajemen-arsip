import os
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'rahasia_super_aman' # Dibutuhkan untuk pesan flash

# Konfigurasi folder upload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Pastikan folder uploads ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Fungsi untuk koneksi ke database
def get_db_connection():
    conn = sqlite3.connect('arsip.db')
    conn.row_factory = sqlite3.Row # Agar data bisa diakses seperti dictionary
    return conn

# Halaman Utama (Menampilkan data)
@app.route('/')
def index():
    conn = get_db_connection()
    # Query SQL untuk mengambil semua data arsip, urutkan dari yang terbaru
    arsip_list = conn.execute('SELECT * FROM arsip ORDER BY tanggal_upload DESC').fetchall()
    conn.close()
    return render_template('index.html', arsip_list=arsip_list)

# Proses Upload File
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('Tidak ada file yang dipilih')
        return redirect(url_for('index'))
    
    file = request.files['file']
    kategori = request.form.get('kategori')
    
    if file.filename == '':
        flash('Nama file kosong')
        return redirect(url_for('index'))
    
    if file:
        # Amankan nama file
        filename = secure_filename(file.filename)
        # Simpan file fisik ke folder uploads
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Simpan nama file dan kategori ke Database SQL
        conn = get_db_connection()
        conn.execute('INSERT INTO arsip (nama_file, kategori) VALUES (?, ?)', (filename, kategori))
        conn.commit()
        conn.close()
        
        flash('File berhasil diunggah!')
        return redirect(url_for('index'))
# --- FITUR DELETE (HAPUS) ---
@app.route('/delete/<int:id>', methods=['POST'])
def delete_arsip(id):
    conn = get_db_connection()
    # 1. Cari nama file berdasarkan ID
    arsip = conn.execute('SELECT nama_file FROM arsip WHERE id = ?', (id,)).fetchone()
    
    if arsip:
        nama_file = arsip['nama_file']
        # 2. Hapus file fisik dari folder uploads
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], nama_file)
        if os.path.exists(file_path):
            os.remove(file_path)
            
        # 3. Hapus data dari database
        conn.execute('DELETE FROM arsip WHERE id = ?', (id,))
        conn.commit()
        flash('Arsip berhasil dihapus!')
        
    conn.close()
    return redirect(url_for('index'))

# --- FITUR UPDATE (EDIT KATEGORI) ---
@app.route('/edit/<int:id>', methods=['POST'])
def edit_arsip(id):
    kategori_baru = request.form.get('kategori')
    if kategori_baru:
        conn = get_db_connection()
        # Update kategori di database berdasarkan ID
        conn.execute('UPDATE arsip SET kategori = ? WHERE id = ?', (kategori_baru, id))
        conn.commit()
        conn.close()
        flash('Kategori arsip berhasil diperbarui!')
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)