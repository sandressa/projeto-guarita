from django.contrib import admin
from .models import Aluno, RegistroAcesso

# Registra as tabelas para aparecerem no painel
admin.site.register(Aluno)
admin.site.register(RegistroAcesso)
# Register your models here.
