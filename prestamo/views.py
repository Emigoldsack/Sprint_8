from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


from cliente.models import Cliente
from .models import Prestamo
from .serializer import PrestamoSerializer
from cuenta.models import Cuenta

# Create your views here.

class Loan(APIView):
    def get(self, request,customer_id): ## TRAE EL PRESTAMO DE UN CLIENTE
        prestamo = Prestamo.objects.filter(customer_id=customer_id).first()
        serializer = PrestamoSerializer(prestamo)
        if prestamo:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, customer_id): ## BORRA EL PRESTAMO DE UN CLIENTE
        prestamo = Prestamo.objects.filter(customer_id=customer_id).first()
        if prestamo:
            serializer = PrestamoSerializer(prestamo)
            prestamo.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class CreateLoan(APIView): ## CREA UN PRESTAMO
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchLoan(APIView): ## TRAE LOS PRESTAMOS DE UN SUCURSAL
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,branch_id):
        brachloan = Prestamo.objects.filter(branch_id=branch_id).first()
        serializer = PrestamoSerializer(brachloan)
        if brachloan:
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.error_messages, status=status.HTTP_404_NOT_FOUND)
