from datetime import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

from app_seg_cargas.models import Usuarios,Agentes,Cargas

from app_seg_cargas.forms import UsuarioFormulario


def saludo(request):
	return HttpResponse('Hola a Proyecto Cargas2')


def saludar_con_html(request):
    contexto = { }
    http_responde = render(
        request=request,
        template_name='proyecto_cargas/base.html',
        context=contexto,
    )
    return http_responde

def inicio (request):
    contexto = {}
    
    http_responde= render(
        request=request,
        template_name= 'proyecto_cargas/index.html',
        context = contexto,
    )
    return http_responde




def lista_agentes (request):
    contexto = {
        "agentes": Agentes.objects.all(),
     }
    
    http_responde= render(
        request=request,
        template_name= 'proyecto_cargas/lista_agentes.html',
        context = contexto,
    )
    return http_responde


def lista_usuarios (request):
    contexto = {
        "usuarios": Usuarios.objects.all(),
     }
    
    http_responde= render(
        request=request,
        template_name= 'proyecto_cargas/lista_usuarios.html',
        context = contexto,
    )
    return http_responde

def lista_guias (request):
    contexto = {
        "shipments": Cargas.objects.all(),
     }
    
    http_responde= render(
        request=request,
        template_name= 'proyecto_cargas/lista_guias.html',
        context = contexto,
    )
    return http_responde


def crear_usuario (request):
    
    if request.method== "POST":
        formulario = UsuarioFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            area = data["area"]
            New_user = Usuarios.objects.create(nombre=nombre,apellido=apellido,area=area)
            New_user.save()
        
            url_exitosa = reverse ("Usuarios")
            return redirect(url_exitosa)
    else:
        formulario = UsuarioFormulario()
  
        http_responde=render(
            request = request,
            template_name= 'proyecto_cargas/form_usuarios.html',
            context = {'formulario':formulario}
        )
    return http_responde


def buscar_fwr(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       cargas = Cargas.objects.filter(abrev_fwr__contains=busqueda)
       contexto = {
           "cargas": cargas,
       }
       http_response = render(
           request=request,
           template_name='proyecto_cargas/buscar_cargas.html',
           context=contexto,
       )
       return http_response