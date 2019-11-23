from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from api.models import Usuario, Mascota
from .forms import Login, Registro, RegistroMascota
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from os import environ
from social_django.models import UserSocialAuth

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

def index(request):
        return render(request, "index.html") 

def salir(request):
    logout(request)
    return redirect('index')

def registro(redirect):
    return redirect("registroExitoso.html")

def registrate(request):
    if request.user.is_authenticated:
        return redirect('index')
    actual=request.user
    form=Registro(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        regDB=User.objects.create_user(data.get("username"),data.get("correo"), data.get("password"))
        usuario=Usuario(user=regDB,rut=data.get("rut"),nombre=data.get("nombre"),fechaNac=data.get("fechaNac"),telContacto=data.get("telContacto"),region=data.get("region"),ciudad=data.get("ciudad"),tipoVivienda=data.get("tipoVivienda"))
        regDB.save()
        usuario.save()
    form=Registro()
    if request.POST:
        return render(request, "registroExitoso.html", {'actual':actual, 'form':form})
    return render(request, "registrate.html", {'actual':actual, 'form':form})

def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,"login.html",{'form':form,})

@login_required(login_url='login')
def mascotas(request):
    actual=request.user
    mascotas = Mascota.objects.all().order_by("idMascota")
    form=RegistroMascota(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        mascota=Mascota(imgMascota=request.FILES["imgMascota"],nombreMascota=data.get("nombreMascota"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"))
        mascota.save()
    form=RegistroMascota
    mascotas = Mascota.objects.all()
    paginator = Paginator(mascotas, 8)
    page = request.GET.get('page')
    mascotas = paginator.get_page(page)
    return render(request, "mascotas.html", {'form':form, 'mascotas':mascotas, 'actual':actual})

@login_required(login_url='login')
def eliminarMascotas(request, idMascota):
    mascotas=Mascota.objects.get(idMascota=idMascota)
    if request.method == 'POST':
        mascotas.delete()
        return redirect('mascotas')
    return render(request, 'eliminarMascotas.html', {'mascotas':mascotas})
    
@login_required(login_url='login')
def editarMascotas(request, idMascota):
    instance=get_object_or_404(Mascota, idMascota=idMascota)
    mascotas=Mascota.objects.get(idMascota=idMascota)
    form = RegistroMascota(request.POST or None,request.FILES or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mascotas')
    return render(request, 'editarMascotas.html', {'form':form, 'mascotas':mascotas})