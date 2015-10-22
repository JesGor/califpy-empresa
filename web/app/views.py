"""
Modulo con todas las views de la aplicacion que contienen las funcionalidades de la misma.
"""

from django.http import HttpResponse
from django.shortcuts import render
from .models import Empresa, Calificacion

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
	Permite acceder al formulario donde se crea la empresa
	
	:param request: peticion http
	:return: devuelve un render con request al formulario de creacion de empresa
	"""
	return render(request, 'app/crear_empresa.html')
	
def nueva_empresa(request):
	"""
	Crea una empresa con los datos recogidos de un formulario y si sucede algun error vuelve a mostrar el formulario con un error.
	
	:param request: peticion http
	:return: devuelve una respuesta http
	"""
	if request.method == "POST":
		e = Empresa(nombre=request.POST['nombre'], ciudad=request.POST['ciudad'], sector=request.POST['sector'])
		e.save()
		return HttpResponse("Empresa creada")
	else:
		return render(request, 'app/crear_empresa.html', {
			'error_message': "Error al crear empresa.",
			})
	
def eliminar_empresa(request):
	"""
	Muestra el template con el formulario para eliminar empresas
	
	:param request: peticion http
	:return: devuelve un render con un request al formulario para eliminar empresas
	"""
	lista_empresas = Empresa.objects.order_by('nombre')
	context = { 'lista_empresas' : lista_empresas }
	return render(request, 'app/eliminar_empresa.html', context)
	
def eliminar_empresa_seleccionada(request):
	"""
	Elimina una empresa con los datos obtenidos a traves de un formulario. Devuelve una respuesta en caso afirmativo o sino vuelve al formulario para la eliminacion de empresas.
	
	:param request: peticion http
	:return: devuelve una respuesta http
	"""
	if request.method == "POST":
		try:
			e = Empresa.objects.get(pk=request.POST['empresa'])
		except (KeyError, Empresa.DoesNotExist):
			return render(request, 'app/eliminar_empresa.html', {
				'error_message': "No has seleccionado ninguna empresa.",
				})
		else:
			e.delete();
			return HttpResponse("Empresa eliminada")
	else:
		return render(request, 'app/eliminar_empresa.html', {
			'error_message': "Error al eliminar empresa.",
			})
    	
def crear_calificacion(request):
	"""
	Permite acceder al formulario para crear una calificacion para una empresa
	
	:param request: peticion http
	:return: devuelve un render con request al template de creacion de calificaciones
	"""
	lista_empresas = Empresa.objects.order_by('nombre')
	context = { 'lista_empresas' : lista_empresas }
	return render(request, 'app/crear_calificacion.html', context)
	
def nueva_calificacion(request):
	"""
	Crea una nueva calificacion con los datos obtenivos a traves de un formulario.
	
	:param request: peticion http
	:return: devuelve una respuesta http
	"""
	if request.method == "POST":
		emp = Empresa.objects.get(pk=request.POST['empresa'])
		c = Calificacion(alumno=request.POST['alumno'], calificacion=request.POST['calif'], empresa=emp)
		c.save()
		return HttpResponse("Calificacion creada")
	else:
		return render(request, 'app/crear_calificacion.html', {
			'error_message': "Error al crear calificacion.",
			})
	
def eliminar_calificacion(request, empresa_id):	
	"""
	Permite acceder al formulario para eliminar calificaciones de una determinada empresa
	
	:param request: peticion http
	:param empresa_id: id de la empresa que tiene la calificacion
	:return: devuelve un render con un request al template de eliminacion de calificaciones.
	"""
	empresa = Empresa.objects.get(pk=empresa_id)
	lista_calificaciones = empresa.calificacion_set.all()
	context = { 'lista_calificaciones' : lista_calificaciones, 'empresa' : empresa }
	return render(request, 'app/eliminar_calificacion.html', context)
    	
def eliminar_calificacion_seleccionada(request, empresa_id):
	"""
	Borra una calificacion seleccionada desde un formulario asociada a una empresa
	
	:param request: peticion http
	:param empresa_id: id de la empresa que tiene la calificacion
	:return: devuelve una respuesta http
	"""
	if request.method == "POST":
		try:
			c = Calificacion.objects.get(pk=request.POST['calif'])
		except (KeyError, Empresa.DoesNotExist):
			return render(request, 'app/eliminar_calificacion.html', {
				'error_message': "No has seleccionado ninguna calificacion.",
				})
		else:
			c.delete();
			return HttpResponse("Calificacion eliminada")
	else:
		return render(request, 'app/eliminar_calificacion.html', {
			'error_message': "Error al eliminar calificacion.",
			})

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
	

