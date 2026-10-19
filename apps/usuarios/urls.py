from django.urls import path
from .views import *

urlpatterns = [
    path('perfil/', perfil, name='perfil'),
    path('meus_dados/', meus_dados, name='meus_dados'),

    path('usuarios_listar', usuarios_listar, 
         name='usuarios_listar'),

    path('usuario_editar/<str:cpf>/', usuario_editar,
         name='usuario_editar'),
]