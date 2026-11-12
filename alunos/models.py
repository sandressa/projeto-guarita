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
