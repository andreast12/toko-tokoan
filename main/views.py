from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
  products = Product.objects.all()
  context = {
    'nama_app': 'toko-tokoan',
    'nama': 'Andreas Timothy',
    'kelas': 'PBP E',
    'products': products
  }

  return render(request, "main.html", context)

def create_product(request):
  if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("main:show_main")
  else:
    form = ProductForm()

  return render(request, "create_product.html", {"form": form})

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