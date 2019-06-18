from rest_framework.serializers import ModelSerializer
from categoria.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'titulo', 'imagem')
        ordering = ['titulo']


class CategoriaEstabelecimentoSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('titulo', 'imagem')
        ordering = ['titulo']
