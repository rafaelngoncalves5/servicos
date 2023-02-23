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
    fk_usuario = models.ForeignKey(auth_user, on_delete=models.DO_NOTHING)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    telefone_1 = models.CharField(max_length=50)
    telefone_2 = models.CharField(max_length=50)
    preco = models.FloatField

    def __str__(self):
        return self.titulo
