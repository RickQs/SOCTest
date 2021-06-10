from typing import Tuple
from django.db import models


class Exames(models.Model):

    paciente = models.CharField(max_length=100, unique=True)
    exame = models.CharField(max_length=100)
    data = models.DateTimeField()
    resultado = models.CharField(max_length=250, blank=True, null=True)