from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    isim = "Volkan"
    context = {'isim': isim}
    return render(request, 'index.html', context)
    # return HttpResponse("Merhaba")
