from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
# Usuários
from .forms import UsuarioForm, UsuarioEditarForm
from django.contrib.auth.decorators import login_required
from .models import Usuario

@login_required
def perfil(request):
    return render(request, 'privado/perfil.html')

@login_required
def meus_dados(request):
    # A senha só é trocada se o usuário preencher os campos de senha
    trocar_senha = bool(request.POST.get('new_password1') or request.POST.get('new_password2'))
    form = UsuarioForm(request.POST or None, instance=request.user)
    form_senha = SetPasswordForm(request.user, request.POST if trocar_senha else None)
    if request.POST and form.is_valid() and (not trocar_senha or form_senha.is_valid()):
        form.save()
        if trocar_senha:
            form_senha.save()
            # mantém o usuário logado depois de trocar a senha
            update_session_auth_hash(request, request.user)
        return redirect('meus_dados')
    context = {
        'form': form,
        'form_senha': form_senha
    }
    return render(request, 'privado/meus_dados.html', context)

@login_required
def usuarios_listar(request):
    if request.user.is_superuser:
        usuarios = Usuario.objects.all()
        context = {
            'usuarios': usuarios
        }
        return render(request, 'privado/usuarios.html', context)
    else:
        return redirect('login')

@login_required
def usuario_editar(request, cpf):
    if request.user.is_superuser:
        usuario = Usuario.objects.get(pk=cpf)
        form = UsuarioEditarForm(request.POST or None,
                                    instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios_listar')
        context = {
            'form': form,
            'usuario': usuario
        }
        return render(request, 'privado/usuario_editar.html', context)
    else:
        return redirect('login')