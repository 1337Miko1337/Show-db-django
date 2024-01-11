from django.forms import ModelForm, TextInput

from .models import city


class Addcity(ModelForm):
    class Meta:
        model = city
        fields = ['region', 'name']
        widgets = {'region': TextInput(attrs={
            'placeholder': 'region'}),
            'name': TextInput(attrs={'placeholder': 'city name'})
        }
