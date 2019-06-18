from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from estabelecimento.models import Estabelecimento
from .serializers import EstabelecimentoSerializer


class EstabelecimentoViewSet(ModelViewSet):
    queryset = Estabelecimento.objects.all().order_by('titulo')
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EstabelecimentoSerializer
    filter_fields = ('categoria',)
