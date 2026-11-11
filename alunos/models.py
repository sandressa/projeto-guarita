from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model): 
    matricula = models.CharField("matricula", max_length=20, unique=True)
    nome = models.CharField("nome completo", max_length=150)
    qrcode_token = models.CharField("token do qr code", max_length=100, unique=True)
    foto = models.ImageField("imagem do aluno", upload_to="fotos/aluno", blank=True, null=True)
    ativo = models.BooleanField("ativo", default=True)

    def __str__(self):
        return f"{self.nome} - {self.matricula}"

    class Meta: 
        verbose_name = "aluno"
        verbose_name_plural = "alunos"

class Vigilante(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vigilante')
    matricula = models.CharField(max_length=20, unique=True)
    nome_completo = models.CharField(max_length=100, verbose_name="nome_completo")

    def __str__(self):
        return f"{self.nome_completo} - {self.matricula}"

class RegistroAcesso(models.Model): 
    TIPO_CHOICES = [ 
        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),
    ]
    
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) 
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.tipo}"