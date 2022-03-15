from django.contrib import admin
from .models import Banco, Tipo_de_conta, Chave_PIX

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display=(        
        'banco',
        
    )
    search_fields=('banco',)
    list_filter=('banco',)


@admin.register(Tipo_de_conta)
class Tipo_de_contaAdmin(admin.ModelAdmin):
    list_display=(        
        'tipo_de_conta',
        
    )
    search_fields=('tipo_de_conta',)
    list_filter=('tipo_de_conta',)
    
@admin.register(Chave_PIX)
class Chave_PIX(admin.ModelAdmin):
    list_display=(        
        'pix_key_type',
    )
    search_fields=('pix_key_type',)
    list_filter=('pix_key_type',)
