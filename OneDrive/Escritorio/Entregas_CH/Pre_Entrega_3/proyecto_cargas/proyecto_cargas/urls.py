"""
URL configuration for proyecto_cargas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  

from proyecto_cargas.views import saludo, saludar_con_html,inicio,lista_usuarios,lista_agentes,lista_guias,crear_usuario,buscar_fwr


urlpatterns = [
    path('',inicio,name="Inicio"),
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('saludar/', saludar_con_html),    
    path('lst_usuarios/',lista_usuarios,name="Usuarios"),
    path('lst_agentes/',lista_agentes,name="Agentes"),
    path('lst_cargas/',lista_guias,name="Cargas"),
    path('crear-usuario/',crear_usuario,name="crear_usuario"),
    path("buscar-cargas/", buscar_fwr, name="buscar_fwr"),
]
