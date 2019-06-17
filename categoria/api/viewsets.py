from rest_framework.viewsets import ModelViewSet
from categoria.models import Categoria
from categoria.api.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
