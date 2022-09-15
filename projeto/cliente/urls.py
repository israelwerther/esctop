from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente import views as v

app_name='cliente' 

urlpatterns = [
    path('clientes-credcoop/', login_required(v.CredcoopClienteList.as_view()), name='credcoop_cliente_list'),
    # path('', v.cliente_list, name='cliente_list'),
    path('<int:pk>/', v.cliente_detail, name='cliente_detail'),
    path('add/', login_required(v.ClienteCreate.as_view()), name='cliente_add'),
    path('add_fiador/', login_required(v.FiadorCreate.as_view()), name='fiador_add'),
    path('<int:pk>/edit/', login_required(v.ClienteUpdate.as_view()), name='cliente_edit'),
    path('<int:pk>/delete/', login_required(v.ClienteDelete.as_view()), name='cliente_delete'),  
]
