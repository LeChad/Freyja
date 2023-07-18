from django import forms
from .models import Photographs, Albums, AlbumContents

class UploadPhotograph(forms.ModelForm):
    class Meta:
        model = Photographs
        fields = ['title', 'description', 'photograph']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = ['name', 'description']


class AlbumContent(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AlbumContent, self).__init__(*args, **kwargs)
        self.fields['albumSelection'].queryset = Albums.objects.filter(created_by_id=user)
    def save(self, commit=True):
        instance = super(AlbumContent, self).save(commit=False)
        instance.photograph_id = self.request.POST.get('photograph_id')
        if commit:
            instance.save()
        return instance
    class Meta:
        model = AlbumContents
        fields = []

    albumSelection = forms.ModelChoiceField(
        queryset=None,
        empty_label=None
    )
