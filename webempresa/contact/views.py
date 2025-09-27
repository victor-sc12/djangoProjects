from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contac_form = ContactForm()

    if request.method == 'POST':
        contac_form = ContactForm(data=request.POST)
        if contac_form.is_valid():
            name = request.POST.get('name', '') 
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Considerando que todos los datos ingresados en el form son correctos:
            # return redirect(reverse('contacto') + '?ok')

            # Envió del correo y redirección al form:
            email_message = EmailMessage(
                'La Caffetiera: New Message',
                f'De {name} <{email}>\n\nEscribió:\n\n{content}',
                'no-contestar@inbox.mailtrap.io',
                ["victor.suquilanda@udla.edu.ec"],
                reply_to=[email]
            )
            try:
                email_message.send()
                return redirect(reverse('contacto') + '?ok')
            except:
                return redirect(reverse('contacto') + '?fail')

    return render(request, 'contact/contact.html', {'form':contac_form})