# Importa a ferramenta do Django que cria os caminhos (URLs) do site.
from django.urls import path

# Importa o arquivo views.py que está na mesma pasta para acessar as funções.
from . import views

# Cria a lista de rotas do sistema.
urlpatterns = [
    # Quando alguém acessar o link terminado em /gerar/, o Django vai chamar a função gerar_qr.
    # O name='gerar_qr' é só um apelido para essa rota.
    path('gerar/', views.gerar_qr, name='gerar_qr'),
    
    # Quando alguém acessar o link terminado em /validar/, o Django vai chamar a função validar_qr.
    path('validar/', views.validar_qr, name='validar_qr'),
]
