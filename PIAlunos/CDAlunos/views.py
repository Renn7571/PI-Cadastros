from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import CadastroAluno
from .forms import cadastrar 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def base(request):
    return render(request, 'base.html')

def pagina_cadastro(request):
    if request.method == 'GET':
        form = cadastrar()
        return render(request, 'cadastro.html', {'form': form})
    elif request.method == 'POST':
        form = cadastrar(request.POST)
        if form.is_valid():
            form_nome = form.cleaned_data['nome']
            form_cpf = form.cleaned_data['cpf']
            form_email = form.cleaned_data['email']
            form_idade = form.cleaned_data['idade']
            form_telefone = form.cleaned_data['telefone']
            form_mensagem = form.cleaned_data['mensagem']
            from_senha = form.cleaned_data['senha']
            from_username = form.cleaned_data['username']
        else:
            return HttpResponse('Dados inválidos')
        
        user = User.objects.create_user(from_username, form_email, from_senha)
        user.first_name = form_nome
        user.save()
        cadastro = CadastroAluno(user=user, idade=form_idade, cpf=form_cpf, telefone=form_telefone, mensagem=form_mensagem)
        cadastro.save()
        login(request, user)
        return redirect('/concorrentes')
    else:
        return HttpResponseBadRequest()
    
def mostrar_cadastros(request):
    alunos = CadastroAluno.objects.all()
    return render(request, 'post_details.html', {
        'alunos': alunos
    })