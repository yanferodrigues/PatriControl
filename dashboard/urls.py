from django.contrib import admin
from django.urls import path
from dashboard.views import dashboard, grafico

urlpatterns = [
    path('', dashboard, name="index"),
    path('api/grafico/',grafico)
]