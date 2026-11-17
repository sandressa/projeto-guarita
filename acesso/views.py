from django.shortcuts import render
from .forms import RegistroAcessoForm

def registrar_acesso(request):
    mensagem = None

    if request.method == 'POST':
        form = RegistroAcessoForm(request.POST)

        if form.is_valid():
            codigo = form.cleaned_data['qr_code_token']
            tipo = form.cleaned_data['tipo']

            mensagem = 'Dados recebidos com sucesso!'

            form = RegistroAcessoForm()

    else:
        form = RegistroAcessoForm()

    return render(request, 'acesso/registrar_acesso.html', {
        'form': form,
        'mensagem': mensagem
    })