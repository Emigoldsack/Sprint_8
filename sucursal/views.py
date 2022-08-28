from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Sucursal
from .serializer import SucursalSerializer

# Create your views here.

class BranchList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
