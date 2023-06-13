from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Vaga, Cliente, Empresa
from .forms import EmpresaForm, ClienteForm, VagaForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from .serializers import VagaModelSerializer, EmpresaModelSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import viewsets


# Create your views here.
def index(request):
    return render(request, "index.html")

def listar_vagas(request):
    vagas = Vaga.objects.all()
    context = {"vagas": vagas}
    return render(request, "vagas/listar_vagas.html", context)

def detalhar_vaga(request, pk):
    vaga = Vaga.objects.get(pk=pk)
    context = {"vaga": vaga}
    return render (request, "vaga/detalhar_vaga.html", context)

class EmpresaDetailView(DetailView):
    model = Empresa
    template_name =  "detalhar_empresa.html"
    context_object_name = "empresa"
    pk_url_kwarg = 'id'

def realizar_cadastro(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ClienteForm()
            return render(request, "cliente/realizar_cadastro.html", {'form': form})
    else:
        form = ClienteForm()
        return render(request, "cliente/realizar_cadastro.html", {'form': form})
    
def realizar_cadastro_emp(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = EmpresaForm()
            return render(request, "empresa/cadastrar_empresa.html", {'form': form})
    else:
        form = EmpresaForm()
        return render(request, "empresa/cadastrar_empresa.html", {'form': form})
    
@login_required
def criar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            vaga = form.save()
            return redirect('/')
    else:
        form = VagaForm()
    return render(request, 'criar_vaga.html', {'form': form})

class VagaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'criar_vaga.html'
    model = Vaga
    form_class = VagaForm
    success_url = "/"
       
@login_required
def atualizar_vaga(request, id):
    vaga = get_object_or_404(Vaga, pk=id)
    form = VagaForm(instance=vaga)
    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            vaga = form.save()
            return redirect('/')
        else:
            return render(request, 'atualizar_vaga.html', {'form': form, 'vaga': vaga})
    else:
        return render(request, 'atualizar_vaga.html', {'form': form, 'vaga': vaga})
    
@login_required        
def deletar_vaga(request, id):
    vaga = get_object_or_404(Vaga, pk=id)
    vaga.delete()
    return redirect('/')

def dar_like(request, vaga_id):
    vaga = get_object_or_404(Vaga, pk=vaga_id)
    if request.method == 'GET':
        vaga.likes += 1
        vaga.save()
        return redirect(reverse_lazy("detalhar_vaga", args=[vaga.pk]))
    else:
        return redirect(reverse_lazy("detalhar_vaga", args=[vaga.pk]))

    
class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = User
    form_class = UserCreationForm
    success_url = "/"

class VagaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Vaga.objects.all()
    serializer_class = VagaModelSerializer

    @action(methods=['get'], detail=True)
    def likes(self, request, pk=None):
        vaga = get_object_or_404(Vaga, pk=pk)
        vaga.likes += 1
        vaga.save()

        return Response(VagaModelSerializer(vaga, many=False).data)
    
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaModelSerializer
