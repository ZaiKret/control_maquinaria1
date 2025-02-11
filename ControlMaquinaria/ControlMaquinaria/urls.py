from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maquinaria.urls')),  # Asegura que tu app está incluida aquí
]
