from django import forms
from django.forms import ModelForm
from .models import Event
import datetime

class DateForm(forms.ModelForm):
    start_of_interval = forms.DateField()
    end_of_interval = forms.DateField()
    class Meta:
        model = Event
        exclude = ('dt_of_start', 'dt_of_end')
        fields = ('dt_of_start', 'dt_of_end')