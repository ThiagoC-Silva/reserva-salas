from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Sala(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    capacidade = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.usuario.username} - {self.sala.nome} ({self.data} {self.hora_inicio}-{self.hora_fim})"

    def clean(self):
       
        if not self.sala.disponivel:
            raise ValidationError("Esta sala não está disponível para reserva.")

        
        conflitos = Reserva.objects.filter(
            sala=self.sala,
            data=self.data,
            hora_inicio__lt=self.hora_fim,
            hora_fim__gt=self.hora_inicio,
        ).exclude(id=self.id)  

        if conflitos.exists():
            raise ValidationError("Já existe uma reserva para esta sala no horário selecionado.")

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)