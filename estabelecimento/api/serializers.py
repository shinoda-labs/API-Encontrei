from rest_framework.serializers import ModelSerializer
from estabelecimento.models import Estabelecimento
from categoria.api.serializers import CategoriaSerializer


class EstabelecimentoSerializer(ModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Estabelecimento
        fields = (
            'id',
            'categoria',
            'titulo',
            'imagem',
            'endereco',
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

    ordering =['titulo']
