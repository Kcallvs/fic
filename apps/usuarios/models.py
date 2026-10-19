from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=11, primary_key=True)
    email = models.CharField('E-mail', max_length=200, unique=True)
    nascimento = models.DateField('Data de Nascimento', null=True, blank=True)

    REQUIRED_FIELDS =['cpf']

    def __str__(self):
        return self.cpf

