from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('categories/', include('categories.urls')),
    path('subcategories/', include('subcategories.urls')),
    path('stores/', include('stores.urls')),
    path('colors/', include('colors.urls')),
    path('sizes/', include('sizes.urls')),
    path('variants/', include('variant.urls')),
]

#urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
