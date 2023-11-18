from django.http import HttpResponse
from django.shortcuts import render

from home.forms import ContactForm
from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'home'}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkımızda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'referanslar'}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {'setting': setting,
               'page': 'iletisim',
               'form': form}
    return render(request, 'iletisim.html', context)
