"----- TUGAS 4 -----"
✅ Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
Step-by-step:
    - fungsi registrasi
        1. import UserCreationForm dan messages pada views.py
        2. Tambahkan fungsi register() pada views.py. Di dalamnya, request dikirim dengan method POST yang harus digunakan jika ingin mengirim data sensitif
            ```
            def register(request):
                form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
            ```
        3. tambahkan file register.html pada template dan isi dengan kode yang menampilkan halaman register. Tidak lupa memuat form method POST dan csrf token.
    - fungsi login
        1. tambahkan import AuthenticationForm, authenticate, dan login pada views.py
        2. Tambahkan fungsi login_user() pada views.py. Jika request method adalah POST, ia akan membuat form autentikasi. Jika valid, redirect ke halaman main. lalu, tampilkan juga halaman login dari login.html 
            ```
            def login_user(request):
            if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)

                if form.is_valid():
                        user = form.get_user()
                        login(request, user)
                        response = HttpResponseRedirect(reverse("main:show_main"))
                        response.set_cookie('last_login', str(datetime.datetime.now()))
                        return response

            else:
                form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, 'login.html', context)
            ```
        3. tambahkan file login.html pada template dan isi dengan kode yang menampilkan halaman login. Tidak lupa memuat form method POST dan csrf token.
        4. import login_user pada urls.py dan tambahkan path url nya ke dalam urlpatterns.
    - fungsi logout
        1. tambahkan import logout pada views.py
        2. Tambahkan fungsi logout_user() pada views.py. fungsi ini akan memproses request logout dan kembali ke halaman login.
            ```
            def logout_user(request):
                logout(request)
                response = HttpResponseRedirect(reverse('main:login'))
                response.delete_cookie('last_login')
                return response
            ```
        3. masukkan button logout yang melakukan logout pada main.html
        4. import logout_user pada urls.py dan tambahkan path url nya ke dalam urlpatterns.
✅ Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal
Step-by-step:
    1. jalankan python manage.py shell (kita akan membuat akun dari lokal dengan shell)
    2. tulis kode berikut: 
    ```
    from django.contrib.auth.models import User
    from main.models import Product   

    # Buat 2 akun
    user1 = User.objects.create_user(username='user1', password='password123')
    user2 = User.objects.create_user(username='user2', password='password456')

    # Buat 3 dummy data untuk user1
    Product.objects.create(user=user1, name='bola', price=100000, description='bola')
    Product.objects.create(user=user1, name='bola', price=300000, description='sepatu')
    Product.objects.create(user=user1, name='bola', price=50000, description='baju')

    # Buat 3 dummy data untuk user2
    Product.objects.create(user=user2, name='bola', price=110000, description='bola')
    Product.objects.create(user=user2, name='bola', price=400000, description='sepatu')
    Product.objects.create(user=user2, name='bola', price=60000, description='baju')

    ```
    3. cek apakah data sudah terdaftar dari lokal dengan tulis di shell: 
    ```
    User.objects.all()
    Product.objects.all()
    ```
✅ Menghubungkan model Product dengan User.
Step-by-step:
    1. Pada file models.py, import User
    2. masukkan kode berikut di dalam class Product
    ```
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ```
    fungsi kode tersebut untuk menghubungkan user dengan product, sehingga tiap product terasosiasi dengan suatu user
    3. migrasi model (karena sudah ada perubahan) dengan 
    ```
    python manage.py makemigrations # untuk membuat migrasi
    python manage.py migrate # untuk migrasi
    ```
✅ Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
Step-by-step:
    1. tambahkan @login_required(login_url='/login') pada show_product dan show_main pada views.py
    2. pada main.html, ganti { name } dengan { user } sehingga akan menampilkan nama user yang sedang login pada main page.
    3. tambahkan pula import datetime HttpResponseRedirect, dan reverse. Lalu set kode dalam login_user yang akan menyimpan cookie baru bernama last_login
    ```
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ```
Pertanyaan tambahan:
    1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    - Django AuthenticationForm adalah form bawaan dari django yang dipakai untuk proses login. Form ini sudah menyediakan field username dan password, serta melakukan proses validasi pengguna.
    - Kelebihan: 
        - praktis, sehingga developer tidak perlu menulis form untuk autentikasi dari scratch
        - terintegrasi, karena langsung terhubung dengan sistem django
        - aman secara default 
    - Kekurangan:
        - kurang fleksibel untuk jenis autentikasi tambahan. misal ingin menambah 2FA, maka harus dikustomisasi
        - tampilan yang standar dan masih perlu disesuaikan dengan kebutuhan UI/UX
    2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    - Autentikasi: Proses memverifikasi indentitas pengguna. contoh: login dengan username dan password
    - Otorasisasi: Proses memverifikasi user terautentikasi yang akan diberi akses tertentu. contoh: verifikasi admin untuk mengakses halaman tertentu
    3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    - Cookies: 
        - kelebihan: 
            - bisa digunakan langsung tanpa server-side (dari client-side)
            - ringan untuk menyimpan data yang lebih kecil 
        - kekurangan:  
            - lebih mudah dimanipulasi (terutama jika tanpa csrf token)
            - tidak cocok untuk data sensitif
            - ukuran terbatas
    - Session: 
        - kelebihan: 
            - disimpan di sisi server sehingga lebih aman
            - bisa menyimpan data lebih banyak
            - user hanya pegang session ID
        - kekurangan: 
            - membebani server karena data session harus dikelola di server
            - mekanisme pembersihan yang lama
    4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    - tidak sepenuhnya aman. beberapa resiko (penggunaan cookies secara default) antara lain: 
        - cookie session bisa dicuri (XSS) dan bisa seolah-olah pencuri merupakan user
        - cookie bisa dimanipulasi
        - jika cookie dikirim lewat http biasa dan tidak dienkripsi, bisa dicuri
    - cara django menanganinya:
        - menggunakan csrf token, yaitu membuat token unik untuk setiap user login yang punya data sensitif. csrf token tidak sama setiap user sudah logout. selain itu, dengan csrf token, server tahu apakah yang melakukan request user dari browser yang sama atau bukan karena mencocokkan token dari request tersebut.
        - menggunakan cookie session terenkripsi.

"----- TUGAS 6 -----"
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