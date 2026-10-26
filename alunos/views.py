from django.shortcuts import render

# Create your views here.

def index(request):
    """pagina principal do guarita ifpi"""
    return render(request, 'alunos/index.html')

