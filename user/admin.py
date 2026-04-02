from django.contrib import admin
from user.models import Usuario


class Listar_usuario(admin.ModelAdmin):
    list_display = ("user__username","user__email", "empresa")
    list_display_links = ("user__username","user__email", "empresa")
    search_fields = ("user__username","user__email", "empresa")

admin.site.register(Usuario,Listar_usuario)