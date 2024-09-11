Link aplikasi: http://andreas-timothy-tokotokoan.pbp.cs.ui.ac.id/

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

```
path('', include('main.urls'))
```

4. Untuk membuat model, tambahkan potongan kode berikut di file `models.py` pada direktori `main`. Di sini class `Product` beserta attribute-attributenya merepresentasikan model yang akan digunakan nantinya.

```
class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.IntegerField()
  description = models.TextField()
```

5. Tambahkan fungsi berikut di file `views.py`. Fungsi `show_main` ini akan mendefinisikan `context` yang akan ditampilkan pada halaman html, lalu memanggil fungsi `render` untuk menampilkan halaman `main.html` dengan data `context` yang sudah didefinisikan.

```
def show_main(request):
  context = {
    'nama_app': 'toko-tokoan',
    'nama': 'Andreas Timothy',
    'kelas': 'PBP E'
  }

  return render(request, "main.html", context)
```

6. Tambahkan 2 potongan kode berikut pada file `urls.py` di direktori `main` untuk mengimport fungsi `show_main` yang sudah didefinisikan sebelumnya, lalu memetakan root url untuk memanggil fungsi `show_main` tersebut.

```
from main.views import show_main
```

```
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
