from django.db import models
from django.utils import timezone
from user.models import Empresa

class Ativos(models.Model):
    CATEGORIA_CHOICES = [
        ('MÁQUINAS E IMPLEMENTOS', 'Máquinas e implementos'),
        ('INFORMÁTICA E COMUNICAÇÃO', 'Informática e comunicação'),
        ('VEÍCULOS', 'Veículos'),
        ('EQUIPAMENTOS DIVERSOS', 'Equipamentos diversos'),
        ('MÓVEIS E UTENSÍLIOS', 'Móveis e utensílios'),
        ('EQUIPAMENTOS OFICINA', 'Equipamentos oficina'),
        ('EQUIPAMENTOS UBG', 'Equipamentos UBG'),
        ('EQUIPAMENTOS UBA', 'Equipamentos UBA'),
        ('AERONAVES', 'Aeronaves')
    ]
    FILIAIS_CHOICES = [
        ('SANTA LUCIA', 'Santa Lúcia'),
        ('GRANDE LESTE', 'Grande Leste'),
        ('SANTO EXPEDITO', 'Santo Expedito'),
        ('JATOBA', 'Jatobá'),
        ('ESCRITORIO CENTRAL', 'Escritório Central'),
        ('UBA', 'Uba'),
    ]
    
    empresa = models.ForeignKey(Empresa, related_name="ativos",on_delete=models.CASCADE, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    codigo = models.CharField(blank=False, null=False, max_length=10)
    descricao = models.CharField(blank=False, null=False, max_length=50)
    chassi = models.CharField(blank=True, null=True, max_length=50)
    placa = models.CharField(blank=True, null=True, max_length=10)
    adesivado = models.BooleanField(blank=False, null=False)
    auxiliar = models.CharField(blank=False, null=False, max_length=10)
    cor = models.CharField(blank=True, null=True, max_length=15)
    categoria = models.CharField(blank=False, null=False, max_length=50, choices=CATEGORIA_CHOICES)
    ativo = models.BooleanField(blank=False, null=False, max_length=15)
    detalhamento = models.TextField(blank=True, null= True)
    localizacao = models.CharField(blank=False, null=False, max_length=20, choices=FILIAIS_CHOICES)
    responsavel = models.CharField(blank=True, null=True, max_length=50)
    incorporacao = models.DateField(blank=True, null=True)
    fornecedor = models.CharField(blank=True, null=True, max_length=200)
    numero_nota = models.IntegerField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    nota = models.FileField(upload_to="documentos/%Y/%m/%d", blank=True)

    TAXA_DEPRECIACAO_ANUAL = 0.10

    @property
    def valor_depreciado(self):
        if not self.valor or not self.incorporacao:
            return None
        hoje = timezone.now().date()
        anos = (hoje - self.incorporacao).days / 365.25
        fator = max(0.0, 1 - self.TAXA_DEPRECIACAO_ANUAL * anos)
        return round(self.valor * fator, 2)

    @property
    def percentual_depreciado(self):
        if not self.valor or not self.incorporacao:
            return None
        hoje = timezone.now().date()
        anos = (hoje - self.incorporacao).days / 365.25
        percentual = min(100.0, self.TAXA_DEPRECIACAO_ANUAL * anos * 100)
        return round(percentual, 1)
