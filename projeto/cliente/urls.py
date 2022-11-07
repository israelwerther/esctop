from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente import views as v

app_name='cliente' 

urlpatterns = [
    # antigo
    path('formulario-cliente/', login_required(v.ClienteCreate.as_view()), name='cliente_add'),

    # novo
    path('credcoop-decision/', login_required(v.CredcoopDecision.as_view()), name='credcoop_decision'),
    path('formulario-cliente-credcoop/', login_required(v.CredcoopCreate.as_view()), name='credcoop_add'),
    path('<int:pk>/atualiza-cliente-credcoop/', login_required(v.CredcoopUpdate.as_view()), name='credcoop_update'),
    path('formulario-fiador-credcoop/', login_required(v.CredcoopFiadorCreate.as_view()), name='fiador_credcoop_add'),
    
    # novo e antigo
    path('clientes-credcoop/', login_required(v.CredcoopClienteList.as_view()), name='credcoop_cliente_list'),
    path('<int:pk>/', v.cliente_detail, name='cliente_detail'),

    # não sei se está em uso ainda(verificar)

    # path('', v.cliente_list, name='cliente_list'),
    path('add_fiador/', login_required(v.FiadorCreate.as_view()), name='fiador_add'),
    path('<int:pk>/edit/', login_required(v.ClienteUpdate.as_view()), name='cliente_edit'),
    path('<int:pk>/delete/', login_required(v.ClienteDelete.as_view()), name='cliente_delete'),  
]
