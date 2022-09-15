from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente_cnpj import views as v

app_name='cliente_cnpj' 

urlpatterns = [
    path('clientes-esctop/', login_required(v.EsctopClienteList.as_view()), name='esctop_cliente_list'),
    path('<int:pk>/', v.cliente_cnpj_detail, name='cliente_cnpj_detail'),
    path('add/', login_required(v.ClienteCnpjCreate.as_view()), name='cliente_cnpj_add'),
    # path('add/', login_required(v.Cliente_CnpjCreate.as_view()), name='cliente_cnpj_add'),
    path('<int:pk>/edit/', login_required(v.Cliente_cnpjUpdate.as_view()), name='cliente_cnpjupdate'),    
    # path('<int:pk>/edit/', v.cliente_cnpjupdate, name='cliente_cnpjupdate'),
    path('<int:pk>/delete/', login_required(v.Cliente_cnpjDelete.as_view()), name='cliente_cnpj_delete'),
]