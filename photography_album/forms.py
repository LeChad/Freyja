from django import forms
from .models import Photographs

class UploadPhotograph(forms.ModelForm):
    class Meta:
        model = Photographs
        fields = ['title', 'description', 'photograph']
