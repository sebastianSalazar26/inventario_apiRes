from rest_framework import serializers
from inventario.models import Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Productos
        fields = '__all__'