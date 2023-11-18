from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import ContactForm
from home.models import Setting, ContactFormMessage
from product.models import Product, Category, Images, Comment, CommentForm


# Create your views here.

def index(request):
    slider = Product.objects.all()
    urunler = Product.objects.order_by('?')[:8]
    context = {'page': 'home',
               'slider': slider,
               'urunler':urunler}
    return render(request, 'index.html', context)


def hakkimizda(request):
    context = {'page': 'hakkımızda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    context = {'page': 'referanslar'}
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
    context = {'form': form,
               'page': 'iletisim'}
    return render(request, 'iletisim.html', context)


def categoryProducts(request, id, slug):
    urunKategori = Category.objects.get(pk=id)
    urunler = list(Product.objects.filter(category_id=id))

    node = Category.objects.get(pk=id)
    children = Category.objects.add_related_count(node.get_children(), Product,
                                                  'category', 'product_counts')
    for dd in children:
        a = list(Product.objects.filter(category_id=dd.id))
        urunler.extend(a)

    context = {'page': 'Kategori',
               'urunKategori': urunKategori,
               'urunler': urunler}
    return render(request, 'kategori_urunler.html', context)


def productDetail(request, id, slug):
    urun = Product.objects.get(pk=id)
    images = Images.objects.filter(product = urun)
    # print(request.get_full_path())
    # print(request.get_host())
    # print(request.build_absolute_uri())
    comments = Comment.objects.filter(product_id=id)
    context = {'page': 'Urun',
               'urun': urun,
               'images': images,
               'comments': comments
    }
    return render(request, 'urun_detay.html', context)
