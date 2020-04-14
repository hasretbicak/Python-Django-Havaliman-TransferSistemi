from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import *
from product.models import *


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:15]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:1]

    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproduct': randomproducts,

               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page': 'referanslar'}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.subject = form.cleaned_data['subject']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür Ederiz.")
            return HttpResponseRedirect('/iletisim')
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting,
               'category': category,
               'form': form}
    return render(request, 'iletisim.html', context)

def category_products(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
               'category': category,
               'categorydata': categorydata,
               }
    return render(request, 'products.html', context)
