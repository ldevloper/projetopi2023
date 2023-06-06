from django.contrib import admin
from .models import Cliente, Vaga, Empresa

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    model=Empresa

class VagaAdmin(admin.ModelAdmin):
    model=Vaga 


admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(Vaga)




# Register your models here.
