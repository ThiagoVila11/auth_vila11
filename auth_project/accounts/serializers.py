from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'usuarioNome', 'usuarioEmail', 
                 'usuarioTelefone', 'usuarioDataNascimento', 'usuarioAtivo']
        extra_kwargs = {
            'password': {'write_only': True},
            'usuarioEmail': {'required': True}
        }
    
    def create(self, validated_data):
        # Extrai a senha do dicionário validated_data
        password = validated_data.pop('password')
        
        # Cria o usuário com os demais campos
        usuario = Usuario(**validated_data)
        
        # Usa set_password para hash da senha (não usar make_password diretamente)
        usuario.set_password(password)
        
        # Salva o usuário
        usuario.save()
        
        return usuario