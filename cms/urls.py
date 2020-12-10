from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cms import views
urlpatterns = [
    path("", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("imgupload/", views.imgupload, name="imgupload"),
    path("client_upload/", views.client_upload, name="client_upload"),
    path("banner_image/", views.banner_image, name="banner_image"),
    path("customize/", views.customize, name="customize"),

] 
