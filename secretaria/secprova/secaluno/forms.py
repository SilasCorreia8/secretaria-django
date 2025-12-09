from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'cpf', 'dataNascimento']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'idade': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'dataNascimento': forms.TextInput(attrs={'class': 'form-control'}),
        }