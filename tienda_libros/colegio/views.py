from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrera, Estudiante, Nota
from .forms import CarreraForm, EstudianteForm, NotaForm


def ver_carreras(request):
    return render(request, 'colegio/lista.html', {
        'titulo': 'Carreras',
        'datos': Carrera.objects.all(),
        'url_crear': 'crear_carrera',
        'url_editar': 'editar_carrera',
        'url_borrar': 'borrar_carrera',
    })

def crear_carrera(request):
    form = CarreraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ver_carreras')
    return render(request, 'colegio/formulario.html', {'form': form, 'volver': 'ver_carreras'})

def editar_carrera(request, id):
    obj = get_object_or_404(Carrera, id=id)
    form = CarreraForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ver_carreras')
    return render(request, 'colegio/formulario.html', {'form': form, 'volver': 'ver_carreras'})

def borrar_carrera(request, id):
    obj = get_object_or_404(Carrera, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_carreras')
    return render(request, 'colegio/borrar.html', {'obj': obj, 'volver': 'ver_carreras'})


def ver_estudiantes(request):
    return render(request, 'colegio/lista.html', {
        'titulo': 'Estudiantes',
        'datos': Estudiante.objects.all(),
        'url_crear': 'crear_estudiante',
        'url_editar': 'editar_estudiante',
        'url_borrar': 'borrar_estudiante',
    })

def crear_estudiante(request):
    form = EstudianteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ver_estudiantes')
    return render(request, 'colegio/formulario.html', {'form': form, 'volver': 'ver_estudiantes'})

def editar_estudiante(request, id):
    obj = get_object_or_404(Estudiante, id=id)
    form = EstudianteForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ver_estudiantes')
    return render(request, 'colegio/formulario.html', {'form': form, 'volver': 'ver_estudiantes'})

def borrar_estudiante(request, id):
    obj = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_estudiantes')
    return render(request, 'colegio/borrar.html', {'obj': obj, 'volver': 'ver_estudiantes'})


def ver_notas(request):
    return render(request, 'colegio/lista.html', {
        'titulo': 'Notas',
        'datos': Nota.objects.all(),
        'url_crear': 'crear_nota',
        'url_editar': 'editar_nota',
        'url_borrar': 'borrar_nota',
    })

def crear_nota(request):
    form = NotaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ver_notas')
    return render(request, 'colegio/formulario.html', {'form': form, 'volver': 'ver_notas'})

def editar_nota(request, id):
    obj = get_object_or_404(Nota, id=id)
    form = NotaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ver_notas')
    return render(request, 'colegio/formulario.html', {'form': form, 'volver': 'ver_notas'})

def borrar_nota(request, id):
    obj = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_notas')
    return render(request, 'colegio/borrar.html', {'obj': obj, 'volver': 'ver_notas'})