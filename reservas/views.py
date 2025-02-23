from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reserva, Sala

@login_required
def criar_reserva(request):
    if request.method == 'POST':
        sala_id = request.POST.get('sala')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')

        try:
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
        except ValidationError as e:
            messages.error(request, e.message)
        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao realizar a reserva.')

        return redirect('dashboard')
    else:
        return redirect('dashboard')