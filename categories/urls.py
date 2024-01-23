from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search),
    path('', views.get_categories),
    path('get/<int:pk>/', views.get_category),
    path('post/', views.create_category),
    path('edit/<int:pk>/', views.edit_category),
    path('delete/<int:pk>/', views.delete_category),
]
