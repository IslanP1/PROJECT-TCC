from distutils.command.upload import upload
from django.db import models
from django.contrib.postgres.fields import *

class Trabalho(models.Model):
    autor = models.ForeignKey("autores.Autor", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150, default=None)
    orientador = models.ForeignKey("orientador.Orientador", on_delete=models.CASCADE)
    curso = models.ForeignKey("curso.Curso", on_delete=models.CASCADE)
    ano_documento = models.IntegerField(verbose_name = "Ano do Tcc", default=None)
    resumo = models.TextField(max_length=150, default=None)
    tcc = models.FileField(upload_to='tccs/', verbose_name="TCC")
    palavras_chave = ArrayField(models.CharField(max_length=200), blank=True)
   
    def __str__(self) -> str:
        return self.autor
    
    