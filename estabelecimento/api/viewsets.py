from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from estabelecimento.models import Estabelecimento
from .serializers import EstabelecimentoSerializer


class EstabelecimentoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EstabelecimentoSerializer
    filter_fields = ('categoria',)

    def get_queryset(self):
        return Estabelecimento.objects.filter(aprovado=True, ativo=True).order_by('titulo')
