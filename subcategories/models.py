from django.db import models
from categories.models import Category

# Create your models here.

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default='placeholder.png')
    created = models.DateTimeField(auto_now_add=True)