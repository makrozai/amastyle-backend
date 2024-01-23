from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_variants),
    path('by-product/<int:pk>/', views.get_variants_by_product),
    path('get/<int:pk>/', views.get_variant),
    path('post/', views.create_variant),
    path('post/images/<int:pk>/', views.create_image_variant),
    path('edit/<int:pk>/', views.edit_variant),
    path('delete/<int:pk>/', views.delete_variant),
    path('delete/image/<int:pk>/', views.delete_image),
]
