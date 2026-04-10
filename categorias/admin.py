from django.contrib import admin
from categorias.models import CategoriaOperacional


class ListarCategorias(admin.ModelAdmin):
    list_display = ("nome", "empresa", "ativo")
    list_display_links = ("nome",)
    search_fields = ("nome", "empresa__nome")
    list_editable = ("ativo",)


admin.site.register(CategoriaOperacional, ListarCategorias)
