from django.db import models

class Ativos(models.Model):
    ADESIVADO_CHOICES = [
        ("ADESIVADO","Adesivado"),
        ("NAO ADESIVADO", "Não adesivado"),
    ]
    CATEGORIA_CHOICES = [
        ('MAQUINAS', 'Máquinas e implementos'),
        ('INFORMATICA', 'Informática e comunicação'),
        ('VEICULOS', 'Veículos'),
        ('EQUIPAMENTOS', 'Equipamentos diversos'),
        ('IMOVEIS', 'Imóveis'),
        ('MOVEIS', 'Móveis e utensílios'),
    ]
    STATUS_CHOICES = [
        ('ATIVO','Ativo'),
        ('INATIVO','Inativo'),
    ]
    FILIAIS_CHOICES = [
    ('SANTA LUCIA', 'Santa Lúcia'),
    ('GRANDE LESTE', 'Grande Leste'),
    ('SANTO EXPEDITO', 'Santo Expedito'),
    ('JATOBA', 'Jatobá'),
    ('ESCRITORIO CENTRAL', 'Escritório Central'),
    ('UBA', 'Uba'),
]

    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    codigo = models.CharField(blank=False, null=False, max_length=10)
    descricao = models.CharField(blank=False, null=False, max_length=50)
    chassi = models.CharField(blank=True, null=True, max_length=50)
    placa = models.CharField(blank=True, null=True, max_length=10)
    adesivado = models.CharField(blank=False, null=False, choices=ADESIVADO_CHOICES)
    auxiliar = models.CharField(blank=False, null=False, max_length=10)
    cor = models.CharField(blank=True, null=True, max_length=15)
    categoria = models.CharField(blank=False, null=False, max_length=20, choices=CATEGORIA_CHOICES)
    status = models.CharField(blank=False, null=False, max_length=15, choices=STATUS_CHOICES)
    detalhamento = models.TextField(blank=True, null= True)
    localizacao = models.CharField(blank=False, null=False, max_length=20, choices=FILIAIS_CHOICES)
    responsavel = models.CharField(blank=True, null=True, max_length=50)
    incorporacao = models.DateField(blank=True, null=True)
    fornecedor = models.CharField(blank=True, null=True, max_length=200)
    numero_nota = models.IntegerField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    nota = models.FileField(upload_to="documentos/%Y/%m/%d", blank=True)


