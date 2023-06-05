"""
URL configuration for THEjobfinder project.

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
from django.contrib import path
from .views import  listar_vagas, detalhar_carro, realizar_aluguel, realizar_cadastro, register

urlpatterns = [
    path('vagas/', listar_vagas, name='listar_vagas'),
    path('vagas/<str:pk>', detalhar_vaga, name='detalhar_vaga'),
    path('aluguel/',realizar_aluguel, name='realizar_aluguel'),
    path('clientes/cadastrar',realizar_cadastro, name='realizar_cadastro'),
    path('empresa/cadastrar',realizar_cadastro, name='cadastrar_empresa'),
    path('registration', register, name= 'register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)