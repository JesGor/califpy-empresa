from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^crear_empresa$', views.crear_empresa, name='crear_empresa'),
    url(r'^crear_empresa/nueva_empresa$', views.nueva_empresa, name='nueva_empresa'),
    url(r'^eliminar_empresa$', views.eliminar_empresa, name='eliminar_empresa'),
    url(r'^eliminar_empresa_seleccionada$', views.eliminar_empresa_seleccionada, name='eliminar_empresa_seleccionada'),
    url(r'^(?P<empresa_id>[0-9]+)/calificaciones/$', views.calificaciones, name='calificaciones'),
]
