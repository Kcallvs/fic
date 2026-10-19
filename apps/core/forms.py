from django import forms
from apps.usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioFormCadastro(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'cpf',
            'email',
            'nascimento',
            'first_name',
            'last_name',
            'username'
        ]