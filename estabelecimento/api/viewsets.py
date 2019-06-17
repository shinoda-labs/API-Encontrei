from rest_framework.viewsets import ModelViewSet
from estabelecimento.models import Estabelecimento
from .serializers import EstabelecimentoSerializer


class EstabelcimentoViewSet(ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
