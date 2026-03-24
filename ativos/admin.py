from django.contrib import admin
from ativos.models import Ativos


class Listar_ativos(admin.ModelAdmin):
    list_display = ("codigo","descricao","localizacao","ativo")
    list_display_links = ("codigo","descricao","localizacao")
    search_fields = ("codigo","descricao","localizacao","ativo")
    list_editable = ('ativo',)

admin.site.register(Ativos,Listar_ativos)
