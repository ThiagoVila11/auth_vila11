from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(AbstractUser):
    # Campos adicionais podem ser adicionados aqui
    usuarioNome = models.CharField(max_length=100, blank=True)
    usuarioEmail = models.EmailField(verbose_name="E-mail",
                                    max_length=255,
                                    unique=True,  # Opcional: para garantir emails únicos
                                    validators=[EmailValidator(message="Digite um e-mail válido")],
                                    help_text="Exemplo: usuario@provedor.com")
    usuarioTelefone = models.CharField(max_length=20, blank=True)
    usuarioDataNascimento = models.DateField(null=True, blank=True)
    usuarioAtivo = models.CharField(max_length=1,default='A')
    usuarioSenhaHash = models.CharField(max_length=128, null=True, blank=True)

    def set_senha(self, senha):
        """Armazena o hash da senha, não a senha em si"""
        self.usuarioSenhaHash = make_password(senha)
    
    def check_senha(self, senha):
        """Verifica se a senha está correta"""
        return check_password(senha, self.usuarioSenhaHash)

    def __str__(self):
        return self.usuarioNome
