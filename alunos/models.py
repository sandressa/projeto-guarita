from django.db import models

# Create your models here.
class aluno(models.Model):
    matricula = models.CharField("matricula", max_length=20,unique=True)
    nome = models.CharField("nome completo",max_length=150)
    qrcode_token = models.CharField("token do qr code",max_length=100,unique=True)
    foto = models.ImageField("imagem do aluno", upload_to="fotos/aluno",blank=True)
    ativo = models.BooleanField("ativo",default=True)

    def __str__(self):
        return super().__str__()