from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'nascimento'
        ]
        # formato ISO para o <input type="date"> exibir o valor já salvo
        widgets = {
            'nascimento': forms.DateInput(format='%Y-%m-%d')
        }

class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'nascimento',
            'is_superuser'
        ]
        # formato ISO para o <input type="date"> exibir o valor já salvo
        widgets = {
            'nascimento': forms.DateInput(format='%Y-%m-%d')
        }

