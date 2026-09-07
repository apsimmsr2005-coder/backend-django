from rest_framework import serializers
from .models import Producto

# modelo = Producto Indica que el serializer se basa en el modelo Producto
# fields = '__all__' Indica que se incluirán todos los campos del modelo en el serializer
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'El precio debe ser mayor a cero'
            )
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'El stock debe ser mayor a cero'
            )
        return value