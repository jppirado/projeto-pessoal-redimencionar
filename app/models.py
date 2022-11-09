from django.db import models

import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

class tratarImagem(models.Model):
    imagem = models.ImageField("Imagem" , upload_to ='uploads/')
    x = models.IntegerField("Largura" , null=True)
    y = models.IntegerField("Altura" , null=True)
    

    def save(self, *args, **kwargs):
        imageTemproary = Image.open(self.imagem)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (self.x ,self.y) ) 
        imageTemproaryResized.save(outputIoStream , format='JPEG', quality=150)
        outputIoStream.seek(0)
        self.imagem = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" %self.imagem.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        super(tratarImagem, self).save(*args, **kwargs)
        

