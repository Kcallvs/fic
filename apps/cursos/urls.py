from django.urls import path
from .views import *

urlpatterns = [
    
    path('area_listar/', area_listar, name='area_listar'),
    path('area_cadastrar/', area_cadastrar, name='area_cadastrar'),
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),

    path('publicoalvo_listar/', publicoalvo_listar, name='publicoalvo_listar'),
    path('publicoalvo_cadastrar/', publicoalvo_cadastrar, name='publicoalvo_cadastrar'),
    path('publicoalvo_editar/<int:id>/', publicoalvo_editar, name='publicoalvo_editar'),
    path('publicoalvo_remover/<int:id>/', publicoalvo_remover, name='publicoalvo_remover'),

    path('curso_listar/', curso_listar, name='curso_listar'),
    path('curso_cadastrar/', curso_cadastrar, name='curso_cadastrar'),
    path('curso_editar/<int:id>/', curso_editar, name='curso_editar'),
    path('curso_remover/<int:id>/', curso_remover, name='curso_remover'),

]