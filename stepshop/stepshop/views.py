from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'Main'
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'index.html', context)


def contacts(request):
    title = 'Contacts'
    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)


def about(request):
    title = 'About Us'
    context = {
        'title': title,
    }
    return render(request, 'about.html', context)


def product(request):
    title = 'Product | Detail'
    context = {
        'title': title,
    }
    return render(request, 'product.html', context)
