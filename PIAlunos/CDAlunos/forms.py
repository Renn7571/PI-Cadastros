from django import forms

class cadastrar(forms.Form):
    username = forms.CharField(max_length=200)
    nome = forms.CharField(max_length=200)
    idade = forms.CharField(max_length=3)
    cpf = forms.CharField(max_length=11)
    email = forms.EmailField(max_length=200)
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput) 
    telefone = forms.CharField(max_length=11)
    mensagem = forms.CharField(max_length=500)
