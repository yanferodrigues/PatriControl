from django.core.management.base import BaseCommand
from categorias.models import CategoriaOperacional
from user.models import Empresa

CATEGORIAS_PADRAO = [
    'MÁQUINAS E IMPLEMENTOS',
    'INFORMÁTICA E COMUNICAÇÃO',
    'VEÍCULOS',
    'EQUIPAMENTOS DIVERSOS',
    'MÓVEIS E UTENSÍLIOS',
    'EQUIPAMENTOS OFICINA',
    'EQUIPAMENTOS UBG',
    'EQUIPAMENTOS UBA',
    'AERONAVES',
]


class Command(BaseCommand):
    help = 'Popula as categorias operacionais padrão para todas as empresas cadastradas'

    def handle(self, *args, **kwargs):
        empresas = Empresa.objects.all()
        for empresa in empresas:
            criadas = 0
            for nome in CATEGORIAS_PADRAO:
                _, created = CategoriaOperacional.objects.get_or_create(
                    empresa=empresa,
                    nome=nome,
                    defaults={'ativo': True},
                )
                if created:
                    criadas += 1
            self.stdout.write(f'{empresa.nome}: {criadas} categoria(s) criada(s)')
        self.stdout.write(self.style.SUCCESS('Concluído.'))
