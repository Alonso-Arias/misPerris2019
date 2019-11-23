from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mascotas/$', views.ApiMascota.as_view()),
    url(r'^usuarios/$', views.ApiUsuario.as_view()),
]