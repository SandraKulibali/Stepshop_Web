from django.shortcuts import render

from mainapp.models import Product


links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def index(request):
    title = 'Main'
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'products': products,
        'links_menu': links_menu,
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
