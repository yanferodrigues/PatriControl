from django.db import models
from django.contrib.auth.models import User

class Responsavel(models.Model):
    nome = models.CharField(null=False, blank=False)
    cpf = models.CharField(null=False, blank=False)
    def __str__(self):
        return f"{self.nome}"

class Empresa(models.Model):
    nome = models.CharField(null=False, blank=False)
    cidade = models.CharField(null=False, blank=False)
    responsavel = models.ForeignKey(Responsavel,related_name="empresa",on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.nome}"

class Usuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=False, related_name="extras")
    foto = models.ImageField(upload_to='fotos_usuarios/%Y/%m/%d', blank=True, null=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE, null=False, related_name="usuarios")
    incorporacao = models.DateField(blank=False, null=False)




