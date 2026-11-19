# Importa a função render para carregar páginas HTML e HttpResponse para respostas diretas
from django.shortcuts import render
from django.http import HttpResponse

# Bibliotecas usadas para gerar o código único e a imagem do QR Code
import uuid
import qrcode
from io import BytesIO
import base64

# Importa as tabelas (modelos) do banco de dados criadas no arquivo models.py
from .models import Aluno, RegistroAcesso


# Função responsável pela tela de geração de QR Code
def gerar_qr(request):
    # Inicia as variáveis vazias antes do usuário clicar no botão
    imagem_qr = None
    codigo_gerado = None

    # Verifica se o usuário enviou o formulário (clicou no botão "Gerar Código")
    if request.method == 'POST':
        # Captura o número de matrícula digitado no campo HTML
        matricula = request.POST.get('matricula')

        # Garante que o campo não veio vazio
        if matricula:
            # Remove espaços em branco antes ou depois da matrícula
            matricula = matricula.strip()

            # Procura o aluno no banco de dados pela matrícula; se não existir, cria automaticamente
            aluno, criado = Aluno.objects.get_or_create(
                matricula=matricula,
                defaults={
                    'nome': f'Aluno {matricula}',  # Define um nome padrão caso o aluno seja novo
                    'ativo': True                   # Marca o aluno como ativo no sistema
                }
            )

            # Verifica se o aluno ainda não tem um código QR salvo no banco
            if not aluno.qrcode_token:
                # Cria um código único misturando a matrícula com 4 caracteres aleatórios
                codigo_gerado = f"ALUNO-{matricula}-{uuid.uuid4().hex[:4].upper()}"
                # Guarda o código gerado na ficha do aluno e salva no banco de dados
                aluno.qrcode_token = codigo_gerado
                aluno.save()
            else:
                # Se o aluno já tinha um QR Code, reaproveita o mesmo código
                codigo_gerado = aluno.qrcode_token

            # Transforma o texto do código em uma imagem de QR Code
            qr = qrcode.make(codigo_gerado)

            # Salva a imagem na memória temporária do computador (sem criar arquivo físico)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            # Converte a imagem da memória para texto Base64 para o navegador conseguir exibir
            imagem_qr = base64.b64encode(buffer.getvalue()).decode()

    # Busca todos os alunos cadastrados no banco, ordenados pela matrícula, para exibir na tabela
    todos_alunos = Aluno.objects.all().order_by('matricula')

    # Renderiza a página HTML enviando a imagem, o código gerado e a lista de alunos
    return render(request, 'gerar_qr.html', {
        'imagem_qr': imagem_qr,
        'codigo_gerado': codigo_gerado,
        'todos_alunos': todos_alunos
    })


# Função responsável pela tela da guarita que valida a entrada e saída
def validar_qr(request):
    # Verifica se o vigilante enviou o código no formulário
    if request.method == 'POST':
        # Captura o código digitado ou lido pelo leitor
        codigo_lido = request.POST.get('codigo_qr')

        # Limpa espaços extras e deixa todas as letras maiúsculas para evitar erro de digitação
        if codigo_lido:
            codigo_lido = codigo_lido.strip().upper()

        try:
            # Busca no banco qual aluno é dono desse código QR
            aluno_encontrado = Aluno.objects.get(qrcode_token=codigo_lido)

            # Bloqueia a passagem caso o aluno esteja marcado como inativo no sistema
            if not aluno_encontrado.ativo:
                return HttpResponse(
                    "<div style='text-align:center; padding:50px;'>"
                    "<h2 style='color:red;'>❌ ACESSO NEGADO</h2>"
                    "<p>Aluno inativo no sistema.</p></div>"
                )

            # Busca o registro mais recente de entrada ou saída desse aluno
            ultimo_registro = RegistroAcesso.objects.filter(
                aluno=aluno_encontrado
            ).order_by('-data_hora').first()

            # Se o último registro foi ENTRADA, agora marca SAIDA; caso contrário, marca ENTRADA
            if ultimo_registro and ultimo_registro.tipo == 'ENTRADA':
                tipo = 'SAIDA'
            else:
                tipo = 'ENTRADA'

            # Cria e salva o novo registro de acesso no histórico com data e hora atuais
            RegistroAcesso.objects.create(
                aluno=aluno_encontrado,
                tipo=tipo
            )

            # Mostra na tela a confirmação verde de acesso liberado
            return HttpResponse(
                f"<div style='text-align:center; padding:50px;'>"
                f"<h2 style='color:green;'>✅ ACESSO LIBERADO</h2>"
                f"<p>Registro de {tipo} salvo!</p></div>"
            )

        # Caso nenhum aluno tenha esse código QR no banco de dados
        except Aluno.DoesNotExist:
            # Mostra na tela o aviso vermelho de acesso negado
            return HttpResponse(
                f"<div style='text-align:center; padding:50px;'>"
                f"<h2 style='color:red;'>❌ ACESSO NEGADO</h2>"
                f"<p>O código '{codigo_lido}' não existe.</p></div>"
            )

    # Se a página foi apenas aberta (sem envio de formulário), exibe o HTML normalmente
    return render(request, 'validar_qr.html')