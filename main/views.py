from django.shortcuts import render

# Create your views here.
def show_main(request):
  context = {
    'nama_app': 'toko-tokoan',
    'nama': 'Andreas Timothy',
    'kelas': 'PBP E'
  }

  return render(request, "main.html", context)