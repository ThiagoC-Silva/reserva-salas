from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Sala(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    capacidade = models.PositiveIntegerField()

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
        if self.data < timezone.now().date():
            raise ValidationError("A data da reserva não pode ser no passado. Por favor, selecione uma data futura.")

        if self.hora_fim <= self.hora_inicio:
            raise ValidationError("O horário de término deve ser após o horário de início. Por favor, ajuste os horários.")

        conflitos_usuario = Reserva.objects.filter(
            usuario=self.usuario,
            data=self.data,
            hora_inicio__lt=self.hora_fim,
            hora_fim__gt=self.hora_inicio,
        ).exclude(id=self.id)  

        if conflitos_usuario.exists():
            raise ValidationError("Você já tem uma reserva para este horário. Por favor, escolha outro horário.")

        conflitos_sala = Reserva.objects.filter(
            sala=self.sala,
            data=self.data,
            hora_inicio__lt=self.hora_fim,
            hora_fim__gt=self.hora_inicio,
        ).exclude(id=self.id)  

        if conflitos_sala.exists():
            raise ValidationError("Esta sala já está reservada para o horário selecionado. Por favor, escolha outro horário ou sala.")

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)