import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from ativos.models import Ativos
from investimentos.models import Investimentos
df = pd.read_excel('ATIVOS SF.xlsx')


for _, linha in df.iterrows():
    data = pd.to_datetime(linha['DATA EMISSÃO'], errors='coerce')
    if linha['CLASSE DO ATIVO'] != 'IMÓVEIS':
        Ativos.objects.create(
            codigo=linha['IS '],
            descricao=linha['DESCRIÇÃO DO ITEM'],
            chassi=linha['CHASSI'],
            placa=linha['PLACA'],
            adesivado=str(linha['ADESIVADO']).strip().upper() == "OK",
            auxiliar=linha['ITEM '],
            cor=linha['Cor'],
            categoria=linha['CLASSE DO ATIVO'],
            ativo=True,
            detalhamento=linha['OBSERVAÇÕES EXTRAS'],
            localizacao=linha['LOCALIZAÇÃO DE ORIGEM'],
            responsavel=linha['COLABORADOR'],
            incorporacao=data.date() if pd.notna(data) else None,
            fornecedor=linha['FORNECEDOR/CLIENTE'],
            numero_nota=int(linha['NOTA FISCAL']) if not pd.isna(linha['NOTA FISCAL']) and linha['NOTA FISCAL'] != 'NOTA NÃO ENCONTRADA' else None,
            valor=float(linha['FORMATADO']) if not pd.isna(linha['FORMATADO']) else None
        )

for _, linha in df.iterrows():
    data = pd.to_datetime(linha['DATA EMISSÃO'], errors='coerce')
    if linha['CLASSE DO ATIVO'] == 'IMÓVEIS':
        Investimentos.objects.create(
            codigo=linha['IS '],
            descricao=linha['DESCRIÇÃO DO ITEM'],
            ativo=True,
            detalhamento=linha['ITEM '],
            localizacao=linha['LOCALIZAÇÃO DE ORIGEM'],
            data=data.date() if pd.notna(data) else None,
            valor=float(linha['FORMATADO']) if not pd.isna(linha['FORMATADO']) else None
        )

