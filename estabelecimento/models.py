from django.db import models
from categoria.models import Categoria


class Estabelecimento(models.Model):
    class Meta:
        db_table = 'tb_estabelecimento'

    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, editable=False)
    titulo = models.CharField(max_length=50)
    imagem = models.URLField(max_length=255)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cep = models.IntegerField()
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    telefone = models.IntegerField()
    email = models.EmailField()
    sobre = models.TextField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    whatsapp = models.IntegerField()
    facebook = models.URLField(max_length=100)
    criado = models.DateTimeField(auto_created=True)
    ativo = models.BooleanField(default=False)

    database = 'db_encontrei'

    def __str__(self):
        return self.titulo
