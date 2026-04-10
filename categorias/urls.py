from django.urls import path
from categorias.views import nova_categoria, categorias, apagar_categoria

urlpatterns = [
    path('categorias/', categorias, name="categorias"),
    path('nova-categoria/', nova_categoria, name="nova-categoria"),
    path('apagar-categoria/<int:categoria_id>', apagar_categoria, name="apagar-categoria"),
]
