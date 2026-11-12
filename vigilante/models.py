from django.db import models

# Create your models here.
class vigilante(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20,unique=True)
    nome_completo = models.CharField(max_length=100,verbose_name="nome_completo")

