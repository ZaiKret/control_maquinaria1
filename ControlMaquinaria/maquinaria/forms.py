from django import forms
from .models import Equipo, Obra, Ubicacion, Responsable

class EquipoForm(forms.ModelForm):
    fecha_registro = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Equipo
        fields = '__all__'

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = '__all__'
