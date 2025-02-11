from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipo, Obra, Ubicacion, Responsable
from .forms import EquipoForm, ObraForm, UbicacionForm, ResponsableForm
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Equipo
import pandas as pd
from django.db.models import Count
import matplotlib.pyplot as plt
import io
import base64

def home(request):
    return render(request, 'base.html')

# ---- EQUIPO ----
def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'maquinaria/equipo_lista.html', {'equipos': equipos})

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'maquinaria/form.html', {'form': form})

def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'maquinaria/form.html', {'form': form})

def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('lista_equipos')
    return render(request, 'maquinaria/confirmar_eliminar.html', {'objeto': equipo})

# ---- CRUD para OBRAS ----
def lista_obras(request):
    obras = Obra.objects.all()
    return render(request, 'maquinaria/obra_lista.html', {'obras': obras})

def crear_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_obras')
    else:
        form = ObraForm()
    return render(request, 'maquinaria/form.html', {'form': form})

def editar_obra(request, id):
    obra = get_object_or_404(Obra, id=id)
    if request.method == 'POST':
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('lista_obras')
    else:
        form = ObraForm(instance=obra)
    return render(request, 'maquinaria/form.html', {'form': form})

def eliminar_obra(request, id):
    obra = get_object_or_404(Obra, id=id)
    if request.method == 'POST':
        obra.delete()
        return redirect('lista_obras')
    return render(request, 'maquinaria/confirmar_eliminar.html', {'objeto': obra})

# ---- CRUD para UBICACIONES ----
def lista_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'maquinaria/ubicacion_lista.html', {'ubicaciones': ubicaciones})

def crear_ubicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ubicaciones')
    else:
        form = UbicacionForm()
    return render(request, 'maquinaria/form.html', {'form': form})

def editar_ubicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    if request.method == 'POST':
        form = UbicacionForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            return redirect('lista_ubicaciones')
    else:
        form = UbicacionForm(instance=ubicacion)
    return render(request, 'maquinaria/form.html', {'form': form})

def eliminar_ubicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    if request.method == 'POST':
        ubicacion.delete()
        return redirect('lista_ubicaciones')
    return render(request, 'maquinaria/confirmar_eliminar.html', {'objeto': ubicacion})

# ---- CRUD para RESPONSABLES ----
def lista_responsables(request):
    responsables = Responsable.objects.all()
    return render(request, 'maquinaria/responsable_lista.html', {'responsables': responsables})

def crear_responsable(request):
    if request.method == 'POST':
        form = ResponsableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_responsables')
    else:
        form = ResponsableForm()
    return render(request, 'maquinaria/form.html', {'form': form})

def editar_responsable(request, id):
    responsable = get_object_or_404(Responsable, id=id)
    if request.method == 'POST':
        form = ResponsableForm(request.POST, instance=responsable)
        if form.is_valid():
            form.save()
            return redirect('lista_responsables')
    else:
        form = ResponsableForm(instance=responsable)
    return render(request, 'maquinaria/form.html', {'form': form})

def eliminar_responsable(request, id):
    responsable = get_object_or_404(Responsable, id=id)
    if request.method == 'POST':
        responsable.delete()
        return redirect('lista_responsables')
    return render(request, 'maquinaria/confirmar_eliminar.html', {'objeto': responsable})


# Función genérica para generar PDF
def generar_pdf(response, titulo, datos, campos):
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    y_position = height - 50  # Posición inicial

    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, y_position, titulo)
    y_position -= 30

    p.setFont("Helvetica", 10)
    for item in datos:
        for i, campo in enumerate(campos):
            valor = getattr(item, campo, "")
            if hasattr(valor, "strftime"):  # Si es una fecha
                valor = valor.strftime('%d/%m/%Y %H:%M')
            p.drawString(50, y_position, f"{campo.capitalize()}: {valor}")
            y_position -= 15

        y_position -= 20
        if y_position < 50:  # Nueva página si no hay espacio
            p.showPage()
            y_position = height - 50

    p.showPage()
    p.save()
    return response

# ---- REPORTES PDF ----

def generar_pdf_equipos(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="equipos.pdf"'
    equipos = Equipo.objects.all()
    return generar_pdf(response, "Reporte de Equipos", equipos, ["nombre", "descripcion", "ubicacion", "obra", "responsable", "fecha_registro"])

def generar_pdf_obras(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="obras.pdf"'
    obras = Obra.objects.all()
    return generar_pdf(response, "Reporte de Obras", obras, ["nombre", "descripcion", "fecha_inicio", "fecha_fin"])

def generar_pdf_ubicaciones(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ubicaciones.pdf"'
    ubicaciones = Ubicacion.objects.all()
    return generar_pdf(response, "Reporte de Ubicaciones", ubicaciones, ["nombre", "descripcion"])

def generar_pdf_responsables(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="responsables.pdf"'
    responsables = Responsable.objects.all()
    return generar_pdf(response, "Reporte de Responsables", responsables, ["nombre", "cargo"])

def exportar_excel(request):
    # Datos de ejemplo (ajusta esto según tu modelo)
    data = {
        'ID': [1, 2, 3],
        'Nombre': ['Excavadora', 'Grúa', 'Camión'],
        'Ubicación': ['Obra A', 'Obra B', 'Obra C'],
    }

    df = pd.DataFrame(data)  # Crear DataFrame
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="equipos.xlsx"'
    df.to_excel(response, index=False)  # Generar Excel

    return response

def generar_grafico():
    obras = Obra.objects.annotate(num_equipos=Count('equipo'))
    nombres = [obra.nombre for obra in obras]
    cantidades = [obra.num_equipos for obra in obras]
    
    plt.figure(figsize=(6,4))
    plt.bar(nombres, cantidades, color='skyblue')
    plt.xlabel('Obras')
    plt.ylabel('Cantidad de Equipos')
    plt.title('Equipos por Obra')
    plt.xticks(rotation=45)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.getvalue()).decode()
    return imagen_base64

def dashboard(request):
    grafico = generar_grafico()
    return render(request, 'dashboard.html', {'grafico': grafico})
