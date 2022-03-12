from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber


# Create your views here.
def subscriber_view(request):
    email = request.POST.get('email')
    if Subscriber.objects.filter(email=email).exists():
        messages.add_message(request, messages.ERROR, 'Subscriber already exits')
        return redirect('home')
    Subscriber.objects.create(email=email)
    return redirect('home')