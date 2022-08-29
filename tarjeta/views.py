from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


from cliente.models import Cliente
from .models import Tarjetas
from .serializer import TarjetaSerializer
from cuenta.models import Cuenta

# Create your views here.

class TarjetasCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,customer_id):
        account_id = Cuenta.objects.filter(customer_id=customer_id).first()
        tarjeta = Tarjetas.objects.filter(account_id=account_id)
        serializer = TarjetaSerializer(tarjeta, many=True)
        if tarjeta:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_404_NOT_FOUND)
