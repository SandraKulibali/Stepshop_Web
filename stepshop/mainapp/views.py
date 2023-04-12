from django.shortcuts import render


def products(request):
    title = 'Products | Catalogue'

    links_menu = [
        {'href': 'products_all', 'name': 'all'},
        {'href': 'products_galaxies', 'name': 'galaxies'},
        {'href': 'products_stars', 'name': 'stars'},
        {'href': 'products_spacecrafts', 'name': 'spacecrafts'},
        {'href': 'products_planets', 'name': 'planets'},
    ]
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'products.html', context)


def product(request):
    title = 'Product | Detail'
    context = {
        'title': title,
    }
    return render(request, 'product.html', context)
