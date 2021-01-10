from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente_cnpj import views as v

app_name='cliente_cnpj' 

urlpatterns = [
    path('', v.cliente_cnpj_list, name='cliente_cnpj_list'),   
    path('<int:pk>/', v.cliente_cnpj_detail, name='cliente_cnpj_detail'),
    path('cadastra/', v.cliente_cnpj_cadastra, name='cliente_cnpj_cadastra'),
    path('cep/', v.cliente_cep, name='cliente_cep'),
    path('cliente_cnpj_add/', v.cliente_cnpj_add, name='cliente_cnpj_add'),
    # path('add/', login_required(v.Cliente_CnpjCreate.as_view()), name='cliente_cnpj_add'),
    # path('<int:pk>/edit/', login_required(v.Cliente_cnpjUpdate.as_view()), name='cliente_cnpj_edit'),    
    path('<int:pk>/edit/', v.cliente_cnpjupdate, name='cliente_cnpjupdate'),
    path('<int:pk>/delete/', login_required(v.Cliente_cnpjDelete.as_view()), name='cliente_cnpj_delete'),
]