from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from django.core.paginator import Paginator
from django.db.models import Q
# Usuários
from apps.usuarios.models import Usuario
from apps.cursos.models import Area, PublicoAlvo, Curso
from .forms import UsuarioFormCadastro
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Min, Max, Avg, Sum

def transparencia(request):
    qtd_areas = Area.objects.count()
    qtd_publicos = PublicoAlvo.objects.count()
    qtd_cursos = Curso.objects.count()
    hoje = date.today()
    cursos_a_iniciar = Curso.objects.filter(data__gt=hoje).count()
    cursos_iniciados = Curso.objects.filter(data__lte=hoje).count()
    cursos_sem_data = Curso.objects.filter(data__isnull=True).count()
    
    cursos_iniciar = Curso.objects.filter(data__lte=hoje)

    vagas_iniciar = 0
    for curso in cursos_iniciar:
        vagas_iniciar = vagas_iniciar + curso.vagas
    
    menor_ch = Curso.objects.order_by('ch').first().ch

    maior_ch = Curso.objects.order_by('ch').last().ch
    maior_ch = Curso.objects.order_by('-ch').first().ch

    todos_cursos = Curso.objects.all()

    soma_ch = 0
    for curso in todos_cursos:
        soma_ch += curso.ch
    
    media_ch = soma_ch / qtd_cursos

    resumo = Curso.objects.aggregate(
        ch_menor = Min('ch'),
        ch_maior = Max('ch'),
        ch_media =Avg('ch'),
        ch_total = Sum('ch')
    )

    cursos_ch = Curso.objects.all().order_by('-ch')   

    context = {
        'qtd_areas': qtd_areas,
        'qtd_publicos': qtd_publicos,
        'qtd_cursos': qtd_cursos,
        'cursos_a_iniciar': cursos_a_iniciar,
        'cursos_iniciados': cursos_iniciados,
        'cursos_sem_data': cursos_sem_data,
        'vagas_iniciar': vagas_iniciar,
        'menor_ch': menor_ch,
        'maior_ch': maior_ch,
        'media_ch': media_ch,
        'resumo': resumo,
        'cursos_ch': cursos_ch
    }
    return render(request, 'transparencia.html', context)

def cadastro(request):
    form = UsuarioFormCadastro(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'privado/cadastro.html', context)

def autenticar(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'privado/login.html')
    else:
        return render(request, 'privado/login.html')
    
def sair(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def curso_galeria(request):
    busca = request.GET.get('busca', '')
    areas_marcadas = request.GET.getlist('area')
    publicos_marcados = request.GET.getlist('publico')

    cursos = Curso.objects.all().order_by('titulo')
    if busca:
        cursos = cursos.filter(Q(titulo__icontains=busca) | Q(descricao__icontains=busca))
    if areas_marcadas:
        cursos = cursos.filter(area__in=areas_marcadas)
    if publicos_marcados:
        cursos = cursos.filter(publicos__in=publicos_marcados).distinct()

    paginator = Paginator(cursos, 9)
    pagina = paginator.get_page(request.GET.get('page'))

    # querystring sem o 'page', para os links da paginação manterem os filtros
    filtros = request.GET.copy()
    filtros.pop('page', None)

    context = {
        'pagina': pagina,
        'filtros': filtros.urlencode(),
        'areas': Area.objects.all(),
        'publicoalvos': PublicoAlvo.objects.all(),
        'busca': busca,
        'areas_marcadas': areas_marcadas,
        'publicos_marcados': publicos_marcados,
    }
    return render(request, 'curso_galeria.html', context)

def curso_detalhes(request, id):
    curso = Curso.objects.get(pk=id)
    context = {
        'curso': curso
    }
    return render(request, 'curso_detalhe.html', context)