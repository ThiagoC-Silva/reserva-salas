from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reserva, Sala
from django.contrib import messages

@login_required
def criar_reserva(request):
    if request.method == 'POST':
        sala_id = request.POST.get('sala')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')

        sala = Sala.objects.get(id=sala_id)
        reserva = Reserva(
            usuario=request.user,
            sala=sala,
            data=data,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim
        )
        reserva.save()
        messages.success(request, 'Reserva realizada com sucesso!')
        return redirect('dashboard')
    else:
        return redirect('dashboard')