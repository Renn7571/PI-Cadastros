from django.contrib import admin
from . import models

@admin.register(models.CadastroAluno)
class CadastroAlunoAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'telefone', 'mensagem']

# Register your models here.
