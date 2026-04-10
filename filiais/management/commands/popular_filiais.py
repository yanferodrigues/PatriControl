from django.core.management.base import BaseCommand
from filiais.models import Filial
from user.models import Empresa

FILIAIS_PADRAO = [
    'SANTA LUCIA',
    'GRANDE LESTE',
    'SANTO EXPEDITO',
    'JATOBA',
    'ESCRITORIO CENTRAL',
    'UBA',
]


class Command(BaseCommand):
    help = 'Popula as filiais padrão para todas as empresas cadastradas'

    def handle(self, *args, **kwargs):
        empresas = Empresa.objects.all()
        for empresa in empresas:
            criadas = 0
            for nome in FILIAIS_PADRAO:
                _, created = Filial.objects.get_or_create(
                    empresa=empresa,
                    nome=nome,
                )
                if created:
                    criadas += 1
            self.stdout.write(f'{empresa.nome}: {criadas} filial(is) criada(s)')
        self.stdout.write(self.style.SUCCESS('Concluído.'))
