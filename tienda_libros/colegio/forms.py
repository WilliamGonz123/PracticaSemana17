from django import forms
from .models import Carrera, Estudiante, Nota


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'anos', 'activa']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'correo', 'edad', 'carrera']


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['materia', 'valor', 'aprobado', 'estudiante']