from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Cuenta
from .serializer import CuentaSerializer
from cliente.models import Cliente

# Create your views here.

class AccountBalance(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,customer_id):
        cuenta = Cuenta.objects.filter(customer_id=customer_id).first()
        serializer = CuentaSerializer(cuenta)
        if cuenta:
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.error_messages, status=status.HTTP_404_NOT_FOUND)