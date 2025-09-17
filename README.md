tautan ke aplikasi PWS: https://pbp.cs.ui.ac.id/web/project/vidia.qonita/footballshop
1. Mengapa kita butuh data delivery dalam implementasi pengembangan platform:
    data delivery adalah proses memindahkan data dari tempat ia disimpan untuk disajikan atau ditempatkan ke tempat tujuan. dalam mengembangkan platform, tentu data delivery sangat penting, sebagai:
    - penghubung antara user dan inti platform: misalnya, user perlu melihat data-data penting yang tersimpan pada komputer. Tentu untuk mampu dilihat user butuh data delivery
    - User Interaction: dengan data delivery, data bisa diatur penyajiannya agar terlihat menarik dan cepat sesuai dengan kenyamanan user
    - data delivery yang efisien dapat menjaga sistem server agar tidak crash atau. melambat saat jumlah user bertambah banyak
    - dengan data delivery, kita bisa menjaga keamanan sistem dengan membatasi akses global user untuk data-data personal 
    - data delivery juga dapat membuat antar platform atau aplikasi terhubung, memudahkan user saat menggunakan beberapa aplikasi sekaligus
2. Menurut saya, mana yang lebih baik antara XML dan JSON + mengapa JSON lebih populer dibandingkan XML:
    Saya lebih memilih JSON. Alasan: 
        lebih mudah dibaca. format JSON disusun seperti dictionary di Java, membuat saya pribadi lebih mudah mengenali dan membacanya. sedangkan, XML juga lebih sulit untuk ditulis dan tampilan web dengan link JSON lebih gampang dibaca daripada tampilan XML. 
    Mengapa JSON lebih populer dibandingkan XML?
        JSON berasal dari JavaScript, yang mendominasi pengembangan frontend, sehingga lebih mudah untuk dipelajari para developer dan banyak digunakan untuk aplikasi web dan mobile. JSON juga lebih efisien untuk parsing ke bahasa pemrograman, karena ukuran data yang lebih kecil. formatnya juga lebih simpel sehingga mudah dimengerti oleh developer.
3. Fungsi dari method is_valid() pada form django + mengapa kita butuh fungsi tersebut:
    tujuannya untuk memastikan validasi input pada form. saat input tidak valid (misalnya kosong di beberapa input), form akan return False dan muncul error. jika valid, form return True.
    mengapa kita butuh fungsi tersebut? 
    - untuk menjaga keamanan data. jika is_valid() return false, form bisa menggunakan clean() untuk mengosongi input sehingga keamanan data terjaga.
    - menunjukkan pesan error saat input tidak valid, untuk memastikan user menaruh input yang valid
    - memastikan input yang masuk adalah input sesuai format yang developer buat di form
4. Mengapa kita butuh csrf_token saat membuat form django + apa yang terjadi jika csrf_token tidak ditambahkan + bagaimana hal tersebut dapat dimanfaatkan oleh penyerang:
    kita butuh csrf_token saat membuat form django untuk:
    - melindungi aplikasi dari csrf attack, yaitu serangan yang membuat user mengirim request tanpa sepengetahuan mereka. csrf_token merupakan token unik yang dibuat server untuk tiap sesi user. developer menambahkannya pada form di template. saat user submit form, csrf_token dikirim bersamaan. jika cocok, permintaan diterima. namun jika tidak, akan return 403 forbidden 
    jika csrf_token tidask ditambahkan:
    - django akan menolak request dan data tidak diproses
    bagaimana penyerang memanfaatkan tidak adanya csrf_token:
    misalnya, penyerang menaruh form tersembunyi pada website yang sedang dibuka oleh pengguna. saat cookie session pengguna aktif, pengguna meng-klik link form tersebut. ini membuat pengguna melakukan request tanpa ia ketahui. jika semisal situs yang ia buka adalah situs bank dan situs itu tidak punya csrf_token, maka apa yang dilakukan dengan menekan link tersebut bisa dimanipulasi oleh penyerang, misal transfer uang sedangkan situs bank tidak mengenali pengguna asli dan menerima request tersebut.
5. Implementasi checklist tugas 3:
   ✅ Menambah 4 fungsi baru pada views untuk tampilan XML, JSON, XML by Id, dan JSON by Id
   Step-by-step: 
   1. pada views.py, import HttpResponse dan Serielizers
   2. definisikan 4 fungsi tersebut. isinya harus memuat:
   - menerima parameter request
   - inisiasi data hasil query yang diserialisasikan (berparameter product_list)
   - return function berupa HttpResponse yang parameter content_type nya sesuai fungsi (application/xml, application/json)
   - untuk show by Id, gunakan try except untuk exception saat id tidak ditemukan
   kode fungsi:
        ```
        def show_xml(request):
            product_list = Product.objects.all()
            xml_data = serializers.serialize("xml", product_list)
            return HttpResponse(xml_data, content_type="application/xml")

        def show_json(request):
            product_list = Product.objects.all()
            json_data = serializers.serialize("json", product_list)
            return HttpResponse(json_data, content_type="application/json")

        def show_xml_by_id(request, product_id):
        try:
            product_item = Product.objects.filter(pk=product_id)
            xml_data = serializers.serialize("xml", product_item)
            return HttpResponse(xml_data, content_type="application/xml")
        except Product.DoesNotExist:
            return HttpResponse(status=404)
        def show_json_by_id(request, product_id):
        try:
            product_item = Product.objects.get(pk=product_id)
            json_data = serializers.serialize("json", [product_item])
            return HttpResponse(json_data, content_type="application/json")
        except Product.DoesNotExist:
            return HttpResponse(status=404)
        ```
   ✅ Buat routing URL untuk masing-masing views pada poin 1
   Step-by-step: 
   1. ke urls.py dan import fungsi-fungsi yang sudah dibuat
    ```
        from main.views import  ..., show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
   2. tambah path ke urlpatterns untuk akses fungsi-fungsi tersebut.
    ```
        urlpatterns = [
        ...
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
        ]
    ```
   ✅ Buat tombol "Add" yang redirect ke form page + tombol "Detail" yang dapat menampilkan detail objek
   Step-by-step: 
   1. dalam blok kode main.html, tambahkan kode untuk membuat button "Add" yang akan redirect ke form page
    ```
        ...
        <!-- ini kode untuk redirect ke halaman form page untuk menambah produk -->
        <a href="{% url 'main:create_product' %}">
        <!-- ini untuk menambah button Add -->
        <button>+ Add Product</button>
        </a>
        ...
    ```
    2. untuk menambahkan button "Detail", tulis kode berikut
    ```
        ...
        <div>
        <!-- ini kode untuk redirect ke halaman detail produk -->
        <h2><a href="{% url 'main:show_product' product.id %}">{{ product.name }}</a></h2>

        <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
            <b>Featured</b>{% endif %}</p>

        {% if product.thumbnail %}
        <img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100">
        <br />
        {% endif %}

        <p>{{ product.content|truncatewords:25 }}...</p>
        <!-- ini kode untuk memasang button detail -->
        <p><a href="{% url 'main:show_product' product.id %}"><button>Detail</button></a></p>
        </div>
        ...
    ```
   ✅ Membuat form page untuk menambahkan objek model
   Step-by-step:
   1. 
   ✅ Membuat halaman yang menampilkan detail objek
   Step-by-step: 
   1. tentu saja kita harus punya model di models.py
   2. buat forms.py di main. import Product dari main.models
   3. definisikan model berupa Product dan array fields, yang akan menjadi field form
    ```
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "category", "thumbnail", "description", "is_featured"]
        
    ```
    4. membuat view untuk form page. di views.py, buat fungsi create_product() untuk menampilkan halaman form.
    5. untuk tampilan halaman form, buat pada main/templates/create_product.html
    pada create_product.html:
    ```
    {% extends 'base.html' %}
    {% block content %}
    <h1>Add Product</h1>

    <form method="POST"> // membuat form html
    {% csrf_token %} // csrf_token sebagai security
    <table>
        {{ form.as_table }} // menampilkan fields dari forms.py sebagai tabel
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add PRODUCT" /> // tombol kirim form
        </td>
        </tr>
    </table>
    </form>

    {% endblock content %}

    ```
    pada views.py: 
    ```
    from django.shortcuts import render, redirect, get_object_or_404
    from main.forms import ProductForm
    from main.models import Product

    ...
    // ini adalah fungsi untuk form page
    def create_product(request): 
        form = ProductForm(request.POST or None)
        // is_valid() untuk menyaring input yang tidak valid
        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main') 

        context = {'form': form}
        return render(request, "create_product.html", context)

    ...
    ```
6. Feedback untuk asisten dosen tutorial 2: Terima kasih sudah memberikan tutorial yang begitu detail dan jelas, sehingga memudahkan saya untuk mengimplementasikan data delivery dengan mudah dan membuat form page, serta menambahkan button dan menampilkan halaman detail produk.





