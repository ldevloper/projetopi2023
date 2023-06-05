from django.forms import ModelForm
from .models import Vaga, Cliente, Empresa

class VagaForm(ModelForm):
    
    class Meta:
        model = Vaga
        fields = '__all__'

class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

class EmpresaForm(ModelForm):
    
    class Meta:
        model = Empresa
        fields = '__all__'