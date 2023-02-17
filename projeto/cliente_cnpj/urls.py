from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente_cnpj import views as v

app_name='cliente_cnpj'

urlpatterns = [
    path('esctop-decision/', login_required(v.EsctopClienteDecision.as_view()), name='esctop_cliente_decision'),
    path('esctop-delete/<int:pk>/', login_required(v.EsctopClienteDelete.as_view()), name='esctop_delete'),
    path('detalhes-cliente-esctop/<int:pk>/', login_required(v.EsctopClienteDetail.as_view()), name='esctop_cliente_detail'),
    path('formulario-cliente-esctop/', login_required(v.EsctopClienteCreate.as_view()), name='esctop_cliente_create'),
    path('atualiza-cliente-esctop/<int:pk>/', login_required(v.EsctopClienteUpdate.as_view()), name='esctop_cliente_update'),
    path('clientes-esctop/', login_required(v.EsctopClientList.as_view()), name='esctop_cliente_list'),
]