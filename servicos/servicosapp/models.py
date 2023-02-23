import django
from django.db import models
from django.contrib.auth import get_user_model

# Pegando a model do usuário
auth_user = get_user_model()

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_categoria

class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    fk_usuario = models.ForeignKey(auth_user, on_delete=models.DO_NOTHING, null=True)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=150, null=False)
    descricao = models.CharField(max_length=150, default=None)
    email = models.CharField(max_length=150, null=False)
    telefone_1 = models.CharField(max_length=50, null=True)
    telefone_2 = models.CharField(max_length=50, null=True)
    preco = models.IntegerField(default=0, null=True)
    data_pub = models.DateTimeField("Data de publicação", default=django.utils.timezone.now, null=True)

    def __str__(self):
        return self.titulo