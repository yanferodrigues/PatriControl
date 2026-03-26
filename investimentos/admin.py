from django.contrib import admin
from investimentos.models import Investimentos

class ListarInvestimentos(admin.ModelAdmin):
    list_display = ("codigo","descricao","localizacao","ativo")
    list_display_links = ("codigo","descricao","localizacao")
    search_fields = ("codigo","descricao","localizacao","ativo")
    list_editable = ('ativo',)

admin.site.register(Investimentos, ListarInvestimentos)
