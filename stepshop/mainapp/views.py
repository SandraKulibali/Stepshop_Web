from random import sample

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


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products = Product.objects.all()
    return sample(list(products), 1)[0]


def get_same_products(product):
    same_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
    return same_products


def products(request, pk=None):
    title = "products"

    products = Product.objects.all().order_by('-price')  # [:2]
    categories = ProductCategory.objects.all()

    basket = get_basket(request.user)

    context = {
        'title': title,
        'products': products,
        'categories': categories,
        'links_menu': links_menu,
        'basket': basket,
    }

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all()
            category = {'name': 'All'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk)

        context.update({'products': products_, 'category': category})

    return render(request, 'products.html', context)


def product(request, pk):
    title = "product"

    product_item = get_object_or_404(Product, pk=pk)
    category = product_item.category
    basket = get_basket(request.user)
    same_products = get_same_products(product_item)  # [:10]

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'category': category,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'product.html', context)
