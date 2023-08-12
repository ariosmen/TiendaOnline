from django.shortcuts import render
from contacto.forms import FormularioContacto
from django.core.mail import send_mail

def contacto(request):
    
    if request.method == 'POST':
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            send_mail(info['asunto'], info['mensaje'], info.get('email', ''), ['arielmendezcantautor@gmail.com'], )
            return render(request, 'gestion/gracias.html')
    else:
        miFormulario = FormularioContacto()
    
    return render(request, 'contacto/formulario_contacto.html', {'form': miFormulario})