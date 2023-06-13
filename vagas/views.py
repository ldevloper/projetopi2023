from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Vaga, Cliente, Empresa
from .forms import EmpresaForm, ClienteForm, VagaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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


    

    

