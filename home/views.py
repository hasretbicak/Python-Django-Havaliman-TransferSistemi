import json

from ckeditor_uploader.forms import SearchForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from home.models import *
from product.models import *


def index(request):
    setting = Setting.objects.get(pk=1)
    product = Product.objects.all()[:10]
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:15]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:1]

    context = {'setting': setting,
               'category': category,
               'product': product,
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


def product_detail(request, slug, id):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'product': product,
               'category': category,
               'images': images,
               'comments': comments,
               }
    return render(request, 'product_detail.html', context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = {'products': products,
                       'query': query,
                       'category': category,
                       }
            return render(request, 'product_search.html', context)
    return HttpResponseRedirect('/')

def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype ='application/json'
    return HttpResponse(data, mimetype)