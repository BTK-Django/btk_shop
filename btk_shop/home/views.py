from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import ContactForm
from home.models import Setting, ContactFormMessage
from product.models import Product, Category


# Create your views here.
def index(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    slider = Product.objects.all()
    context = {'category': category,
               'setting': setting,
               'page': 'home',
               'slider': slider}
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, ' Mesajınız Sisteme İletildi')
            return HttpResponseRedirect('/iletisim')
        else:
            messages.warning(request, ' Mesajınız Sisteme İletilemedi')
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {'setting': setting,
               'form': form,
               'page': 'iletisim'}
    return render(request, 'iletisim.html', context)
