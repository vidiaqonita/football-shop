"----- TUGAS 5 -----"
✅ Implementasikan fungsi untuk menghapus dan mengedit product.
Step-by-step:
    
✅ Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
- Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
- Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
    ✅ Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
        Step-by-step:
            1. 
    ✅ Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
    ✅ Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
    ✅ Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
Step-by-step:
    1. 
✅ 
Step-by-step:
    1.
✅ 
Step-by-step:
    1. 
Pertanyaan tambahan:
    1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    - Inline style (style="..." di HTML) → Prioritas tertinggi.
    - ID selector (#id) → Prioritas tinggi.
    - Class selector (.class), attribute selector ([attr=value]), dan pseudo-class (:hover) → Prioritas sedang.
    - Element selector (div, p, h1, dll.) dan pseudo-element (::before, ::after) → Prioritas rendah.
    - Universal selector (*) → Prioritas paling rendah.
    2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
    - Pengalaman pengguna lebih baik → Tidak perlu zoom atau scroll horizontal.
    - SEO lebih baik → Google lebih memprioritaskan website yang mobile-friendly.
    - Efisiensi pengembangan → Tidak perlu membuat versi terpisah untuk mobile.o
    Contoh yang sudah pakai: Youtube, Instagram, dll.
    Contoh yang belum pakai: aplikasi yang tampilannya belum ada untuk di mobile, membuat pengguna tidak betah menggunakannya.
    3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    - Margin: Ruang di luar elemen, memisahkan elemen dari elemen lain.
    - Border: Garis tepi yang membungkus konten + padding elemen.
    - Padding: Ruang di dalam elemen, antara konten dan border.
    4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    - Flexbox: Layout model yang memudahkan pengaturan elemen dalam satu dimensi (baris atau kolom). Fleksibel, cocok untuk layout sederhana seperti navbar, card list, atau form.
    - Grid: Layout model yang mengatur elemen dalam dua dimensi (baris dan kolom). Cocok untuk layout kompleks seperti dashboard, website dengan banyak section.

"===== TUGAS 6 ====="
✅ Apa perbedaan antara synchronous request dan asynchronous request?
    synchronous request akan blokir browser sampai muncul response (maka user harus melihat browser yang terhenti prosesnya hingga response), sedangkan asynchronous request akan membiarkan halaman terus diproses selama menunggu response, sehingga pada user experience nya tidak terhenti dan halaman tetap responsif.
✅ Bagaimana AJAX bekerja di Django (alur request–response)?
    - Browser (JavaScript) mengirim request ke URL Django menggunakan AJAX (seperti fetch() atau $.ajax()).
    - Django URLConf (urls.py) menerima request dan meneruskannya ke view terkait.
    - View Django memproses data dan mengembalikan JSON response.
    - JavaScript di browser menerima JSON tersebut dan memperbarui tampilan halaman tanpa reload.
✅ Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
    Keuntungan: 
    - Tidak perlu reload seluruh halaman saat request, cukup ambil dan ubah data yang diperlukan saja
    - Responsif dan interaktif, tidak selama render biasa.
    - secara User Experience, halaman berjalan dengan lebih smooth dan tidak kelihatan reload
    - Tidak perlu kirim semua data HTML setiap request, cukup kirim data JSON yang kecil.
✅ Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
    - Mengunakan csrf token, dengan menulis kode keamanannya di header AJAX request
    - Menggunakan https, agar data username/password tidak dikirim dalam bentuk plaintext
    - validasi input di server
    - Pastikan kirim password melalui koneksi aman seperti django.contrib.auth.authenticate agar tidak terkirim dalam plaintext
✅ Bagaimana AJAX mempengaruhi User Experience (UX) pada website?
    - tidak perlu reload halaman sehingga interaksi terasa cepat (user experience yang baik)
    - feedback langsung
    - SPA-like experience (mirip aplikasi)
    - cocok untuk fitur realtime, seperti chat dan notifikasi
    - hati-hati, bila tidak diimplementasikan dengan baik, bisa membuat pengguna bingung. selain itu, terlalu banyak AJAX request bisa membebani server