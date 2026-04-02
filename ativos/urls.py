from django.contrib import admin
from django.urls import path
from ativos.views import ativos, novo_ativo, descricao_ativo, buscar_ativo


urlpatterns = [
    path('ativos/', ativos, name="ativos"),
    path('novo-ativo/', novo_ativo, name="novo-ativo"),
    path('descricao-ativo/<int:ativo_id>', descricao_ativo, name="descricao-ativo"),
    path('buscar-ativo', buscar_ativo, name='buscar-ativo')
    
]