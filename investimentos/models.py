from django.db import models
from user.models import Empresa

class Investimentos(models.Model):

    FILIAIS_CHOICES = [
        ('SANTA LUCIA', 'Santa Lúcia'),
        ('GRANDE LESTE', 'Grande Leste'),
        ('SANTO EXPEDITO', 'Santo Expedito'),
        ('JATOBA', 'Jatobá'),
        ('ESCRITORIO CENTRAL', 'Escritório Central'),
        ('UBA', 'Uba'),
    ]

    empresa = models.ForeignKey(Empresa, related_name="investimentos",on_delete=models.CASCADE, null=False, blank=False)
    codigo = models.CharField(blank=False, null=False, max_length=10)
    descricao = models.CharField(blank=False, null=False, max_length=50)
    ativo = models.BooleanField(blank=False, null=False, max_length=15)
    detalhamento = models.TextField(blank=True, null= True)
    localizacao = models.CharField(blank=False, null=False, max_length=20, choices=FILIAIS_CHOICES)
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
