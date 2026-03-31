import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from ativos.models import Ativos

df = pd.read_excel('ativos_mock.xlsx')

for _, linha in df.iterrows():
    Ativos.objects.create(
        codigo=linha['codigo'],
        descricao=linha['descricao'],
        chassi=linha['chassi'],
        placa=linha['placa'],
        adesivado=bool(linha['adesivado']),
        auxiliar=linha['auxiliar'],
        cor=linha['cor'],
        categoria=linha['categoria'],
        ativo=bool(linha['ativo']),
        detalhamento=linha['detalhamento'],
        localizacao=linha['localizacao'],
        responsavel=linha['responsavel'],
        incorporacao=linha['incorporacao'],
        fornecedor=linha['fornecedor'],
        numero_nota=int(linha['numero_nota']) if not pd.isna(linha['numero_nota']) else None,
        valor=float(linha['valor']) if not pd.isna(linha['valor']) else None
    )