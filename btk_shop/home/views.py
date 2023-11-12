from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    title= "Volkan"
    context = {'title': title}
    return render(request, 'index.html', context)
    # return HttpResponse("Merhaba")
