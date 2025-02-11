from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),  # ✅ Agregada la ruta para evitar el error

    path('equipos/', lista_equipos, name='lista_equipos'),
    path('equipos/nuevo/', crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:id>/', editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:id>/', eliminar_equipo, name='eliminar_equipo'),

    path('obras/', lista_obras, name='lista_obras'),
    path('obras/nuevo/', crear_obra, name='crear_obra'),
    path('obras/editar/<int:id>/', editar_obra, name='editar_obra'),
    path('obras/eliminar/<int:id>/', eliminar_obra, name='eliminar_obra'),

    path('ubicaciones/', lista_ubicaciones, name='lista_ubicaciones'),
    path('ubicaciones/nuevo/', crear_ubicacion, name='crear_ubicacion'),
    path('ubicaciones/editar/<int:id>/', editar_ubicacion, name='editar_ubicacion'),
    path('ubicaciones/eliminar/<int:id>/', eliminar_ubicacion, name='eliminar_ubicacion'),

    path('responsables/', lista_responsables, name='lista_responsables'),
    path('responsables/nuevo/', crear_responsable, name='crear_responsable'),
    path('responsables/editar/<int:id>/', editar_responsable, name='editar_responsable'),
    path('responsables/eliminar/<int:id>/', eliminar_responsable, name='eliminar_responsable'),

    path('equipos/reporte/', generar_pdf_equipos, name='generar_pdf_equipos'),
    path('obras/reporte/', generar_pdf_obras, name='generar_pdf_obras'),
    path('ubicaciones/reporte/', generar_pdf_ubicaciones, name='generar_pdf_ubicaciones'),
    path('responsables/reporte/', generar_pdf_responsables, name='generar_pdf_responsables'),

    path('exportar-excel/', exportar_excel, name='exportar_excel'),

]
