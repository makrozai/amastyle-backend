from django.db import models
# Create your models here.

class Size(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)