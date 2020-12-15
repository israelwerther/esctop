from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):    
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'complemento': forms.TextInput(attrs={'placeholder': 'Ex: Apt A, BL B'}),             
            'ref1_nome': forms.TextInput(attrs={'placeholder': 'Refencia 1'}),
            'ref2_nome': forms.TextInput(attrs={'placeholder': 'Refencia 2'}),            
            'ref3_nome': forms.TextInput(attrs={'placeholder': 'Refencia 3'}),            
            'complemento': forms.TextInput(attrs={'placeholder': 'Ex: Apt A, BL B'}), 
            'conjuge_nome': forms.TextInput(attrs={'placeholder': 'Opcional'}), 
            'conjuge_cpf': forms.TextInput(attrs={'placeholder': 'Opcional'}), 
            'conjuge_telefone': forms.TextInput(attrs={'placeholder': 'Opcional'}), 
        }
    # def existe_cpf(self):
    #     cpf = self.cleaned_data['cpf']
    #     if Cliente.objects.filter(cpf=cpf).exists():
    #         print("CPF já existe")
    #         raise forms.ValidationError('CPF ja cadastrado!')
    #     return cpf   
        
