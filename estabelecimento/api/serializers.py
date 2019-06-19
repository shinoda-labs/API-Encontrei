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
            'facebook',
            'categoria',
        )

    ordering = ['titulo']


class EstabelecimentoAdmSerializer(ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ('titulo', 'ativo', 'aprovado')
        ordering = ['titulo']

    def aprovar_estabelecimento(self, id):
        flag  = False
        try:
            estabelecimento = Estabelecimento.objects.get(pk=id)

            if estabelecimento.aprovado is True:
                flag = True
                raise
            else:
                serializer = EstabelecimentoAdmSerializer(estabelecimento, data={'aprovado': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'O estabelecimento {} já está aprovado.'.format(id)})
            else:
                raise ValidationError({'error': 'Estabelecimento inexistente'})

    def reprovar_estabelecimento(self, id):
        flag = False
        try:
            estabelecimento = Estabelecimento.objects.get(pk=id)

            if estabelecimento.aprovado is False:
                flag = True
                raise
            else:
                serializer = EstabelecimentoAdmSerializer(estabelecimento, data={'aprovado': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'O estabelecimento {} já está reprovado.'.format(id)})
            else:
                raise ValidationError({'error': 'Estabelecimento inexistente'})

    def ativar_estabelecimento(self, id):
        flag = False
        try:
            estabelecimento = Estabelecimento.objects.get(pk=id)

            if estabelecimento.ativo is True:
                flag = True
                raise
            else:
                serializer = EstabelecimentoAdmSerializer(estabelecimento, data={'ativo': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'O estabelecimento {} já está ativo.'.format(id)})
            else:
                raise ValidationError({'error': 'Estabelecimento inexistente'})

    def desativar_estabelecimento(self, id):
        flag = False
        try:
            estabelecimento = Estabelecimento.objects.get(pk=id)

            if estabelecimento.ativo is False:
                flag = True
                raise
            else:
                serializer = EstabelecimentoAdmSerializer(estabelecimento, data={'ativo': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'O estabelecimento {} já está inativo.'.format(id)})
            else:
                raise ValidationError({'error': 'Estabelecimento inexistente'})

