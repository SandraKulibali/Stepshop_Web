from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=64,
        unique=True,
    )
    description = models.TextField(
        verbose_name="description",
        blank=True,
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name or f'Category Id - {self.pk}'

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        verbose_name="category",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='product name',
        max_length=128,
    )
    image = models.ImageField(
       verbose_name="product image",
       upload_to='product_images',
       blank=True,
    )
    short_desc = models.CharField(
        verbose_name="short description",
        max_length=128,
        blank=True,
    )
    description = models.TextField(
        verbose_name="description",
        blank=True,
    )
    price = models.DecimalField(
        verbose_name="price",
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name="remains quantity",
        default=0,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name or f'Product Id - {self.pk}'

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
