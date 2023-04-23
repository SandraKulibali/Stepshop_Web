from django.http import request
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, UpdateView, DetailView

from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.forms import ProductCategoryEditForm, ProductEditForm
from mainapp.models import ProductCategory, Product


class UsersListView(ListView):
    model = ShopUser
    template_name = 'admin_staff/users.html'
    context_object_name = 'users_list'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        context.update({'title': 'users'})
        return context

    def get_queryset(self):
        return ShopUser.objects.order_by('-is_active',
                                         '-is_superuser',
                                         '-is_staff',
                                         'username')


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'admin_staff/user_create.html'
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context.update({'title': 'users | create'})
        return context


class UserUpdateView(UpdateView):
    model = ShopUser
    fields = ['username', 'first_name', 'age', 'avatar', 'is_active']
    template_name = 'admin_staff/user_update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('admin_staff:users')


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'admin_staff/user_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('admin_staff:users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'admin_staff/categories.html'
    context_object_name = 'categories_list'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesListView, self).get_context_data()
        context.update({'title': 'categories'})
        return context

    def get_queryset(self):
        return ProductCategory.objects.order_by('name',
                                                '-is_active', )


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'admin_staff/category_create.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        context.update({'title': 'category | create'})
        return context


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    fields = ['name', 'description', 'is_active']
    template_name = 'admin_staff/category_update.html'
    context_object_name = 'category'

    def get_success_url(self):
        return reverse_lazy('admin_staff:categories')


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admin_staff/category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('admin_staff:categories')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductsListView(ListView):
    template_name = 'admin_staff/products.html'
    context_object_name = 'products_list'
    paginate_by = 3

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Product.objects.filter(category__pk=pk).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'products'
        context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'admin_staff/product_create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data()
        context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        context.update({'title': 'product | create'})
        return context

    def get_success_url(self):
        return reverse_lazy('admin_staff:products', kwargs={'pk': self.object.category.pk})


class ProductReadView(DetailView):
    model = Product
    template_name = 'admin_staff/product_read.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'product | detail'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'category', 'short_desc',  'description', 'price', 'quantity', 'image', 'is_active']
    template_name = 'admin_staff/product_update.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('admin_staff:products', kwargs={'pk': self.object.category.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admin_staff/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('admin_staff:products')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
