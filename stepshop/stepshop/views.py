from django.shortcuts import render

from mainapp.models import Product
from mainapp.views import get_basket

links_menu = [
    {'href': 'index', 'name': 'Main', 'route': ''},
    {'href': 'products:index', 'name': 'Products', 'route': 'products/'},
    {'href': 'about', 'name': 'About Us', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Contacts', 'route': 'contacts/'},
]


def index(request):
    title = 'Main'
    products = Product.objects.all()[:4]
    basket = get_basket(request.user)
    context = {
        'title': title,
        'products': products,
        'links_menu': links_menu,
        'basket': basket,
    }
    return render(request, 'index.html', context)


def contacts(request):
    title = 'Contacts'
    basket = get_basket(request.user)
    context = {
        'title': title,
        'links_menu': links_menu,
        'basket': basket,
    }
    return render(request, 'contacts.html', context)


def about(request):
    title = 'About Us'
    basket = get_basket(request.user)
    context = {
        'title': title,
        'links_menu': links_menu,
        'basket': basket,
    }
    return render(request, 'about.html', context)


def product(request):
    title = 'Product | Detail'
    basket = get_basket(request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'product.html', context)
