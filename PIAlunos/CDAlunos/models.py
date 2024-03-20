from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CadastroAluno(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    idade = models.CharField(max_length=3)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    mensagem = models.CharField(max_length=500)
    aprovado = models.BooleanField(default=False)
    