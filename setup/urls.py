from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("dashboard.urls")),
    path('', include('ativos.urls')),
    path('', include('investimentos.urls')),
    path('', include('user.urls')),
]
