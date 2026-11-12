from django.db import models
import alunos.models as alunos_models
# Create your models here.
class RegistroAcesso(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),
    ]
    
    aluno = models.ForeignKey(alunos_models.Aluno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data_hora = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.aluno.nome} - {self.tipo}"