from django import forms

from .models import Job

class DateInput(forms.DateInput):
    input_type = 'date'


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('slug', )
        widgets = {
            'apply_before': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['apply_before'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['education_level'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['no_of_vacancy'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['experience'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['specification'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['requirement'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['benefit'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['category'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['organization'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['location'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['salary'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['work_day'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['type'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['is_paid'].widget.attrs.update({'class': ' mb-3'})
        self.fields['duration'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['benefit'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['is_active'].widget.attrs.update({'class': ' mb-3'})