from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search),
    path('', views.get_subcategories),
    path('by-category/<int:pk>', views.get_subcategories_by_category),
    path('get/<int:pk>/', views.get_subcategory),
    path('post/<int:pk>/', views.create_subcategory),
    path('edit/<int:pk>/', views.edit_subcategory),
    path('delete/<int:pk>/', views.delete_subcategory),
]
