from django.urls import path
from . import views
from .views import UsuarioCreateAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('api/usuarios/cadastrar/', UsuarioCreateAPIView.as_view(), name='cadastrar-usuario'),
    path('api/login/', obtain_auth_token, name='api-login'),  # Para login e obtenção de token
]
