from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from store import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store/', views.store, name="store"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('add-address/', views.AddressView.as_view(), name="add-address"),
    path('remove-address/<int:id>/', views.remove_address, name="remove-address"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
