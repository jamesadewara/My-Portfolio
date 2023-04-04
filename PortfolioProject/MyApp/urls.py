
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name = "home"),
    path("contactMe", views.contactForm, name = "contact_email")
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)