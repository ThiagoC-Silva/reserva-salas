from django.shortcuts import render, redirect
from reserva_salas.models import Sala, Reserva
from reserva_salas.forms import ReservaForm

def dashboard(request):
    salas = Sala.objects.all()
    reservas = Reserva.objects.all()
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ReservaForm()
    return render(request, 'reserva_salas/dashboard.html', {'salas': salas, 'reservas': reservas, 'form': form})