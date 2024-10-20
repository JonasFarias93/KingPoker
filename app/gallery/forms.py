from django import forms
from .models import Image  # Importa o modelo Image

class ImageForm(forms.ModelForm):
    image_file = forms.FileField()  # Campo para o upload do arquivo

    class Meta:
        model = Image
        fields = ['title', 'image_file']  # Use o campo de arquivo aqui
