from django.urls import path
from filiais.views import nova_filial, filiais, apagar_filial

urlpatterns = [
    path('filiais/', filiais, name="filiais"),
    path('nova-filial/', nova_filial, name="nova-filial"),
    path('apagar-filial/<int:filial_id>', apagar_filial, name="apagar-filial"),
]
