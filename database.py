import sqlite3

def init_db():
    # Membuat/menghubungkan ke database bernama 'arsip.db'
    conn = sqlite3.connect('arsip.db')
    cursor = conn.cursor()
    
    # Membuat tabel 'arsip' dengan query SQL
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arsip (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_file TEXT NOT NULL,
            kategori TEXT NOT NULL,
            tanggal_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database dan tabel berhasil dibuat!")

if __name__ == '__main__':
    init_db()