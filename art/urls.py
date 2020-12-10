from django.contrib import admin
from django.urls import path
from art import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('client/', views.client, name="client"),
    path('contact/', views.contact, name="contact"),
    path('post/<int:id>/',views.detail_view,name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

