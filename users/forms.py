# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect(f"{reverse('login')}?username={username}")
    else:
        form = UserCreationForm()  
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')