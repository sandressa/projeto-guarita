from django.db import models
from django.contrib.auth.models import User

# Classe responsável por armazenar os dados dos alunos
class Aluno(models.Model):

    # Número de matrícula do aluno, que não pode se repetir
    matricula = models.CharField("matricula", max_length=20, unique=True)

    # Nome completo do aluno
    nome = models.CharField("nome completo", max_length=150)

    # Token utilizado para gerar o QR Code do aluno
    qrcode_token = models.CharField("token do qr code", max_length=100, unique=True, blank=True, null=True)

    # Foto do aluno armazenada no sistema
    foto = models.ImageField("imagem do aluno", upload_to="fotos/aluno", blank=True, null=True)

    # Informa se o aluno está ativo no sistema
    ativo = models.BooleanField("ativo", default=True)

    # Exibe o nome e a matrícula do aluno
    def __str__(self):
        return f"{self.nome} - {self.matricula}"


# Classe responsável por registrar os acessos dos alunos
class RegistroAcesso(models.Model):

    # Define os tipos de acesso disponíveis
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),
    ]

    # Relaciona o registro de acesso ao aluno
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='registros_aluno')

    # Informa se o aluno entrou ou saiu
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    # Registra automaticamente a data e a hora do acesso
    data_hora = models.DateTimeField(auto_now_add=True)

    # Exibe o nome do aluno e o tipo de acesso
    def __str__(self):
        return f"{self.aluno.nome} - {self.tipo}"