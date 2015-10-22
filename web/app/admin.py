"""
Modulo que indica las opciones del panel de admin.
"""

from django.contrib import admin

from .models import Empresa, Calificacion

admin.site.register(Empresa)
admin.site.register(Calificacion)
