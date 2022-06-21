from django import forms
from .models import Cliente_cnpj


class Cliente_cnpjForm(forms.ModelForm):
    class Meta:
        model = Cliente_cnpj
        fields = '__all__'
        widgets = {
            'ref1_nome': forms.TextInput(attrs={'placeholder': 'Refencia 1'}),
            'ref2_nome': forms.TextInput(attrs={'placeholder': 'Refencia 2'}),            
            'complemento': forms.TextInput(attrs={'placeholder': 'Ex: Apt A, BL B'}),   
            'rep_conjuge_nome': forms.TextInput(attrs={'placeholder': 'Opcional'}), 
            'rep_conjuge_cpf': forms.TextInput(attrs={'placeholder': 'Opcional'}), 
            'rep_conjuge_telefone': forms.TextInput(attrs={'placeholder': 'Opcional'}),          
        }


