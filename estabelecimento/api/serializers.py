from rest_framework.serializers import ModelSerializer
from estabelecimento.models import Estabelecimento
from categoria.api.serializers import CategoriaEstabelecimentoSerializer


class EstabelecimentoSerializer(ModelSerializer):
    categoria = CategoriaEstabelecimentoSerializer()

    class Meta:
        model = Estabelecimento
        fields = (
            'id',
            'categoria',
            'titulo',
            'imagem',
            'endereco_completo',
            'rua',
            'numero',
            'bairro',
            'cep',
            'uf',
            'telefone',
            'email',
            'sobre',
            'longitude',
            'latitude',
            'whatsapp',
            'facebook'
        )

    ordering = ['titulo']
