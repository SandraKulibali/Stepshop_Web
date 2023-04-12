from django.shortcuts import render


def index(request):
    title = 'Main'
    context = {
        'title': title,
    }
    return render(request, 'index.html', context)


def contacts(request):
    title = 'Contacts'
    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)


def products(request):
    title = 'Products | Catalogue'
    context = {
        'title': title,
    }
    return render(request, 'products.html', context)


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
