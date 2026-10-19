from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Area, PublicoAlvo, Curso
from .forms import AreaForm, PublicoAlvoForm, CursoForm
from django.contrib.auth.decorators import login_required

@login_required
def area_listar(request):
    paginator = Paginator(Area.objects.all().order_by('nome'), 10)
    pagina = paginator.get_page(request.GET.get('page'))
    context = {
        'pagina': pagina
    }
    #return render(request, 'areas.html', context)
    return render(request, 'privado/areas.html', context)

@login_required
def area_cadastrar(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('area_listar')
    context = {
        'form': form
    }
    #return render(request, 'area_cadastrar.html', context)
    return render(request, 'privado/area_cadastrar.html', context)

@login_required
def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('area_listar')
    context = {
        'form': form
    }
    #return render(request, 'area_cadastrar.html', context)
    return render(request, 'privado/area_cadastrar.html', context)

@login_required
def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('area_listar')

@login_required
def publicoalvo_listar(request):
    paginator = Paginator(PublicoAlvo.objects.all().order_by('nome'), 10)
    pagina = paginator.get_page(request.GET.get('page'))
    context = {
        'pagina': pagina
    }
    return render(request, 'privado/publicoalvos.html', context)

@login_required
def publicoalvo_cadastrar(request):
    form = PublicoAlvoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicoalvo_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/publicoalvo_cadastrar.html', context)

@login_required
def publicoalvo_editar(request, id):
    publicoalvo = PublicoAlvo.objects.get(pk=id)
    form = PublicoAlvoForm(request.POST or None, instance=publicoalvo)
    if form.is_valid():
        form.save()
        return redirect('publicoalvo_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/publicoalvo_cadastrar.html', context)

@login_required
def publicoalvo_remover(request, id):
    publicoalvo = PublicoAlvo.objects.get(pk=id)
    publicoalvo.delete()
    return redirect('publicoalvo_listar')

@login_required
def curso_listar(request):
    paginator = Paginator(Curso.objects.all().order_by('titulo'), 10)
    pagina = paginator.get_page(request.GET.get('page'))
    context = {
        'pagina': pagina
    }
    return render(request, 'privado/cursos.html', context)

@login_required
def curso_cadastrar(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('curso_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/curso_cadastrar.html', context)

@login_required
def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('curso_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/curso_cadastrar.html', context)

@login_required
def curso_remover(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('curso_listar')