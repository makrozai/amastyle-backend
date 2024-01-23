from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search),
    path('', views.get_sizes),
    path('get/<int:pk>/', views.get_size),
    path('post/', views.create_size),
    path('edit/<int:pk>/', views.edit_size),
    path('delete/<int:pk>/', views.delete_size),
]
