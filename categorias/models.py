from django.db import models
from user.models import Empresa


class CategoriaOperacional(models.Model):
    empresa = models.ForeignKey(Empresa, related_name="categorias", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
