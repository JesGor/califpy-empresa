"""
Modulo con todas las views de la aplicacion que contienen las funcionalidades de la misma.
"""

from django.http import HttpResponse
from django.shortcuts import render
from .models import Empresa, Calificacion
from .forms import *

def index(request):
	"""
	Lanza el template con el index de la aplicacion, que muestra un listado de empresas.
	
	:param request: peticion http
	:return: devuelve un render con request al index
	"""
	lista_empresas = Empresa.objects.order_by('nombre')
	context = { 'lista_empresas' : lista_empresas }
	return render(request, 'app/index.html', context)
    
def crear_empresa(request):	
	"""
	Muestra el formulario para crear una empresa si no ha sido invocado desde un formulario con metodo POST, crea la empresa y la almacena en caso contrario.
	
	:param request: peticion http
	:return: devuelve un render con request al template de creacion de empresa
	"""
	message= None
	if request.method == "POST":
		form = crearEmpresaForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			message = "Empresa creada correctamente."
	else:
		form = crearEmpresaForm()
		
	context = { 'form' : form, 'message' : message}
	return render(request, 'app/crear_empresa.html', context)
	
def eliminar_empresa(request):
	"""
	Muestra el template con el formulario para eliminar empresas si no ha sido lanzada desde un formulario, de ser asi borra una empresa seleccionada mediante el formulario que la lanza.
	
	:param request: peticion http
	:return: devuelve un render con un request al template de eliminar empresa
	"""
	message=None
	lista_empresas=None
	if request.method == "POST":
		try:
			e = Empresa.objects.get(pk=request.POST['empresa'])
		except (KeyError, Empresa.DoesNotExist):
			message= "No has seleccionado ninguna empresa"
		else:
			e.delete();
			message="Empresa eliminada"
	else:
		lista_empresas = Empresa.objects.order_by('nombre')
		
	context = { 'lista_empresas' : lista_empresas, 'message' : message}
	return render(request, 'app/eliminar_empresa.html', context)
	
    	
def crear_calificacion(request):
	"""
	Permite acceder al formulario para crear una calificacion para una empresa si no es lanzado desde un formulario con metodo POST, en caso contrario crea una calificacion asignandola a una empresa
	
	:param request: peticion http
	:return: devuelve un render con request al template de creacion de calificaciones
	"""
	message = None
	if request.method == "POST":
		form = crearCalificacionForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			message = "Calificacion creada"
	else:
		form = crearCalificacionForm()
	
	context = { 'form' : form, 'message' : message}
	return render(request, 'app/crear_calificacion.html', context)
	
	
def eliminar_calificacion(request, empresa_id):	
	"""
	Permite acceder al formulario para eliminar calificaciones de una determinada empresa, en caso de ser lanzada por un formulario con metodo POST se borra una calificacion de una empresa asociada.
	
	:param request: peticion http
	:param empresa_id: id de la empresa que tiene la calificacion
	:return: devuelve un render con un request al template de eliminacion de calificaciones.
	"""
	message=None
	lista_calificaciones = None
	empresa = Empresa.objects.get(pk=empresa_id)
	if request.method == "POST":
		try:
			c = Calificacion.objects.get(pk=request.POST['calif'])
		except (KeyError, Empresa.DoesNotExist):
			message= "No has selecionado ninguna calificacion"
		else:
			c.delete();
			message = "Calificacion eliminada"
	else:
		lista_calificaciones = empresa.calificacion_set.all()
		
	context = { 'lista_calificaciones' : lista_calificaciones,  'message' : message, 'empresa' : empresa }
	return render(request, 'app/eliminar_calificacion.html', context)
    	

def calificaciones(request, empresa_id):
	"""
	Muestra las calificaciones que tiene una determinada empresa
	
	:param request: peticion http
	:param empresa_id: id de la empresa de la que mostrar las calificaciones
	:return: devuelve un render con un request al template con las calificaciones de la empresa
	"""
	empresa = Empresa.objects.get(pk=empresa_id)
	lista_calificaciones = empresa.calificacion_set.all()
	context = { 'lista_calificaciones' : lista_calificaciones, 'empresa' : empresa }
	return render(request, 'app/calificaciones.html', context)
	

