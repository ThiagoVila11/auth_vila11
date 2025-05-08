from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from rest_framework import generics, permissions
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class UsuarioCreateAPIView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]  # Permite que qualquer um se cadastre
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({
                'usuario': UsuarioSerializer(usuario, context=self.get_serializer_context()).data,
                'message': 'Usuário criado com sucesso'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Mensagem de erro
            pass
    return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

class UsuarioPorEmailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        nomeusuario = request.query_params.get('nomeusuario')
        if not nomeusuario:
            return Response({"erro": "E-mail não fornecido"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Usuario.objects.get(username=nomeusuario)
        except Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data, status=status.HTTP_200_OK)