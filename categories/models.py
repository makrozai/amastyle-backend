from django.db import models

# Create your models here.

class Category(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default='placeholder.png')
    created = models.DateTimeField(auto_now_add=True)