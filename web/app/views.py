from django.http import HttpResponse
from django.shortcuts import render
from .models import Empresa, Calificacion

def index(request):
    lista_empresas = Empresa.objects.order_by('nombre')
    context = { 'lista_empresas' : lista_empresas }
    return render(request, 'app/index.html', context)
    
def crear_empresa(request):	
	return render(request, 'app/crear_empresa.html')
	
def nueva_empresa(request):
	e = Empresa(nombre=request.POST['nombre'], ciudad=request.POST['ciudad'], sector=request.POST['sector'])
	e.save()
	return HttpResponse("Empresa creada")
	
def eliminar_empresa(request):	
	lista_empresas = Empresa.objects.order_by('nombre')
	context = { 'lista_empresas' : lista_empresas }
	return render(request, 'app/eliminar_empresa.html', context)
	
def eliminar_empresa_seleccionada(request):
	try:
	    e = Empresa.objects.get(pk=request.POST['empresa'])
	except (KeyError, Empresa.DoesNotExist):
		return render(request, 'app/eliminar_empresa.html', {
			'error_message': "No has seleccionado ninguna empresa.",
			})
	else:
		e.delete();
    	return HttpResponse("Empresa eliminada")
    	
def calificaciones(request, empresa_id):
	empresa = Empresa.objects.get(pk=empresa_id)
	lista_calificaciones = empresa.calificacion_set.all()
	context = { 'lista_calificaciones' : lista_calificaciones }
	return render(request, 'app/calificaciones.html', context)
