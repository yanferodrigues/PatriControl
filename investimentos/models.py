from django.db import models

class Investimentos(models.Model):

    FILIAIS_CHOICES = [
        ('SANTA LUCIA', 'Santa Lúcia'),
        ('GRANDE LESTE', 'Grande Leste'),
        ('SANTO EXPEDITO', 'Santo Expedito'),
        ('JATOBA', 'Jatobá'),
        ('ESCRITORIO CENTRAL', 'Escritório Central'),
        ('UBA', 'Uba'),
    ]


    codigo = models.CharField(blank=False, null=False, max_length=10)
    descricao = models.CharField(blank=False, null=False, max_length=50)
    ativo = models.BooleanField(blank=False, null=False, max_length=15)
    detalhamento = models.TextField(blank=True, null= True)
    localizacao = models.CharField(blank=False, null=False, max_length=20, choices=FILIAIS_CHOICES)
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
