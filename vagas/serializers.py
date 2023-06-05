from dataclasses import fields
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField
from .models import Vaga, Empresa,Cliente

class VagaModelSerializer(ModelSerializer):
    
    class Meta:
        model = Vaga
        exclude = ["user"]


class ClienteModelSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = "__all__"

class EmpresaModelSerializer(ModelSerializer):

    class Meta:
        model = Empresa
        fields = "__all__"