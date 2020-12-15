from django import forms
from .models import Avalista


class AvalistaForm(forms.ModelForm):
    class Meta:
        model = Avalista
        fields = '__all__'
