from django.urls import path

from .views import  product, ProductListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/<int:pk>/', ProductListView.as_view(), name='category'),
    path('product/<int:pk>/', product, name='product'),
]
