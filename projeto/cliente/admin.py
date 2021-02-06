from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=(        
        'nome',
        'rua',
        'rg',
        'estado_civil',        
        'email',        
        'contato1',        
    )
    search_fields=('nome',)
    list_filter=('rg',)
    