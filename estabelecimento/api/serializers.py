from rest_framework.serializers import ModelSerializer, ValidationError
from estabelecimento.models import Estabelecimento
from categoria.api.serializers import CategoriaEstabelecimentoSerializer, CategoriaEstabelecimentoPreviewSerializer


class EstabelecimentoPreviewSerializer(ModelSerializer):
    categoria = CategoriaEstabelecimentoPreviewSerializer()

    class Meta:
        model = Estabelecimento
        fields = ('id', 'titulo', 'categoria', 'imagem', 'latitude', 'longitude')
        ordering = ['titulo']


class EstabelecimentoSerializer(ModelSerializer):
    categoria = CategoriaEstabelecimentoSerializer()

    class Meta:
        model = Estabelecimento
        fields = (
            'id',
            'titulo',
            'categoria',
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


class EstabelecimentoAdmSerializer(ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ('titulo', 'ativo', 'aprovado')
        ordering = ['titulo']

    def aprovar_estabelecimento(self, id):
        try:
            estabelecimento = Estabelecimento.objects.get(pk=id)

            if estabelecimento.aprovado is True:
                raise
            else:
                serializer = EstabelecimentoAdmSerializer(estabelecimento, data={'aprovado': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            raise ValidationError({'error': 'Estabelecimento inexistente ou já está aprovado.'})

    def reprovar_estabelecimento(self, id):
        try:
            estabelecimento = Estabelecimento.objects.get(pk=id)

            if estabelecimento.aprovado is False:
                raise
            else:
                serializer = EstabelecimentoAdmSerializer(estabelecimento, data={'aprovado': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            raise ValidationError({'error': 'Estabelecimento inexistente ou já está reprovado.'})

    def ativar_estabelecimento(self, id):
        try:
            estabelecimento = Estabelecimento.objects.get(pk=id)

            if estabelecimento.ativo is True:
                raise
            else:
                serializer = EstabelecimentoAdmSerializer(estabelecimento, data={'ativo': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            raise ValidationError({'error': 'Estabelecimento inexistente ou já está ativo.'})

    def desativar_estabelecimento(self, id):
        try:
            estabelecimento = Estabelecimento.objects.get(pk=id)

            if estabelecimento.ativo is False:
                raise
            else:
                serializer = EstabelecimentoAdmSerializer(estabelecimento, data={'ativo': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            raise ValidationError({'error': 'Estabelecimento inexistente ou já está desativado.'})

