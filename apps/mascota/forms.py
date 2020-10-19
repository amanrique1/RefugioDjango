from django import forms  
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
	class Meta:
		model=Mascota

		fields= [
				'nombre',
				'sexo',
				'edad',
				'fechaRescate',
				'persona',
				'vacuna',
				]


		labels= {
				'nombre':'Nombre',
				'sexo':'Sexo',
				'edad':'Edad Aproximada',
				'fechaRescate': 'Fecha Rescate',
				'persona': 'Persona',
				'vacuna': 'Vacuna',
				}

		fields= {
				'nombre':forms.TextInput(attrs={'class':'form-control'}),
				'sexo':forms.TextInput(attrs={'class':'form-control'}),
				'edad':forms.TextInput(attrs={'class':'form-control'}),
				'fechaRescate':forms.TextInput(attrs={'class':'form-control'}),
				'persona':forms.Select(attrs={'class':'form-control'}),
				'vacuna':forms.CheckboxSelectMultiple(),
				}
