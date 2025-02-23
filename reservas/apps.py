from django.apps import AppConfig
from django.db.models.signals import post_migrate

def criar_salas_padrao(sender, **kwargs):
    from .models import Sala
    salas_padrao = [
        {'nome': 'Sala 1', 'capacidade': 10},
        {'nome': 'Sala 2', 'capacidade': 15},
        {'nome': 'Sala 3', 'capacidade': 20},
        {'nome': 'Sala 4', 'capacidade': 25},
        {'nome': 'Sala 5', 'capacidade': 30},
        {'nome': 'Sala 6', 'capacidade': 35},
    ]
    for sala in salas_padrao:
        Sala.objects.get_or_create(**sala)

class ReservasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservas'

    def ready(self):
        post_migrate.connect(criar_salas_padrao, sender=self)