from django import forms
from .models import Photographs, Albums

class UploadPhotograph(forms.ModelForm):
    class Meta:
        model = Photographs
        fields = ['title', 'description', 'photograph']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = ['name', 'description']