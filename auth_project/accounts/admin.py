from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['usuarioNome', 'usuarioEmail', 'usuarioTelefone', 'usuarioDataNascimento', 'usuarioAtivo']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('usuarioNome', 'usuarioEmail')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('usuarioNome', 'usuarioEmail')}),
    )

admin.site.register(Usuario, CustomUserAdmin)