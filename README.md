Link aplikasi: http://andreas-timothy-tokotokoan.pbp.cs.ui.ac.id/

# Tugas 6

## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

Penggunaan JavaScript dalam pengembangan aplikasi web bermanfaat dalam menambah interaktivitas dan dinamisme pada halaman web, seperti animasi, validasi form, event handling, manipulasi DOM, asynchronous programming, dll.

## Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

`await` digunakan untuk menunggu hasil dari promise yang dihasilkan oleh `fetch()` sebelum melanjutkan eksekusi kode berikutnya. Jika kita tidak menggunakan `await`, `fetch()` akan menghasilkan data yang tidak sesuai.

## Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?

Karena jika menggunakan AJAX untuk mengirim `POST` request, CSRF token tidak akan disertakan secara otomatis karena AJAX request dilakukan di latar belakang dan tidak secara otomatis dihubungkan dengan mekanisme CSRF form. Jika CSRF token tidak disertakan dalam permintaan POST melalui AJAX, Django akan menolak request tersebut dengan mengembalikan 403 Forbidden error sebagai respon karena sistem keamanan CSRF mendeteksi bahwa tidak ada token valid yang diterima. Oleh karena itu, kita perlu menggunakan decorator `csrf_exempt` agar Django mengabaikan keberadaan CSRF token.

## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Pembersihan data input perlu dilakukan di backend untuk melindungi database dari data input yang berbahaya. Hal ini tidak cukup dilakukan di frontend saja karena pengguna/penyerang dapat menggunakan tools seperti postman untuk membuat request ke backend secara langsung tanpa melalui frontend.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Menambahkan fungsi `refreshProducts()` pada `main.html` untuk melakukan `GET` request menggunakan AJAX.
2. Menambahkan modal dan fungsi `addProduct()` pada `main.html` untuk melakukan `POST` request menggunakan AJAX.
3. Menambahkan fungsi berikut pada `views.py` untuk menambah product ke database.

   ```python
   @csrf_exempt
   @require_POST
   def add_product_ajax(request):
     name = strip_tags(request.POST.get("name"))
     price = request.POST.get("price")
     description = strip_tags(request.POST.get("description"))
     user = request.user

     new_product = Product(
         name=name, price=price,
         description=description,
         user=user
     )
     new_product.save()

     return HttpResponse(b"CREATED", status=201)
   ```

4. Menambahkan baris berikut pada `urls.py` untuk mengarahkan path `create-ajax/` ke fungsi view yang baru dibuat.
   ```python
   path('create-ajax/', add_product_ajax, name='add_product_ajax')
   ```
5. Menambahkan baris berikut di dalam tag `<script>` pada `main.html` untuk menghubungkan form pada modal ke path `create-ajax/`.
   ```javascript
   document.getElementById("productForm").addEventListener("submit", (e) => {
     e.preventDefault();
     addProduct();
   });
   ```

# Tugas 5

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas pengambilan CSS selector dilakukan berdasarkan spesifisitas yang dihitung dengan cara berikut.

- Elemen tag/selector tipe (p, div, h1, dll.): Memiliki spesifisitas paling rendah.
- Class selector, pseudo-class (.class-name, :hover, :focus, dll.): Spesifisitas sedang.
- ID selector (#id-name): Spesifisitas lebih tinggi.
- Inline style (style yang langsung diberikan di atribut elemen HTML): Spesifisitas tertinggi.
- Aturan !important: Aturan !important akan mengalahkan semua selektor lain, tanpa memperhatikan spesifisitas.

Spesifisitas dihitung menggunakan format angka berbentuk (a, b, c, d), di mana:

- a = 1 jika ada aturan !important, jika tidak a = 0.
- b = jumlah ID selector.
- c = jumlah class selector, pseudo-class (:hover, :active, dll.), atau attribute selector ([type="text"], dll.).
- d = jumlah tag selector atau pseudo-element (::before, ::after, dll.).

Semakin tinggi nilai (a, b, c, d), semakin besar spesifisitasnya. Jika dua selector memiliki spesifisitas yang sama, browser akan menggunakan aturan cascade, yaitu memilih aturan yang ditulis terakhir.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design penting dalam pengembangan aplikasi web untuk meningkatkan aksesibilitas dan pengalaman pengguna. Dengan responsive design, sebuah aplikasi web akan menjadi lebih aksesibel dan nyaman digunakan di berbagai perangkat dan ukuran layar. Contoh aplikasi yang sudah menerapkan responsive design adalah [YouTube](http://www.youtube.com/), sedangkan contoh yang belum menerapkan responsive design adalah [Arngren.net](http://www.arngren.net/).

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

- Margin adalah ruang kosong di luar batas elemen (border). Ini digunakan untuk memberi jarak antara elemen yang satu dengan elemen lainnya. Ada 3 cara menggunakan margin:
  1. Margin individual
     ```css
     div {
       margin-top: 20px;
       margin-right: 15px;
       margin-bottom: 20px;
       margin-left: 15px;
     }
     ```
  2. Margin shorthand (urutannya: top, right, bottom, left)
     ```css
     div {
       margin: 20px 15px 20px 15px;
     }
     ```
  3. Margin seragam (semua sisi sama)
     ```css
     div {
       margin: 10px;
     }
     ```
- Border adalah garis atau bingkai yang berada di antara margin dan padding. Border mengelilingi konten dan padding elemen, serta bisa diatur tampilannya (warna, ketebalan, gaya). Ada 2 cara menggunakan border:
  1. Border individual
     ```css
     div {
       border-top: 2px solid red;
       border-right: 1px dashed blue;
       border-bottom: 3px dotted green;
       border-left: 4px solid black;
     }
     ```
  2. Border shorthand
     ```css
     div {
       border: 2px solid black;
     }
     ```
- Padding adalah ruang kosong di dalam border elemen yang memisahkan konten dari batas elemen (border). Padding berada di antara konten dan border elemen. Ada 3 cara menggunakan padding:
  1. Padding individual
     ```css
     div {
       padding-top: 20px;
       padding-right: 15px;
       padding-bottom: 20px;
       padding-left: 15px;
     }
     ```
  2. Padding shorthand (urutannya: top, right, bottom, left)
     ```css
     div {
       padding: 20px 15px 20px 15px;
     }
     ```
  3. Padding seragam (semua sisi sama)
     ```css
     div {
       padding: 10px;
     }
     ```

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox adalah model layout one-dimensional yang dirancang untuk mengatur elemen di satu arah, yaitu horizontal (baris) atau vertikal (kolom). Flexbox memungkinkan elemen-elemen untuk menyesuaikan ukuran dan letaknya berdasarkan ruang yang tersedia dalam container untuk membuat tata letak yang fleksibel dan responsif.

Grid Layout adalah model layout two-dimensional yang lebih canggih daripada Flexbox. Grid memungkinkan kita untuk menyusun elemen dalam baris dan kolom secara bersamaan sehingga memungkinkan tata letak yang lebih kompleks seperti layout majalah, dashboard, atau halaman e-commerce.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Untuk menghapus dan mengedit product, tambahkan 2 fungsi berikut pada views.

   ```python
   def edit_product(request, id):
     product = Product.objects.get(pk = id)

     form = ProductForm(request.POST or None, instance=product)

     if form.is_valid() and request.method == "POST":
         form.save()
         return HttpResponseRedirect(reverse('main:show_main'))

     context = {'form': form}
     return render(request, "edit_product.html", context)

   def delete_product(request, id):
     product = Product.objects.get(pk = id)
     product.delete()
     return HttpResponseRedirect(reverse('main:show_main'))
   ```

   Kedua fungsi tersebut akan menghandle logic dalam menghapus dan mengedit product. Kita juga perlu membuat routing untuk kedua fungsi tersebut dengan menambahkan baris berikut pada `urls.py`.

   ```python
   path('edit-product/<uuid:id>', edit_product, name='edit_product'),
   path('delete/<uuid:id>', delete_product, name='delete_product')
   ```

   Lalu, kita perlu menambahkan button pada html template untuk mengedit dan menghapus product. Untuk mengedit, kita juga memerlukan sebuah form yang berisi data product yang akan diedit.

2. Untuk mengkustomisasi halaman agar lebih menarik dan responsive, kita dapat menggunakan tailwindcss dengan cara menambahkan baris berikut di dalam tag `head` pada `base.html`.

   ```html
   <script src="https://cdn.tailwindcss.com"></script>
   ```

   Setelah itu, kita tinggal menambahkan class-class tailwind di setiap elemen html yang ingin kita kustomisasi sesuai keinginan.

3. Untuk membuat tombol edit dan hapus pada card product, kita dapat menggunakan svg untuk menampilkan icon dan membungkus svg tersebut ke dalam tag `a` untuk mengarahkan ke url yang sesuai.

4. Untuk membuat navbar yang responsive, kita dapat memanfaatkan breakpoints pada tailwind untuk menampilkan seluruh item pada navbar jika lebar layar melebihi ukuran tertentu. Tetapi jika lebar layar kurang dari ukuran tersebut, seluruh item tadi akan disembunyikan dan hanya menampilkan mobile menu. Lalu kita dapat menggunakan javascript untuk menampilkan dan menyembunyikan item pada navbar ketika mobile menu diklik.

# Tugas 4

## Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`

`HttpResponseRedirect()` hanya dapat menerima url sebagai argumen, sedangkan `redirect()` dapat menerima url, nama view, ataupun model sebagai argumennya.

## Jelaskan cara kerja penghubungan model `Product` dengan `User`!

Kita menghubungkan model `Product` dengan `User` dengan menambahkan baris berikut pada model `Product`.

```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Baris ini memberitahu Django bahwa `Product` akan memiliki field `user` yang menyimpan foreign key terhadap record pada model `User`, alias `user` akan berisi id dari sebuah user yang mengindikasikan bahwa product tersebut adalah milik user yang didefinisikan tersebut.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah proses memverifikasi kebenaran dari credential yang diberikan user, sedangkan authorization adalah proses memverifikasi hak akses yang dimiliki user. Ketika seorang pengguna melakukan login, Django akan memverifikasi kecocokan dari username dan password yang diberikan. Proses ini disebut authentication. Django melakukan authorization dengan memeriksa apakah user yang telah terautentikasi boleh melakukan action yang diinginkan. Untuk pengimplementasiannya bisa beragam tergantung pada use-casenya, bisa menggunakan permission, user group, role, decorator, dsb. Contoh penggunaan authorization pada tugas ini adalah decorator `@login_required()`.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login menggunakan session. Session berisi informasi pengguna yang telah login dan disimpan di database atau cache. Django juga menggunakan cookies untuk menyimpan informasi session pengguna di client. Selain untuk menyimpan session, cookies dapat digunakan untuk menyimpan informasi lain seperti token CSRF dan preferensi pengguna. Tidak semua cookies aman digunakan. Contoh yang tidak aman adalah cookies yang menyimpan informasi sensitif user, sehingga dapat menyebabkan serangan XSS (Cross-Site Scripting).

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Untuk mengimplementasikan register, tambahkan fungsi berikut pada views.

   ```python
   def register(request):
   form = UserCreationForm()

   if request.method == "POST":
     form = UserCreationForm(request.POST)
     if form.is_valid():
       form.save()
       messages.success(request, 'Your account has been successfully created!')
       return redirect('main:login')
   context = {'form' : form}
   return render(request, 'register.html', context)
   ```

   Fungsi ini akan me-render form pembuatan user pada template dan meng-handle logic pembuatan user pada model. Kita juga perlu membuat template baru bernama `register.html` untuk menampilkan form yang sudah dibuat.

2. Untuk mengimplementasikan login, tambahkan fungsi berikut pada views.

   ```python
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

   Fungsi ini akan me-render form authentication pada template dan meng-handle logic untuk mengautentikasi user. Kita juga perlu membuat template baru bernama `login.html` untuk menampilkan form yang sudah dibuat.

3. Untuk mengimplementasikan logout, tambahkan fungsi berikut pada views.

   ```python
   def logout_user(request):
   logout(request)
   response = HttpResponseRedirect(reverse('main:login'))
   response.delete_cookie('last_login')
   return response
   ```

   Fungsi ini akan meng-handle logic untuk melakukan logout user. Kita juga perlu menambahkan button pada `main.html` seperti berikut.

   ```django
   <a href="{% url 'main:logout' %}">
     <button>Logout</button>
   </a>
   ```

4. Untuk membuat 2 akun pengguna dengan masing-masing 3 dummy data, lakukan register 2 buah akun. Untuk masing-masing akun, lakukan login, lalu buat product dengan mengklik button dan mengisi form yang tersedia.

5. Untuk menghubungkan model `Product` dengan `User`, tambahkan field `user` pada model `Product` sebagai foreign key seperti berikut.

   ```python
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ```

6. Untuk menampilkan username dari user yang sedang logged in, tambahkan baris berikut pada `context` pada fungsi `show_main()`.

   ```python
   'nama': request.user.username,
   ```

   Object `request` berisi informasi terkait user yang sedang logged in, proses ini telah dihandle secara otomatis oleh Django saat melakukan login.

7. Untuk menerapkan cookie, tambahkan baris berikut pada fungsi `login_user()`.
   ```python
   response = HttpResponseRedirect(reverse("main:show_main"))
   response.set_cookie('last_login', str(datetime.datetime.now()))
   return response
   ```
   Ini akan membuat cookie dengan key `last_login` setelah user melakukan login. Untuk menampilkan informasi dari cookie `last_login`, tambahkan baris berikut pada `context` pada fungsi `show_main()`.
   ```python
   'last_login': request.COOKIES['last_login'],
   ```
   Tambahkan baris berikut pada `main.html` untuk menampilkan informasi `last_login`.
   ```django
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```

# Tugas 3

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data merupakan komponen esensial dalam sebuah platform. Oleh karena itu, diperlukan data delivery agar dapat mengirim data dengan cepat dan efisien. Data delivery memungkinkan developer untuk mengirim data ke berbagai tempat seperti dari client ke server atau sebaliknya, dan data dapat disajikan dalam berbagai format seperti XML, JSON, atau HTML.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik dari XML karena sintaksnya yang ringkas dan ukuran datanya lebih kecil dan ringan ketimbang XML. Ini membuat JSON lebih mudah dipahami oleh developer dan lebih efisien untuk digunakan dalam komputer. Selain itu, JSON berbasis pada subset dari Javascript, sehingga lebih terintegrasi dan mudah untuk digunakan pada Javascript dan bahasa lainnya. Hal ini juga yang membuat JSON lebih populer dibandingkan XML.

## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` berfungsi untuk memvalidasi data yang dimasukkan dalam input form. Kita membutuhkan method tersebut karena bisa saja user menginput data yang tidak sesuai dengan yang diharapkan ke dalam form.

## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` pada django berfungsi sebagai mekanisme keamanan terhadap serangan CSRF (Cross Site Request Forgery), yaitu serangan dimana penyerang mengirim request palsu ke server melalui user yang terotorisasi. Jika kita tidak menambahkan `csrf_token` pada form Django, maka form tersebut akan lebih rentan terhadap serangan CSRF. Kondisi ini dapat dimanfaatkan oleh penyerang dengan cara melakukan login sebagai user yang menjadi korban, lalu mengirim request destruktif ke server.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat class baru yang meng-inherit class `ModelForm`, yaitu jenis form khusus pada Django yang menghubungkan form dengan model.

   ```python
   from django.forms import ModelForm
   from .models import Product

   class ProductForm(ModelForm):
     class Meta:
       model = Product
       fields = ["name", "price", "description"]
   ```

2. Membuat instance dari class `ProductForm` pada views, lalu mengirim instance dari form tersebut ke template.

   ```python
   def create_product(request):
     if request.method == 'POST':
       form = ProductForm(request.POST)
       if form.is_valid():
         form.save()
         return redirect("main:show_main")
     else:
       form = ProductForm()

     return render(request, "create_product.html", {"form": form})
   ```

3. Menampilkan form pada template seperti berikut.

   ```django
   {% extends "base.html" %} {% block content %}
   <form method="post">
     {% csrf_token %}
     <table>
       {{ form.as_table }}
       <tr>
         <td></td>
         <td>
           <input type="submit" value="Create" />
         </td>
       </tr>
     </table>
   </form>
   {% endblock %}
   ```

4. Membuat 4 fungsi berikut pada views dimana keempat fungsi tersebut mengambil data dari model, lalu mengembalikannya dengan format yang sesuai menggunakan serializers.

   ```python
   def show_xml(request):
     data = Product.objects.all()
     return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
     data = Product.objects.all()
     return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def show_xml_by_id(request, id):
     data = Product.objects.filter(pk=id)
     return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json_by_id(request, id):
     data = Product.objects.filter(pk=id)
     return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

5. Menambahkan baris berikut pada list `urlpatterns` pada `urls.py` aplikasi `main` untuk melakukan routing.
   ```python
   path('xml/', show_xml, name='show_xml'),
   path('json/', show_json, name='show_json'),
   path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
   path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
   ```

## Screenshot Postman

- ### XML
  ![show_xml](/show_xml.png)
- ### JSON
  ![show_json](/show_json.png)
- ### XML by ID
  ![show_xml_by_id](/show_xml_by_id.png)
- ### JSON by ID
  ![show_json_by_id](/show_json_by_id.png)

# Tugas 2

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat proyek django baru dengan membuat direktori baru, mengaktifkan python virtual environment, dan menginstal dependencies sesuai dengan yang telah dilakukan pada tutorial sebelumnya. Lalu untuk membuat proyek django baru, jalankan perintah berikut.

   ```
   django-admin startproject toko_tokoan .
   ```

2. Untuk membuat aplikasi dengan nama `main`, jalankan perintah berikut.

   ```
   python manage.py startapp main
   ```

3. Untuk mengatur routing agar dapat menjalankan aplikasi `main`, tambahkan potongan kode berikut di `urls.py` pada root project (folder `toko_tokoan`). Tujuannya agar django memetakan root url ke file `urls.py` pada aplikasi `main`.

   ```python
   path('', include('main.urls'))
   ```

4. Untuk membuat model, tambahkan potongan kode berikut di file `models.py` pada direktori `main`. Di sini class `Product` beserta attribute-attributenya merepresentasikan model yang akan digunakan nantinya.

   ```python
   class Product(models.Model):
     name = models.CharField(max_length=255)
     price = models.IntegerField()
     description = models.TextField()
   ```

5. Tambahkan fungsi berikut di file `views.py`. Fungsi `show_main` ini akan mendefinisikan `context` yang akan ditampilkan pada halaman html, lalu memanggil fungsi `render` untuk menampilkan halaman `main.html` dengan data `context` yang sudah didefinisikan.

   ```python
   def show_main(request):
     context = {
       'nama_app': 'toko-tokoan',
       'nama': 'Andreas Timothy',
       'kelas': 'PBP E'
     }

     return render(request, "main.html", context)
   ```

6. Tambahkan 2 potongan kode berikut pada file `urls.py` di direktori `main` untuk mengimport fungsi `show_main` yang sudah didefinisikan sebelumnya, lalu memetakan root url untuk memanggil fungsi `show_main` tersebut.

   ```python
   from main.views import show_main
   ```

   ```python
   path('', show_main, name='show_main'),
   ```

7. Untuk men-deploy aplikasi ke pws, inisialisasi direktori ini sebagai git repository, menambahkan project pada pws sebagai remote, lalu melakukan push dari local ke remote pws.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html.

![Bagan](/bagan.png)

## Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah version control system, yang berfungsi untuk menyimpan dan mengelola kode dari sebuah software. Git memiliki berbagai kegunaan dalam pengembangan perangkat lunak, diantaranya:

- Mencatat dan mengelola history commit/perubahan yang dilakukan sehingga developer dapat melihat perubahan yang terjadi atau melakukan _rollback_ ke commit sebelumnya jika diperlukan.
- Memudahkan kolaborasi antara beberapa developer dengan fitur _branching_, sehingga setiap developer dapat bekerja dengan efektif dan rapi.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, django digunakan dalam permulaan pembelajaran pengembangan perangkat lunak karena django sudah mencakup banyak komponen yang umum digunakan dalam pengembangan perangkat lunak, seperti ORM, template engine, router, admin area, dsb sehingga kita dapat mengembangkan aplikasi dengan cepat. Selain itu, django adalah framework berbasis python, dimana python biasanya dianggap sebagai bahasa yang mudah untuk dipelajari dan secara khusus di Fasilkom UI, mahasiswa sudah mempelajari python di mata kuliah sebelumnya.

## Mengapa model pada Django disebut sebagai ORM?

Model pada django disebut sebagai ORM karena dalam aplikasi django, kita dapat langsung berinteraksi dengan database melalui model yang ada. Ketika kita membuat object/instance dari sebuah model, kita dapat melakukan operasi CRUD (create, read, update, delete) pada database secara langsung dari object tersebut.
