# from django.forms import ModelForm
from django import forms
from .models import Emprestimo, EmprestimoPagamento 
from datetime import date


class EmprestimoForm(forms.ModelForm):    
    class Meta:
        model = Emprestimo   
        fields = [
            'funcionario',            
            'cliente',
            'cliente_cnpj',
            'valor_emprestado', 
            'qtd_parcelas',
            'valor_prestacao',            
            'dt_emprestimo',            
            'n_contrato',
            'valor_multa',
            'juros_ao_dia',
            'valor_mutuado',
            'juros_ao_mes',
            'juros_moratorio',
            'multa_por_atraso',
            'iof_real',
            'valor_devido',
            'postergar'
        ]
        

class EmprestimoPagamentoForm(forms.ModelForm):
    class Meta:
        model = EmprestimoPagamento 
        fields = ["valor_pago", "data_pagamento", ]