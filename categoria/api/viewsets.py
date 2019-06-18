from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from categoria.models import Categoria
from categoria.api.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all().order_by('titulo')
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategoriaSerializer
