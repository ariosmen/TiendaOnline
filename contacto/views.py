from django.shortcuts import render
from contacto.forms import FormularioContacto
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def contacto(request):
    
    if request.method == 'POST':
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            valid = True
            
            #PRIMER VARIANTE
            info = miFormulario.cleaned_data
            send_mail(info['asunto'], info['mensaje'], info.get('email', ''), ['arielmendezcantautor@gmail.com'], )
            return render(request, 'contacto/formulario_contacto.html', {'valid': valid, 'form': miFormulario})
            
            #SEGUNDA VARIANTE
            # nombre = request.POST.get('nombre')
            # asunto = request.POST.get('asunto')
            # email = request.POST.get('email')
            # mensaje = request.POST.get('mensaje')
            # email = EmailMessage(f'{asunto}', f'El usuario {nombre} con la direccion {email} escribe lo siguiente:\n\n {mensaje}', '', ['arielmendezcantautor@gmail.com'], ).send()
            # try:
            #     return render(request, 'contacto/formulario_contacto.html', {'valid': valid, 'form': miFormulario})
            # except:
            #     valid=False
            #     return render(request, 'contacto/formulario_contacto.html', {'valid': valid})
            
    else:
        miFormulario = FormularioContacto()
    
    return render(request, 'contacto/formulario_contacto.html', {'form': miFormulario})