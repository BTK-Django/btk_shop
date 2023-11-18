from django.http import HttpResponse
from django.shortcuts import render

from product.models import Category, Product


# Create your views here.
def index(request):
    return HttpResponse("ürünler")
