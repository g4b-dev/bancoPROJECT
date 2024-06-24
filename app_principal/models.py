from django.db import models

# Create your models here.

from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return self.titulo

