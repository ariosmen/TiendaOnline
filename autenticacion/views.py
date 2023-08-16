from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

class Registro(View):
    
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'autenticacion/autenticacion.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request, 'autenticacion/autenticacion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def logear(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'Usuario no valido')
        else:
            messages.error(request, 'Informacion incorrecta')
            
    form = AuthenticationForm()
    return render(request, 'autenticacion/login.html', {'form': form})
    