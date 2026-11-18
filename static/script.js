document.addEventListener('DOMContentLoaded', function() {
    // Kode untuk loading saat upload
    const formUpload = document.querySelector('form[action="/upload"]');
    if (formUpload) {
        formUpload.addEventListener('submit', function(e) {
            const fileInput = document.querySelector('input[type="file"]');
            if (fileInput.files.length > 0) {
                const btn = this.querySelector('.btn');
                btn.innerText = 'Mengupload...';
                btn.disabled = true;
            }
        });
    }
});

// Fungsi membuka Modal Edit
function editKategori(id, kategoriSaatIni) {
    const modal = document.getElementById('editModal');
    const form = document.getElementById('editForm');
    const select = document.getElementById('editKategoriSelect');
    
    // Set action form ke URL edit yang sesuai dengan ID
    form.action = '/edit/' + id;
    
    // Set pilihan dropdown sesuai dengan kategori saat ini
    select.value = kategoriSaatIni;
    
    // Tampilkan modal
    modal.style.display = 'flex';
}

// Fungsi menutup Modal Edit
function tutupModal() {
    document.getElementById('editModal').style.display = 'none';
}

// Menutup modal jika user klik di luar kotak modal
window.onclick = function(event) {
    const modal = document.getElementById('editModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}