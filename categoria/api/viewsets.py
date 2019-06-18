from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from categoria.models import Categoria
from categoria.api.serializers import CategoriaSerializer, CategoriaFullSerializer


class CategoriaViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.filter(aprovado=True, ativo=True).order_by('titulo')

    @action(methods=['patch'], detail=True)
    def aprovar(self, request, pk):
        categoria = CategoriaFullSerializer().aprovar_categoria(pk)
        return Response(data=categoria, status=200)

    @action(methods=['patch'], detail=True)
    def reprovar(self, request, pk):
        categoria = CategoriaFullSerializer().reprovar_categoria(pk)
        return Response(data=categoria, status=200)
