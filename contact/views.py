from django.shortcuts import render
from .tasks import send_email
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        template = render_to_string('contact/contact_mail.html', {'name': name,
                                                                  'email': email,
                                                                  'message': message})

        send_email.delay(template)
        messages.add_message(request, messages.SUCCESS, 'Message sent successfully!')

    return render(request, 'contact/contact.html')