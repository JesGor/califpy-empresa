"""
Modulo destinado a definir los modelos de datos presentes en esta aplicacion, como son las empresas y las calificaciones
"""
from django.db import models

class Empresa(models.Model):
	"""
	Clase que define la estructura de una empresa en la base de datos. Con 'nombre', 'ciudad' y 'sector'.
	"""
	nombre = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=50)
	sector = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

class Calificacion(models.Model):
	"""
	Clase que define la calificacion de una empresa. Con 'alumno', 'calificacion y 'empresa'.
	"""
	alumno = models.CharField(max_length=100)
	calificacion = models.IntegerField(default=0)
	empresa = models.ForeignKey(Empresa)
	def __str__(self):
		return self.alumno
