from rest_framework import serializers
from apps.cursos.models import Area, PublicoAlvo, Curso
from apps.usuarios.models import Usuario

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id','nome']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf', 'username', 'first_name', 'last_name', 'email', 'nascimento']
        read_only_fields = ['cpf']