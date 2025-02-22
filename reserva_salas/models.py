from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    responsavel = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.sala.nome} - {self.data_reserva} {self.hora_inicio}-{self.hora_fim}"

    def save(self, *args, **kwargs):
        # Marca a sala como indisponível ao criar uma reserva
        self.sala.disponivel = False
        self.sala.save()
        super().save(*args, **kwargs)