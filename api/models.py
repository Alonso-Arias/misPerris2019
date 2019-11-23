from django.db import models
from django.contrib.auth.models import User

# Create your models here.

estado=(
    ('Disponible', 'Disponible'),
    ('Rescatado', 'Rescatado'),
)

class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Agregamos datos
    rut=models.CharField(max_length=12)
    nombre=models.CharField(max_length=50)
    fechaNac=models.DateField()
    telContacto=models.CharField(max_length=8)
    region=models.CharField(max_length=15)
    ciudad=models.CharField(max_length=15)
    tipoVivienda=models.CharField(max_length=15)

class Mascota(models.Model):
    idMascota=models.AutoField(primary_key=True)
    imgMascota=models.ImageField(upload_to="mascotas/")
    nombreMascota=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=100)
    estado=models.CharField(max_length=15, choices=estado, default="Disponible")