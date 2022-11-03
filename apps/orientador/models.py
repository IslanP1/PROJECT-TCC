from django.db import models
from django.contrib.auth.models import User

class Orientador(models.Model):
    
    primeiro_nome = models.CharField(max_length=150)
    ultimo_nome = models.CharField(max_length=150)
    link_currilo_lattes = models.CharField(max_length=150)
  
    def __str__(self):
        return self.primeiro_nome

