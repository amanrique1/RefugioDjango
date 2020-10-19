from django.urls import path
from django.conf.urls import url
from apps.mascota.views import *

urlpatterns = [
    url(r'^$', indexMascota,name='indexMascota'), 
    path('agregar', mascotaForm),
    path('listar', listarMascota), 
   	url(r'^editar/(?P<idMascota>\d+)$', editarMascota,name='editarMascota'), 
   	url(r'^eliminar/(?P<idMascota>\d+)$', eliminarMascota,name='eliminarMascota'), 
   	url(r'^listar2$', ListarMascota.as_view(),name='listarMascota'), 
   	path('agregar2', CrearMascota.as_view()),
   	url(r'^editar2/(?P<pk>\d+)$', EditarMascota.as_view(),name='editarMascota2'), 
   	url(r'^eliminar2/(?P<pk>\d+)$', EliminarMascota.as_view(),name='eliminarMascota2'), 
]
