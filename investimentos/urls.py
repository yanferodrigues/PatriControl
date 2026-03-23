from django.contrib import admin
from django.urls import path
from investimentos.views import investimentos, novo_investimento

urlpatterns = [
    path('investimentos/', investimentos, name="investimentos"),
    path('novo-investimento/', novo_investimento, name="novo-investimento"),
]