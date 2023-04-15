from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def users(request):
    title = 'пользователь'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'users_list': users_list
    }

    return render(request, 'admin/users.html', context)


def user_create(request):
    pass


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass


def categories(request):
    title = 'категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'categories_list': categories_list
    }

    return render(request, 'admin/categories.html', context)


def category_create(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


def products(request, pk):
    title = 'продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'products_list': products_list,
    }

    return render(request, 'admin/products.html', context)


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass
