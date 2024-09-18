Link aplikasi: http://andreas-timothy-tokotokoan.pbp.cs.ui.ac.id/

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
