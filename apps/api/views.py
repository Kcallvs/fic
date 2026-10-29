from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.cursos.models import Area, PublicoAlvo, Curso
from .serializers import AreaSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UsuarioSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def entrar(request):
    usuario = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
    if usuario is None:
        return Response({'detail': 'Usuário ou senha inválidos.'}, status=status.HTTP_401_UNAUTHORIZED)
    login(request, usuario)
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)

@api_view(['POST'])
def sair(request):
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def areas(request):
    todas_areas = Area.objects.all().order_by('nome')
    serializer = AreaSerializer(todas_areas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def area_cadastrar(request):
    serializer = AreaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def area_atualizar(request, id):
    area = Area.objects.get(pk=id)
    serializer = AreaSerializer(area, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def area_deletar(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def olamundo(request):
    return Response({'mensagem': 'Olá Mundo!'})


@api_view(['GET'])
def instituicao(request):
    return Response({
        'nome': 'IFRN',
        'campus': 'Cang',
        'Cidade': 'Canguaretama',
        'Anos': 12
    })

@api_view(['GET'])
def materias(request):
    return Response([
        {'nome': 'Teste', 'ch': 60},
        {'nome': 'Corporativas', 'ch': 120},
        {'nome': 'Implantação', 'ch': 60}
    ])

@api_view(['POST'])
def receber1(request):
    dados = request.data
    print(dados)
    print(dados['nome'])
    print(dados['disciplina'])
    return Response({'mensagem': 'recebeu'})

@api_view(['GET'])
def areas_lista(request):
    areas = Area.objects.all()
    dados = []
    for area in areas:
        dados.append({'id': area.id, 'nome': area.nome})
    
    return Response(dados)

@api_view(['GET'])
def publicos_lista(request):
    publicos = PublicoAlvo.objects.all().order_by()
    dados = []
    for publico in publicos:
        dados.append({'id': publico.id, 'nome': publico.nome})
    return Response(dados)
