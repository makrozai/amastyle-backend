from django.db import models
from products.models import Product
from colors.models import Color
from sizes.models import Size
# Create your models here.

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=True, blank=True)
    discount = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class Images(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='placeholder.png')
    created = models.DateTimeField(auto_now_add=True)