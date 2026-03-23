from django.contrib import admin
from django.urls import path
from ativos.views import ativos, novo_ativo, descricao_ativo


urlpatterns = [
    path('/ativos', ativos, name="ativos"),
    path('/novo-ativo', novo_ativo, name="novo-ativo"),
    path('/descricao-ativo', descricao_ativo, name="descricao-ativo"),
]