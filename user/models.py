from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    foto = models.ImageField(upload_to='fotos_usuarios/%Y/%m/%d', blank=True, null=True)
    empresa = models.CharField(blank=False, null=False)
    incorporacao = models.DateField(blank=False, null=False)
