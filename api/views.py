from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota, Usuario
from .serializers import MascotaSerializer, UsuarioSerializer

# Create your views here.
class ApiMascota(APIView):
    def get(self, request):
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

class ApiUsuario(APIView):
    def get(self, request):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)