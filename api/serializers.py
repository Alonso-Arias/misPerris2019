from rest_framework import serializers
from .models import Mascota, Usuario

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = Mascota

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = Usuario