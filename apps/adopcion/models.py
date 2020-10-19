from django.db import models

# Create your models here.
class Persona(models.Model):
	cedula=models.CharField(max_length=20)
	nombre=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=70)
	edad=models.IntegerField()
	telefono=models.CharField(max_length=10)
	email=models.EmailField()
	direccion=models.TextField()

	def __str__(self):
		return '{}{}'.format(self.nombre,self.apellidos)

class Solicitud(models.Model):
	persona=models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
	cantMascotas=models.IntegerField()
	razones=models.TextField()