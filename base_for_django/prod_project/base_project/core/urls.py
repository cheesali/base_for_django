from django.contrib import admin
from django.urls import path, include
from client_management import views

urlpatterns = [
    path("", include("client_management.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]


