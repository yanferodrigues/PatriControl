from django.db import models
from user.models import Empresa


class Filial(models.Model):
    empresa = models.ForeignKey(Empresa, related_name="filiais", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
