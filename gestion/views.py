from django.shortcuts import render
from gestion.forms import FormularioContacto
from django.core.mail import send_mail
from servicios.models import Servicio

def home(request):
    return render(request, 'gestion/index.html')

def tienda(request):
    return render(request, 'gestion/tienda.html')

def blog(request):
    return render(request, 'gestion/blog.html')

def contacto(request):
    
    if request.method == 'POST':
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            send_mail(info['asunto'], info['mensaje'], info.get('email', ''), ['arielmendezcantautor@gmail.com'], )
            return render(request, 'gestion/gracias.html')
    else:
        miFormulario = FormularioContacto()
    
    return render(request, 'gestion/formulario_contacto.html', {'form': miFormulario})