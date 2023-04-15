from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'products_all', 'name': 'all'},
    {'href': 'products_galaxies', 'name': 'galaxies'},
    {'href': 'products_stars', 'name': 'stars'},
    {'href': 'products_spacecrafts', 'name': 'spacecrafts'},
    {'href': 'products_planets', 'name': 'planets'},
]


def products(request, pk=None):
    title = "Products | Catalogue"

    products = Product.objects.all().order_by('-price')  # [:2]
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'products': products,
        'categories': categories,
        'links_menu': links_menu,
        'pk': pk,
        'basket': basket,
    }

    return render(request, 'products.html', context)


def product(request, pk):
    title = "Product | Detail"

    product_item = get_object_or_404(Product, pk=pk)
    category = product_item.category

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'category': category,
    }

    return render(request, 'product.html', context)

