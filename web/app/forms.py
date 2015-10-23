from django import forms
from app.models import Empresa, Calificacion

class crearEmpresaForm(forms.ModelForm):
	
	class Meta:
		model = Empresa
		fields = ('nombre','ciudad','sector')
		
class crearCalificacionForm(forms.ModelForm):
	class Meta:
		model = Calificacion
		fields = ('alumno','calificacion','empresa')
	
