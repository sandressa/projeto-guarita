from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
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
=======
# Create your models here.
class aluno(models.Model):
# class = cia uma class em python
# aluno = nome da class
# models.model = informa ao django que essa  classe representa  uma tabela    
    matricula = models.CharField("matricula", max_length=20,unique=True)
    # matricula = nome do campo que armazena  a matricula do aluno
    # models.charfied =  criar um campo de texo
    # max_length = maximo de caracteres
    # unique = true, = impede a duplicação de informaçẽos do aluno 
    nome = models.CharField("nome completo",max_length=150)
    # nome = campo de armazenamento do nome do aluno
    # models.charfied =  criar um campo de texo
    # max_length = maximo de caracteres = 150
    qrcode_token = models.CharField("token do qr code",max_length=100,unique=True)
    # qrcode_token = armazena o codigo exclusivo do qrcode do aluno
    # models.charfied =  criar um campo de texo
    #max_length = maximo de caracteres = 100
    # unique= true, = garante que cada aluno tenha token diferente
    foto = models.ImageField("imagem do aluno", upload_to="fotos/aluno",blank=True)
    # foto = campo que armazena a imagem do aluno
    # models.imagemfield = permite trabalha com arquivos de  imagem
    #upload_to =  determina  o arquivo aonde armazena as fotos
    # blank= true, = permite cadastra o aluno sem adicionar as fotos
    ativo = models.BooleanField("ativo",default=True)
    # ativo = indica se o aluno esta ativo no sistema
    #booleanfield = campo que aceita apenas dois valores
    #default= true, = quando o aluno for cadastrado, sera automaticamente considerado ativo no sistema

    def __str__(self):
        return super().__str__()
class vigilante(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='vigilante')
    # user = realciona  o vigilante a conta de usuario 
    # models.onetoonefield = cia um relacionamento de um pra um 
    #  on_delete=models.cascade  = se a conta  do usuario for excluida, o cadastro tambem sera excluido
    #  related_name = permite o acessa o cadastro do vigilante aparti do usuario,
    matricula = models.CharField(max_length=20,unique=True)
      # 
      # models.charfied =  criar um campo de texo
      # max_length = maximo de caracteres = 100
      #   unique = true, = impede a duplicação de informaçẽos 
    nome_completo =  models.CharField (max_length=100,verbose_name="nome_completo")
    # models.charfied =  criar um campo de texo
    # max_length = maximo de caracteres = 100
    #verbose_name = define o nome no singular

def __str__(self):
    return f"{self.nome}-{self.matricula}"
class meta:
    # class meta = class interna que permite  configurar caracteristicas do modelo
    verbose_name = "aluno"
    # verbose_name = define o nome no singular
    verbose_name_plural = " alunos"
    # define o nome no plural
class registroAcesso(models.model):
    TIPO__CHOICES = [
        ('ENTRADA,entrada'),
        ('SAIDA,saida'),
>>>>>>> b34d10b9f541ada63796564c5fd0c3a88f1a6381
    ]
    
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) 
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.tipo}"