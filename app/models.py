from django.db import models

# Create your models here.

class tratarImagem(models.Model):
    imagem = models.ImageField("Imagem" , upload_to ='uploads/')
