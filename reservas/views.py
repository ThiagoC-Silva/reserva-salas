from django.forms import ValidationError
from django.shortcuts import get_object_or_404, render, redirect
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
            reserva.full_clean()  
            reserva.save()
            messages.success(request, 'Reserva realizada com sucesso!')
        except ValidationError as e:
            for field, errors in e.message_dict.items():
                for error in errors:
                    if field == '__all__':
                        messages.error(request, error)  
                    else:
                        messages.error(request, f"{field}: {error}")
        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao realizar a reserva. Tente novamente.')

        return redirect('dashboard')
    else:
        return redirect('dashboard')
    
@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    reserva.delete()
    messages.success(request, 'Reserva cancelada com sucesso!')
    return redirect('dashboard')