from django import forms

from .models import CompanyAccount


class CompanyAccountRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(label="Repeat Password", max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = CompanyAccount
        fields = '__all__'

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Password doesn\'t match!')


class CompanyAccountLoginForm(forms.ModelForm):
    class Meta:
        model = CompanyAccount
        fields = ['email', 'password']

