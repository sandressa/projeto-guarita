from django.shortcuts import render
from .forms import RegistroAcessoForm
from .forms import HistoricoAcessoForm
from .models import RegistroAcesso

def registrar_acesso(request):
    mensagem = None

    if request.method == 'POST':  #quais outros métodos HTTP existem além de POST?
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

def historico_acesso(request):
    matricula = request.GET.get('matricula', '').strip()
    registros = RegistroAcesso.objects.all().order_by('-data_hora') # Ordena os registros do mais recente para o mais antigo
    if matricula:
        registros = registros.filter(aluno__matricula=matricula)
    return render(request, 'acesso/historico_acesso.html', {
        'registros': registros
        'matricula': matricula
        })

