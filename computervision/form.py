from django import forms
from .models import UrineStrip

class uploadForm(forms.ModelForm):
    class Meta:
        model = UrineStrip
        fields = ['image']
