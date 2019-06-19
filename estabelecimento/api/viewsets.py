from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from estabelecimento.models import Estabelecimento
from .serializers import EstabelecimentoSerializer, EstabelecimentoPreviewSerializer, EstabelecimentoAdmSerializer


class EstabelecimentoViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = EstabelecimentoSerializer

    def get_queryset(self):
        return Estabelecimento.objects.filter(aprovado=True, ativo=True).order_by('titulo')

    # TODO: Colocar permissão apenas para admin acessar estas Actions

    @action(methods=['patch'], detail=True)
    def aprovar(self, request, pk):
        estabelecimento = EstabelecimentoAdmSerializer().aprovar_estabelecimento(pk)
        return Response(data=estabelecimento, status=200)

    @action(methods=['patch'], detail=True)
    def reprovar(self, request, pk):
        estabelecimento = EstabelecimentoAdmSerializer().reprovar_estabelecimento(pk)
        return Response(data=estabelecimento, status=200)

    @action(methods=['patch'], detail=True)
    def ativar(self, request, pk):
        estabelecimento = EstabelecimentoAdmSerializer().ativar_estabelecimento(pk)
        return Response(data=estabelecimento, status=200)

    @action(methods=['patch'], detail=True)
    def desativar(self, request, pk):
        estabelecimento = EstabelecimentoAdmSerializer().desativar_estabelecimento(pk)
        return Response(data=estabelecimento, status=200)


class EstabelecimentoPreviewViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = EstabelecimentoPreviewSerializer
    filter_fields = ('categoria',)

    def get_queryset(self):
        return Estabelecimento.objects.filter(aprovado=True, ativo=True).order_by('titulo')
