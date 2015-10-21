from django.db import models

class Empresa(models.Model):
	nombre = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=50)
	sector = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

class Calificacion(models.Model):
	alumno = models.CharField(max_length=100)
	calificacion = models.IntegerField(default=0)
	empresa = models.ForeignKey(Empresa)
	def __str__(self):
		return self.alumno
# Create your models here.
