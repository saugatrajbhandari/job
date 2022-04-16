from django import forms

from .models import Salary


class SalaryModelForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SalaryModelForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['salary'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['company_website'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['position'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['employee_status'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['experience'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control mb-3'})