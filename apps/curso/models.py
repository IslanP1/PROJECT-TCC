from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    MODALIDADE = (
        ('B', 'Bacharelado'),
        ('L', 'Licenciatura'),
        ('T', 'Tecnológico'),
    )

    nome = models.CharField(max_length=150)
    modalidade = models.CharField(choices=MODALIDADE, max_length=150)

    # class Meta():
    #     ordering = ['nome']

    def __str__(self):
        return self.nome