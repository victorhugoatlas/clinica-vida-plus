from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'idade', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Nome completo do paciente'
            }),
            'idade': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Ex: 35',
                'min': '0'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': '(62) 99999-9999'
            }),
        }