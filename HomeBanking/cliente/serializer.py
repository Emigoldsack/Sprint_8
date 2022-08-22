from rest_framework import serializers
from cliente.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(read_only=True)
    #customer_name = serializers.CharField(max_length=255)
    #customer_surname = serializers.CharField(max_length=255)
    #customer_DNI = serializers.CharField(max_length=255)
    #customer_direccion= serializers.CharField(max_length=255)

    class Meta:
        model = Cliente
        fields = "__all__"
        read_only_fields = (
            "id",
            
        )