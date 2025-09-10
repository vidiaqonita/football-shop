tautan ke aplikasi PWS: https://pbp.cs.ui.ac.id/web/project/vidia.qonita/footballshop
1. Implementasi checklist tugas 2:
   ✅ Membuat proyek django baru
   Step-by-step: 
   1. Membuat direktori proyek
   2. Mengaktifkan virtual environment dengan perintah `source env/bin/activate`
         (kalo belum install, gunakan perintah `python3 -m venv env` dulu)
   3. Membuat berkas requirements.txt untuk memuat dependencies (termasuk django)
   4. Gunakan perintah `pip install -r requirements.txt`. 
         Perintah ini akan menginstall dependencies yang sudah ditulis di requirements.txt
   5. Membuat proyek django dengan perintah `django-admin startproject football-shop .`.
   6. Mengatur konfigurasi environment untuk proyek
   ✅ Membuat aplikasi dengan nama 'main' pada proyek
   Step-by-step: 
   1. Pada direktori proyek, tulis perintah 'python manage.py startapp main'.
   2. Mendaftarkan aplikasi main ke proyek, dengan cara menambahkan 'main' pada INSTALLED_APPS di settings.py.
   ✅ Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
   Step-by-step: 
   1. Membuka berkas urls.py di football-shop.
   2. import include, untuk mengimpor pola rute URL dari aplikasi lain
   3. tulis:
       ```
           urlpatterns = [
        ...
        path('', include('main.urls')), # path akan diarahkan ke route dalam aplikasi main
        ...
       ]
       ```
   ✅ Membuat model pada aplikasi main dengan nama Product 
   Step-by-step:
   1. buka models.py dan namai class dengan Product.
   2. tulis CATEGORY_CHOICES berisi list kategori barang (bebas)
   3. tambahkan atribut-atribut wajib:
       ```
       id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # id barang (tidak wajib sih)
       name = models.CharField(max_length=255) # nama
       price = models.IntegerField(default=0) # harga
       description=models.TextField() # deskripsi produk
       thumbnail = models.URLField(blank=True, null=True) # thumbnail
       category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='new') # kategori dari list yang dibuat
       is_featured = models.BooleanField(default=False) # featured or not
       ```
   
   ✅ Membuat fungsi pada views.py untuk file html yang menunjukkan nama aplikasi, nama mahasiswa, dan kelas.
   Step-by-step: 
   1. buka views.py
   2. tulis:
     ```
     from django.urls import path
     from main.views import show_main # impor show_main yang dipanggil saat url cocok 
        
     app_name = 'main' #namespace unik URL aplikasi
        
     urlpatterns = [
     path('', show_main, name='show_main'), # route '' yang akan memanggil show_main
     ]
     ```
   ✅ Membuat routing pada urls.py di aplikasi main untuk memetakan fungsi yang sudah dibuat di views.py
   Step-by-step: 
   1. Membuat berkas urls.py pada aplikasi main.
   2. tulis:
     ```
     from django.urls import path
     from main.views import show_main
            
     app_name = 'main'
            
     urlpatterns = [
       path('', show_main, name='show_main'),
     ]
     ```
3. ![Screenshot dari https://python.plainenglish.io/the-mvt-design-pattern-of-django-8fd47c61f582](/football-shop/request_to_client_web.png)
   Penjelasan:
   - user mengirim request ke web
   - request masuk ke url dispatcher untuk dicocokkan ke path di views.py
   - jika cocok, request diarahkan ke path yang sesuai
   - views.py dapat mengambil data dari models.py atau menulisnya
   - setelah itu, views.py mengirimnya ke template untuk ditampilkan
   - template digunakan untuk membuat tampilan yang dilihat user 
   - setelah views.py mengirim data, template akan merender html 
- setelah menghasilkan html, hasil yang ditampilkan dikirim ke django sebagai **response**, dan user bisa melihat halaman tersebut
3. Peran settings.py dalam proyek django: 
    Sebagai konfigurasi utama aplikasi dan proyek. Pada settings.py, kita dapat mengatur:
    - apa saja aplikasi di dalam proyek (INSTALLED_APPS), 
    - keamanan akses (ALLOWED_HOSTS, SECRET_KEY DEBUG), 
    - konfigurasi database (DATABASES)
    - menyimpan middleware di MIDDLEWARE
4. Cara kerja migrasi database di django
    Misalkan kita mengatur atau mengubah isi models.py, maka kita harus melakukan migrasi
    Step-by-step:
    1. jalankan 'python manage.py makemigrations': menciptakan berkas migrasi perubahan model yang belum diaplikasikan ke database
    2. jalankan 'python manage.py migrate': mengaplikasikan perubahan berkas migrasi
    3. di django, ada django_migrations, yaitu tabel yang menyimpan catatan migrasi yang sudah dijalankan, termasuk yang sudah kita jalankan dengan 2 perintah di atas.
5. Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena:
    - punya struktur proyek yang sudah terorganisir (seperti MVT), memudahkan kita memahami konsep software development
    - semua yang diperlukan sudah ada dalam satu paket (library-library dasar sudah terinstall bersama django)
    - dokumentasi django ramah pemula dan detail, karena sudah banyak sekali developer menggunakannya. hal ini memudahkan pemula untuk belajar secara mandiri
    - menggunakan praktek yang baik, seperti keamanan dan environment, yang berguna untuk membangun proyek nyata di industri
6. Feedback untuk asisten dosen tutorial 1: Terima kasih sudah memberikan tutorial yang begitu detail dan jelas, sehingga memudahkan saya untuk belajar pbp dengan django dan menggunakan git



