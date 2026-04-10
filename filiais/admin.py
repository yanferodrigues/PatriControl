from django.contrib import admin
from filiais.models import Filial


class ListarFiliais(admin.ModelAdmin):
    list_display = ("nome", "empresa")
    list_display_links = ("nome",)
    search_fields = ("nome", "empresa__nome")


admin.site.register(Filial, ListarFiliais)
