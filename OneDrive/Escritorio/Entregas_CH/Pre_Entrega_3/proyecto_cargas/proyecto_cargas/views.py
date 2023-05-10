from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse



def saludo(request):
	return HttpResponse('Hola a Proyecto Cargas2')


def saludar_con_html(request):
    contexto = {
        "usuario": "Pedro"
    }
    http_responde = render(
        request=request,
        template_name='proyecto_cargas/base.html',
        context=contexto,
    )
    return http_responde