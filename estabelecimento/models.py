from django.db import models
from categoria.models import Categoria


class Estabelecimento(models.Model):
    class Meta:
        db_table = 'tb_estabelecimento'

    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=50, unique=True)
    imagem = models.URLField(max_length=255)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cep = models.BigIntegerField()
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    telefone = models.BigIntegerField()
    email = models.EmailField()
    sobre = models.TextField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    whatsapp = models.BigIntegerField()
    facebook = models.URLField(max_length=100)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    database = 'db_encontrei'

    @property
    def endereco_completo(self):
        return "{}, N°{}, {} - {} - {} / {}".format(self.rua, self.numero, self.bairro, self.cidade, self.cep, self.uf)

    def __str__(self):
        return self.titulo
