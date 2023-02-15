from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente_cnpj import views as v

app_name='cliente_cnpj'

urlpatterns = [
    path('esctop-decision/', login_required(v.EsctopDecision.as_view()), name='esctop_decision'),
    path('formulario-cliente-esctop/', login_required(v.EsctopCreate.as_view()), name='esctop_add'),
    path('<int:pk>/atualiza-cliente-esctop/', login_required(v.EsctopUpdate.as_view()), name='esctop_update'),
    path('<int:pk>/esctop-delete/', login_required(v.EsctopDelete.as_view()), name='esctop_delete'),
    path('clientes-esctop/', login_required(v.EsctopClientList.as_view()), name='esctop_cliente_list'),
    path('detalhes-cliente-esctop/<int:pk>/', login_required(v.EsctopDetail.as_view()), name='cliente_cnpj_detail'),
]