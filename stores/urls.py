from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search),
    path('', views.get_stores),
    path('get/<int:pk>/', views.get_store),
    path('post/', views.create_store),
    path('edit/<int:pk>/', views.edit_store),
    path('delete/<int:pk>/', views.delete_store),
]
