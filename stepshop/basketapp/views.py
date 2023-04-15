from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product


links_menu = [
    {'href': 'index', 'name': 'Main', 'route': ''},
    {'href': 'products:index', 'name': 'Products', 'route': 'products/'},
    {'href': 'about', 'name': 'About Us', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Contacts', 'route': 'contacts/'},
]

@login_required
def basket(request):
    basket = Basket.objects.filter(user=request.user)

    context = {
        'basket': basket,
        'links_menu': links_menu,
    }

    return render(request, 'basket/basket.html', context)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket = Basket.objects.filter(user=request.user).order_by('product__category')

        context = {
            'basket': basket,
        }

        result = render_to_string('basket/includes/inc_basket_list.html', context)

        return JsonResponse({'result': result})


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
