from django.urls import path
from . import views

# Define os caminhos das páginas do sistema
urlpatterns = [

    # Página responsável por gerar o QR Code do aluno
    path('gerar/', views.gerar_qr, name='gerar_qr'),

    # Página responsável por validar o QR Code na guarita
    path('validar/', views.validar_qr, name='validar_qr'),
]