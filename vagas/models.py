from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Cliente(models.Model):
    cpf = models.CharField("CPF",max_length=15, primary_key=True, blank=True)
    nome = models.CharField("Nome",max_length=250)
    telefone = models.CharField("Telefone",max_length=50, blank=True)
    data_nascimento = models.DateField("Data de Nascimento", blank=True, null=True)
    endereco = models.CharField("Endereço",max_length=150,blank=True, null=True )
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return "{}".format(self.nome)
    
class Empresa(models.Model):
    cnpj = models.CharField("CNPJ",max_length=15, primary_key=True, blank=True)
    nome = models.CharField("Nome",max_length=250)
    telefone = models.CharField("Telefone",max_length=50, blank=True)
    email = models.EmailField("E-mail")
    endereco = models.CharField("Endereço",max_length=150,blank=True, null=True )
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return "{}".format(self.nome)
    
class Vaga(models.Model):
    codigo = models.AutoField("Codigo",primary_key=True, unique=True)
    data_pub = models.DateField("Data de Publicação")
    descricao = models.TextField("Descrição")
    atividade = models.CharField("Atividade",max_length= 300)
    salario = models.CharField("Salário",max_length=50)
    horarios = models.CharField("Horários",max_length=50)
    total_vagas= models.CharField("Total de Vagas",max_length=50)
    curriulos= models.CharField("Curriculos",max_length=250)
    cnpj = models.ForeignKey(Empresa,on_delete=models.CASCADE, related_name='empresa_vagas')




