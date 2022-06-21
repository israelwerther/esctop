from django.contrib import admin
from .models import Cliente_cnpj

@admin.register(Cliente_cnpj)
class Cliente_cnpjAdmin(admin.ModelAdmin):
    list_display=(        
        'razao_social',
        'nome_fantasia',
        'cnpj',
        'fundacao',
        'inscricao_estadual', 
        'inscricao_municipal',  
    )
    search_fields=('nome_fantasia',)
    list_filter=('email',)


