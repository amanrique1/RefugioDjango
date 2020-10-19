from django.urls import path
from apps.adopcion.views import indexAdopcion

urlpatterns = [
    path('', indexAdopcion), 
]
