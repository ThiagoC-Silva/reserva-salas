from django.core.management.base import BaseCommand
from reserva_salas.models import Sala

class Command(BaseCommand):
    help = 'Popula o banco de dados com seis salas'

    def handle(self, *args, **kwargs):
        salas = [
            {'nome': 'Sala 1', 'capacidade': 10},
            {'nome': 'Sala 2', 'capacidade': 15},
            {'nome': 'Sala 3', 'capacidade': 20},
            {'nome': 'Sala 4', 'capacidade': 25},
            {'nome': 'Sala 5', 'capacidade': 30},
            {'nome': 'Sala 6', 'capacidade': 35},
        ]
        for sala in salas:
            Sala.objects.create(**sala)
        self.stdout.write(self.style.SUCCESS('Salas criadas com sucesso!'))