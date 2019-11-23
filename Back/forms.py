from django import forms 
from api.models import Mascota
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
import urllib.request
import json

class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

viviendas=(
    ('1','Casa Patio Grande'),
    ('2','Casa Patio Pequeño'),
)

#Api regiones
regiones = []
regiones_choices = [['0', 'Elegir una región']]
comunas = []
comunas_choices = [['0', 'Elegir una comuna']]

url_regiones = "https://apis.digital.gob.cl/dpa/regiones/"
request = urllib.request.Request(url_regiones, headers={"User-Agent":"Mozilla/5.0"})
response = urllib.request.urlopen(request)
data = json.loads(response.read())

for d in data:
    regiones.append(d)

for idx, r in enumerate(regiones):

    regiones_choices.append([regiones[idx]["codigo"], regiones[idx]["nombre"]])

for i in range(len(data)):
    comunas = []

    i += 1
    if (i < 10):
        index = str("0" + str(i))
    else:
        index = str(i)

    print("Cargando datos: " + str(((i+1)*100)/17)[0:3] + "%", end='\r')

    url_comunas = "https://apis.digital.gob.cl/dpa/regiones/" + index + "/comunas"
    request2 = urllib.request.Request(url_comunas, headers={"User-Agent":"Mozilla/5.0"})
    response2 = urllib.request.urlopen(request2)
    data2 = json.loads(response2.read())

    for d2 in data2:
        comunas.append(d2)
    
    for idx2, c in enumerate(comunas):
        comunas_choices.append([index, comunas[idx2]["nombre"]])

class Registro(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'id':'usuario', 'placeholder': 'Usuario'}), max_length=30, required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'id':'usuario', 'placeholder': 'Contraseña'}), max_length=20, required=True)
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'id':'usuario', 'placeholder': 'Confirmar Contraseña'}), max_length=20)
    correo=forms.EmailField(widget=forms.EmailInput(attrs={'id':'usuario', 'placeholder': 'E-mail'}), max_length=50, required=True)
    correo2=forms.EmailField(widget=forms.EmailInput(attrs={'id':'usuario', 'placeholder': 'Confirmar E-mail'}), max_length=50)
    rut=forms.CharField(widget=forms.TextInput(attrs={'id':'rut', 'placeholder': 'Rut'}), required=True)
    nombre=forms.CharField(widget=forms.TextInput(attrs={'id':'nombre', 'placeholder': 'Nombre'}), max_length=50)
    fechaNac=forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id':'fechaNac'}))
    telContacto=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}), max_length=8, min_length=8)
    region=forms.ChoiceField(choices=regiones_choices, widget=forms.Select(attrs={'id':'region'}))
    ciudad=forms.ChoiceField(choices=comunas_choices, widget=forms.Select(attrs={'id':'ciudad'}))
    tipoVivienda=forms.ChoiceField(choices=viviendas)

class RegistroMascota(forms.ModelForm):
    class Meta: 
        model = Mascota
        fields= ['idMascota', 'imgMascota', 'nombreMascota', 'raza', 'descripcion', 'estado']

