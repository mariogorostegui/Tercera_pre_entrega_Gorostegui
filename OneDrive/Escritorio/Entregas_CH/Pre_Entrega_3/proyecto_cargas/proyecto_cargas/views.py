from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from app_seg_cargas.models import Usuarios,Agentes,Cargas


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