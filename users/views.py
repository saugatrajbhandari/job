from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .tokens import account_activation_token
from .models import User
from .forms import (UserRegistrationForm, )
from django.contrib.auth.views import LogoutView as Logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async
import asyncio


async def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if await sync_to_async(form.is_valid)():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            await sync_to_async(user.save)()
            current_site = await sync_to_async(get_current_site)(request)
            subject = 'Activate your Account'
            message = render_to_string('accounts/registration/account_activation_email.html',
                                       {
                                           'user': user,
                                           'domain': current_site.domain,
                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                           'token': account_activation_token.make_token(user),
                                           })
            send_email = sync_to_async(user.email_user)
            asyncio.create_task(send_email(subject=subject, message=message))
            # user.email_user(subject=subject, message=message)
            return HttpResponse('registered successfully and activation sent')

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('success')
    else:
        return render(request, 'account/registration/activation_invalid.html')


class LogoutView(LoginRequiredMixin, Logout):
    pass


def check_email(request):
    email = request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("<div style='color:red;'>Email already exists </div>")
    else:
        return HttpResponse("<div style='color:green;'>Email is available </div>")
