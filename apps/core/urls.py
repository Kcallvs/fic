from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('curso_galeria/', curso_galeria, name='curso_galeria'),
    path('curso_detalhes/<int:id>/', curso_detalhes, name='curso_detalhes'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', autenticar, name='login'),
    path('sair/', sair, name='sair'),
    path('transparencia/', transparencia, name='transparencia'),
]