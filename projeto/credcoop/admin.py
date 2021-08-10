from projeto.credcoop.models import ClienteCredcoop, Contato, DadosBancarios, DadosPessoais, Endereco, LocalDeTrabalho, Referencias
from django.contrib import admin

# Register your models here.

admin.site.register(DadosPessoais)
admin.site.register(Endereco)
admin.site.register(Contato)
admin.site.register(Referencias)
admin.site.register(LocalDeTrabalho)
admin.site.register(DadosBancarios)
admin.site.register(ClienteCredcoop)
