from django.urls import path
from .views import *

urlpatterns = [
    path('olamundo/', olamundo, name='olamundo'),
    path('instituicao/', instituicao, name='instituicao'),
    path('materias/', materias, name='materias'),
    path('receber1/', receber1, name='receber1'),
    path('areas_lista/', areas_lista, name='areas_lista'),
    path('publicos_lista/', publicos_lista, name='publicos_lista'),

    path('areas/', areas, name='areas'),
    path('area_cadastrar/', area_cadastrar, name='area_cadastrar'),
    path('area_atualizar/<int:id>/', area_atualizar, name='area_atualizar'),

    path('area_deletar', area_deletar, name='area_deletar'),
    
    path('login/', entrar, name='api_login'),
    path('logout/', sair, name='api_logout'),


    
    
]