from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente import views as v

app_name='cliente' 

urlpatterns = [
    path('credcoop-decision/', login_required(v.CredcoopClienteDecision.as_view()), name='credcoop_decision'),
    path('credcoop-delete/<int:pk>/', login_required(v.CredcoopClienteDelete.as_view()), name='credcoop_cliente_delete'),
    path('detalhes-cliente-credcoop/<int:pk>/', login_required(v.CredcoopClienteDetail.as_view()), name='credcoop_client_detail'),
    path('formulario-cliente-credcoop/', login_required(v.CredcoopClienteCreate.as_view()), name='credcoop_cliente_create'),
    path('atualiza-cliente-credcoop/<int:pk>/', login_required(v.CredcoopClienteUpdate.as_view()), name='credcoop_update'),
    path('clientes-credcoop/', login_required(v.CredcoopClienteList.as_view()), name='credcoop_cliente_list'),

    # Fiador
    path('formulario-fiador-credcoop/', login_required(v.CredcoopFiadorCreate.as_view()), name='credcoop_fiador_create'),
]
