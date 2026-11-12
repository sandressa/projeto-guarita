from django.shortcuts import render
from .forms import RegistroAcessoForm

# Create your views here.

def registrar_acesso(request):
    form = RegistroAcessoForm()
    if request.method == 'POST':
        form = RegistroAcessoForm(request.POST)

    if form.is_valid():
        codigo = form.cleaned_data['qr_code_token']
        tipo = form.cleaned_data['tipo']
        return render(request, 'acesso/registrar_acesso.html', {'form': form, 'mensagem': 'Dados recebidos com sucesso!'})
    return render(request, 'acesso/registrar_acesso.html', {'form': form})
    