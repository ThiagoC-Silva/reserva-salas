# Generated by Django 5.1.6 on 2025-02-23 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sala',
            name='disponivel',
        ),
    ]
