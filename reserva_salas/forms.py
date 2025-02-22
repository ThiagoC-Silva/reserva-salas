from django import forms
from reserva_salas.models import Reserva
from django.forms.widgets import DateInput, TimeInput
from django.core.exceptions import ValidationError
from datetime import date

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['sala', 'data_reserva', 'hora_inicio', 'hora_fim', 'responsavel', 'descricao']
        widgets = {
            'data_reserva': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Selecione a data',
            }),
            'hora_inicio': TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Selecione a hora de início',
            }),
            'hora_fim': TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Selecione a hora de término',
            }),
            'sala': forms.Select(attrs={
                'class': 'form-control',
            }),
            'responsavel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do responsável',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição da reserva',
                'rows': 3,
            }),
        }

    def clean_data_reserva(self):
        data_reserva = self.cleaned_data['data_reserva']
        if data_reserva < date.today():
            raise ValidationError("A data da reserva não pode ser no passado.")
        return data_reserva

    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fim = cleaned_data.get('hora_fim')
        sala = cleaned_data.get('sala')

        if hora_inicio and hora_fim:
            if hora_fim <= hora_inicio:
                raise ValidationError("A hora de término deve ser após a hora de início.")

        if sala and not sala.disponivel:
            raise ValidationError("Esta sala já está reservada e não está disponível.")

        return cleaned_data