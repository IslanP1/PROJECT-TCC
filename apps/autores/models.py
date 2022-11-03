from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    
    primeiro_nome = models.CharField(max_length=150)
    ultimo_nome = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='fotos/')
  

    def __str__(self):
        return self.primeiro_nome

