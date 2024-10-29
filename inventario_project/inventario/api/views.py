from rest_framework import viewsets
from inventario.models import Productos
from inventario.api.serializer import ProductosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer