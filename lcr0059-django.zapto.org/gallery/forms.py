from django import forms
from .models import Artist, Artwork

class CreateArtist(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class CreateArtwork(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = '__all__'