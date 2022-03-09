from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import (validate_password, MinimumLengthValidator,
                                                     CommonPasswordValidator, UserAttributeSimilarityValidator,
                                                     NumericPasswordValidator)
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'login-email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class UserRegistrationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
    }

    email = forms.EmailField(help_text='Required',
                             error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label="Password", max_length=255,
                               widget=forms.PasswordInput,
                               validators=[MinimumLengthValidator],
                               )
    password2 = forms.CharField(label="Repeat Password",
                                max_length=255,
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
            raise forms.ValidationError(self.error_messages['password_mismatch'])
        return cd['password2']


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists!')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control mb', 'placeholder': 'Repeat Password'})
