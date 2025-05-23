from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('usuarioNome', 'usuarioEmail', 'usuarioTelefone', 'usuarioDataNascimento', 
                  'usuarioAtivo', 'usuarioFuncao')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('usuarioNome', 'usuarioEmail', 'usuarioTelefone', 'usuarioDataNascimento', 
                  'usuarioAtivo', 'usuarioFuncao')
