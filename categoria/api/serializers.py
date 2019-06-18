from rest_framework.serializers import ModelSerializer, ValidationError
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


class CategoriaEstabelecimentoPreviewSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('titulo',)
        ordering = ['titulo']


class CategoriaAdmSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('titulo', 'ativo', 'aprovado')
        ordering = ['titulo']

    def aprovar_categoria(self, id):
        try:
            categoria = Categoria.objects.get(pk=id)

            serializer = CategoriaAdmSerializer(categoria, data={'aprovado': True}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return serializer.data
        except Exception as e:
            raise ValidationError({'error': 'A Categoria com o código {} não existe.'.format(id)})

    def reprovar_categoria(self, id):
        try:
            categoria = Categoria.objects.get(pk=id)

            serializer = CategoriaAdmSerializer(categoria, data={'aprovado': False}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return serializer.data
        except Exception as e:
            raise ValidationError({'error': 'A Categoria com o código {} não existe.'.format(id)})

    def ativar_categoria(self, id):
        try:
            categoria = Categoria.objects.get(pk=id)

            serializer = CategoriaAdmSerializer(categoria, data={'ativo': True}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return serializer.data
        except Exception as e:
            raise ValidationError({'error': 'A Categoria com o código {} não existe.'.format(id)})

    def desativar_categoria(self, id):
        try:
            categoria = Categoria.objects.get(pk=id)

            serializer = CategoriaAdmSerializer(categoria, data={'ativo': False}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return serializer.data
        except Exception as e:
            raise ValidationError({'error': 'A Categoria com o código {} não existe.'.format(id)})
