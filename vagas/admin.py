from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import forms
from .models import Cliente, Vaga, Empresa

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(Vaga)




# Register your models here.
