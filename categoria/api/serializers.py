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
        fields = ('id', 'titulo', 'ativo', 'aprovado')
        ordering = ['titulo']

    def aprovar_categoria(self, id):
        flag = False
        try:
            categoria = Categoria.objects.get(pk=id)

            if categoria.aprovado is True:
                flag = True
                raise
            else:
                serializer = CategoriaAdmSerializer(categoria, data={'aprovado': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'A categoria {} já está aprovada.'.format(id)})
            else:
                raise ValidationError({'error': 'Categoria inexistente'})

    def reprovar_categoria(self, id):
        flag = False
        try:
            categoria = Categoria.objects.get(pk=id)

            if categoria.aprovado is False:
                flag = True
                raise
            else:
                serializer = CategoriaAdmSerializer(categoria, data={'aprovado': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'A categoria {} já está reprovada.'.format(id)})
            else:
                raise ValidationError({'error': 'Categoria inexistente'})

    def ativar_categoria(self, id):
        flag = False
        try:
            categoria = Categoria.objects.get(pk=id)

            if categoria.ativo is True:
                flag = True
                raise
            else:
                serializer = CategoriaAdmSerializer(categoria, data={'ativo': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'A categoria {} já está ativa.'.format(id)})
            else:
                raise ValidationError({'error': 'Categoria inexistente'})

    def desativar_categoria(self, id):
        flag = False
        try:
            categoria = Categoria.objects.get(pk=id)

            if categoria.ativo is False:
                flag = True
                raise
            else:
                serializer = CategoriaAdmSerializer(categoria, data={'ativo': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'A categoria {} já está inativa.'.format(id)})
            else:
                raise ValidationError({'error': 'Categoria inexistente'})
