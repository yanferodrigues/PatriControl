from django.contrib import admin
from user.models import Usuario, Empresa,Responsavel


class Listar_usuario(admin.ModelAdmin):
    list_display = ("user__username","user__email", "empresa")
    list_display_links = ("user__username","user__email", "empresa")
    search_fields = ("user__username","user__email", "empresa")
class Listar_empresa(admin.ModelAdmin):
    list_display = ("nome","cidade")
    list_display_links = ("nome","cidade")
    search_fields = ("nome","cidade")
class Listar_responsavel(admin.ModelAdmin):
    list_display = ("nome","cpf")
    list_display_links = ("nome","cpf")
    search_fields = ("nome","cpf")

admin.site.register(Usuario,Listar_usuario)
admin.site.register(Empresa,Listar_empresa)
admin.site.register(Responsavel,Listar_responsavel)