from django.shortcuts import render,redirect
from .models import Vaga, Cliente, Empresa
from .forms import EmpresaForm, ClienteForm, VagaForm
from .admin import  CustomUserCreationForm
from .serializers import NoticiaModelSerializer, AutorModelSerializer
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def listar_vagas(request):
    vagas = Vaga.objects.all()
    context = {"vagas": vagas}
    return render(request, "vagas/listar_vagas.html", context)

def detalhar_vaga(request, pk):
    vagas = Vaga.objects.get(pk=pk)
    context = {"vaga": vaga}
    return render (request, "vaga/detalhar_vaga.html", context)
# Create your views here.
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
        noticia = get_object_or_404(Noticia, pk=pk)
        noticia.likes += 1
        noticia.save()

        return Response(NoticiaModelSerializer(vaga, many=False).data)
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteModelSerializer
