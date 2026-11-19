from django.shortcuts import render
from django.http import HttpResponse
import uuid
import qrcode
from io import BytesIO
import base64

# Importa as tabelas criadas no arquivo models.py
from .models import Aluno, RegistroAcesso

def gerar_qr(request):

    # Verifica se o formulário foi enviado
    if request.method == 'POST':

        # Pega a matrícula digitada pelo usuário
        matricula = request.POST.get('matricula')

        try:
            # Procura o aluno no banco de dados pela matrícula
            aluno = Aluno.objects.get(matricula=matricula)

            # Verifica se o aluno já possui um QR Code
            if not aluno.qrcode_token:

                # Gera um código único para o aluno
                codigo_gerado = f"ALUNO-{matricula}-{uuid.uuid4().hex[:4].upper()}"

                # Salva o código na ficha do aluno
                aluno.qrcode_token = codigo_gerado
                aluno.save()

            else:
                # Reutiliza o código que o aluno já possui
                codigo_gerado = aluno.qrcode_token

            # Gera a imagem do QR Code
            qr = qrcode.make(codigo_gerado)

            # Armazena a imagem temporariamente
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            # Converte a imagem para texto
            img_str = base64.b64encode(buffer.getvalue()).decode()

            # Envia o QR Code e o código para a página
            return render(request, 'gerar_qr.html', {
                'imagem_qr': img_str,
                'codigo_gerado': codigo_gerado
            })

        except Aluno.DoesNotExist:

            # Exibe uma mensagem se a matrícula não for encontrada
            return render(request, 'gerar_qr.html', {
                'erro': 'Matrícula não cadastrada no banco!'
            })

    # Exibe a página normalmente ao ser aberta
    return render(request, 'gerar_qr.html')

def validar_qr(request):

    # Verifica se o formulário foi enviado
    if request.method == 'POST':

        # Pega o código QR informado
        codigo_lido = request.POST.get('codigo_qr')

        # Remove espaços e transforma as letras em maiúsculas
        if codigo_lido:
            codigo_lido = codigo_lido.strip().upper()

        try:
            # Procura o aluno pelo código do QR Code
            aluno_encontrado = Aluno.objects.get(qrcode_token=codigo_lido)

            # Verifica se o aluno está ativo no sistema
            if not aluno_encontrado.ativo:
                return HttpResponse(
                    "<div style='text-align:center; padding:50px;'>"
                    "<h2 style='color:red;'>❌ ACESSO NEGADO</h2>"
                    "<p>Aluno inativo no sistema.</p></div>"
                )

            # Busca o último registro de acesso do aluno
            ultimo_registro = RegistroAcesso.objects.filter(
                aluno=aluno_encontrado
            ).order_by('-data_hora').first()

            # Verifica se o próximo acesso será entrada ou saída
            if ultimo_registro and ultimo_registro.tipo == 'ENTRADA':
                tipo = 'SAIDA'
            else:
                tipo = 'ENTRADA'

            # Salva o acesso no histórico
            RegistroAcesso.objects.create(
                aluno=aluno_encontrado,
                tipo=tipo
            )

            # Exibe a mensagem de acesso liberado
            return HttpResponse(
                f"<div style='text-align:center; padding:50px;'>"
                f"<h2 style='color:green;'>✅ ACESSO LIBERADO</h2>"
                f"<p>Registro de {tipo} salvo!</p></div>"
            )

        except Aluno.DoesNotExist:

            # Exibe uma mensagem se o código não for encontrado
            return HttpResponse(
                f"<div style='text-align:center; padding:50px;'>"
                f"<h2 style='color:red;'>❌ ACESSO NEGADO</h2>"
                f"<p>O código '{codigo_lido}' não existe.</p></div>"
            )

    # Abre a página de validação normalmente
    return render(request, 'validar_qr.html')