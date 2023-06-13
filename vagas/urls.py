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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import  listar_vagas, detalhar_vaga, realizar_cadastro_emp, realizar_cadastro, deletar_vaga, dar_like,criar_vaga

urlpatterns = [
    path('vagas/', listar_vagas, name='listar_vagas'),
    path('vagas/<str:pk>', detalhar_vaga, name='detalhar_vaga'),
    path('criar_vaga/', criar_vaga, name='criar_vaga'),
    path('clientes/cadastrar',realizar_cadastro, name='realizar_cadastro'),
    path('empresa/cadastrar',realizar_cadastro_emp, name='cadastrar_empresa'),
    path('deletar_vaga/<int:id>/', deletar_vaga, name='deletar_vaga'),
    path('criar_vaga/', criar_vaga, name='criar_vaga'),
    path('detalhar_vaga/<int:vaga_id>/like', dar_like, name='like_vaga'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)