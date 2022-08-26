from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
# Create your views here.

def curso(request):
    return render(request,"AppCoder/cursos.html")

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")