# Importa a função que desenha as páginas HTML.
from django.shortcuts import render

# Importa a função que devolve respostas simples (as telas verde e vermelha).
from django.http import HttpResponse

# Importa a biblioteca que cria códigos aleatórios (para o token do QR).
import uuid

# Importa a biblioteca que desenha a imagem do QR Code.
import qrcode

# Importa ferramentas para guardar a imagem na memória temporariamente.
from io import BytesIO
import base64

def gerar_qr(request):
    # Verifica se a pessoa clicou no botão "Gerar Código" (envio de dados via POST).
    if request.method == 'POST':
        
        # Pega o que foi digitado no campo 'matricula' do formulário HTML.
        matricula = request.POST.get('matricula')
        
        # Junta a palavra "ALUNO", a matrícula e 4 letras aleatórias para criar um código único.
        codigo_gerado = f"ALUNO-{matricula}-{uuid.uuid4().hex[:4].upper()}"
        
        # MOSTRA NO TERMINAL PRETO (É o Print 5 que o professor pediu!).
        print(f"✅ SISTEMA GEROU: {codigo_gerado}")
        
        # Manda o Python desenhar a imagem do QR Code com base no texto gerado.
        qr = qrcode.make(codigo_gerado)
        
        # Cria um espaço vazio na memória do computador para segurar a imagem.
        buffer = BytesIO()
        
        # Salva a imagem dentro desse espaço no formato PNG.
        qr.save(buffer, format="PNG")
        
        # Converte a imagem para texto (base64) para que o HTML consiga mostrar ela na tela.
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        # Envia a imagem e o texto do código para a tela (gerar_qr.html).
        return render(request, 'gerar_qr.html', {'imagem_qr': img_str, 'codigo_gerado': codigo_gerado})
        
    # Se a pessoa só abriu a página (sem clicar no botão), mostra o formulário vazio.
    return render(request, 'gerar_qr.html')

def validar_qr(request):
    # Verifica se a pessoa clicou no botão "Verificar Acesso".
    if request.method == 'POST':
        
        # Pega o que foi digitado (ou colado) no campo 'codigo_qr' do formulário HTML.
        codigo_lido = request.POST.get('codigo_qr')
        
        # MOSTRA NO TERMINAL PRETO (Simulando o celular mandando o dado).
        print(f"✅ SISTEMA RECEBEU A LEITURA: {codigo_lido}")
        
        # Verifica se o código lido começa com a palavra "ALUNO".
        if codigo_lido.startswith("ALUNO"):
            
            # Se começar, devolve uma tela com a mensagem verde de liberado.
            return HttpResponse("<h2 style='color: green;'>✅ ACESSO LIBERADO!</h2>")
            
        # Se não começar com "ALUNO", significa que é um código inválido.
        else:
            
            # Devolve uma tela com a mensagem vermelha de negado.
            return HttpResponse("<h2 style='color: red;'>❌ ACESSO NEGADO!</h2>")
            
    # Se a pessoa só abriu a página (sem clicar no botão), mostra o formulário vazio.
    return render(request, 'validar_qr.html')
