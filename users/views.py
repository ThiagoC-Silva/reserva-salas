from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reservas.models import Reserva, Sala

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

from reservas.models import Sala

@login_required
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    salas = Sala.objects.all()
    minhas_reservas = Reserva.objects.filter(usuario=request.user)
    outras_reservas = Reserva.objects.exclude(usuario=request.user)

    return render(request, 'users/dashboard.html', {
        'user': request.user,
        'salas': salas,
        'minhas_reservas': minhas_reservas,
        'outras_reservas': outras_reservas,
    })

def logout_view(request):
    logout(request)
    return redirect('login')