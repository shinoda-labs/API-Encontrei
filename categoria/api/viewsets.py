from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from categoria.models import Categoria
from categoria.api.serializers import CategoriaSerializer, CategoriaAdmSerializer


class CategoriaViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    http_method_names = ['get', 'patch', 'delete', 'post']
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.filter(aprovado=True, ativo=True).order_by('titulo')

    # TODO: Colocar permissão apenas para admin acessar estas Actions

    @action(methods=['patch'], detail=True)
    def aprovar(self, request, pk):
        categoria = CategoriaAdmSerializer().aprovar_categoria(pk)
        return Response(data=categoria, status=200)

    @action(methods=['patch'], detail=True)
    def reprovar(self, request, pk):
        categoria = CategoriaAdmSerializer().reprovar_categoria(pk)
        return Response(data=categoria, status=200)

    @action(methods=['patch'], detail=True)
    def ativar(self, request, pk):
        categoria = CategoriaAdmSerializer().ativar_categoria(pk)
        return Response(data=categoria, status=200)

    @action(methods=['patch'], detail=True)
    def inativar(self, request, pk):
        categoria = CategoriaAdmSerializer().inativar_categoria(pk)
        return Response(data=categoria, status=200)
