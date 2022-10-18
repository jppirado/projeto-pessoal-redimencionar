from django import forms
from .models import tratarImagem


class ImagemModelForm( forms.ModelForm ):
    class Meta:
        model = tratarImagem
        fields= ('imagem' , )
