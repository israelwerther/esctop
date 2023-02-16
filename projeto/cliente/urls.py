from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente import views as v

app_name='cliente' 

urlpatterns = [
    path('formulario-cliente-credcoop/', login_required(v.CredcoopCreate.as_view()), name='credcoop_add'),
    path('credcoop-decision/', login_required(v.CredcoopDecision.as_view()), name='credcoop_decision'),
    path('clientes-credcoop/', login_required(v.CredcoopClienteList.as_view()), name='credcoop_cliente_list'),
    path('detalhes-cliente-credcoop/<int:pk>/', login_required(v.CredcoopDetail.as_view()), name='credcoop_client_detail'),
    path('<int:pk>/atualiza-cliente-credcoop/', login_required(v.CredcoopUpdate.as_view()), name='credcoop_update'),
    path('<int:pk>/credcoop-delete/', login_required(v.CredcoopDelete.as_view()), name='cliente_delete'),

    # Fiador
    path('formulario-fiador-credcoop/', login_required(v.CredcoopFiadorCreate.as_view()), name='fiador_credcoop_add'),
]
