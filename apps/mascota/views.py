from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota


# Create your views here.

def indexMascota(request):
	return render(request,"mascota/index.php")

def mascotaForm(request):
	if request.method =='POST':
		form=MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:indexMascota')

	else:
		form=MascotaForm()

	return render(request,'mascota/mascotaForm.html',{'form':form})

def listarMascota(request):
	
	mascota=Mascota.objects.all().order_by('id')
	contexto={'mascotas':mascota}
	return render(request, 'mascota/listarMascota.html',contexto)

def editarMascota(request,idMascota):

	mascota=Mascota.objects.get(id=idMascota)
	if request.method=='GET':
		form=MascotaForm(instance=mascota)
	else:
		form=MascotaForm(request.POST,instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('../listar')
	return render(request,'mascota/mascotaForm.html',{'formu':form})

def eliminarMascota(request,idMascota):
	mascota=Mascota.objects.get(id=idMascota)
	if request.method=='POST':
		mascota.delete()
		return redirect('../listar')
	return render(request,'mascota/eliminarMascota.html',{'mascota':mascota})

class ListarMascota(ListView):
	model= Mascota
	template_name='mascota/listarMascota2.html'

class CrearMascota(CreateView):
	model= Mascota
	form_class=MascotaForm
	template_name='mascota/mascotaForm.html'
	success_url=reverse_lazy('listarMascota')

class EditarMascota(UpdateView):
	model= Mascota
	form_class=MascotaForm
	template_name='mascota/mascotaForm.html'
	success_url=reverse_lazy('listarMascota')

class EliminarMascota(DeleteView):
	model=Mascota
	template_name='mascota/eliminarMascota2.html'
	success_url=reverse_lazy('listarMascota')