from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search),
    path('', views.get_colors),
    path('get/<int:pk>/', views.get_color),
    path('post/', views.create_color),
    path('edit/<int:pk>/', views.edit_color),
    path('delete/<int:pk>/', views.delete_color),
]
