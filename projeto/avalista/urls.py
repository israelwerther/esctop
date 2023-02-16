from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.avalista import views as v

app_name='avalista' 

urlpatterns = [
    path('delete-avalista-esctop/<int:pk>/', login_required(v.EsctopAvalistaDelete.as_view()), name='esctop_avalista_delete'),
    path('detalhes-avalista-esctop/<int:pk>/', login_required(v.EsctopAvalistaDetail.as_view()), name='esctop_avalista_detail'),
    path('formulario-fiador-esctop/', login_required(v.EsctopAvalistaCreate.as_view()), name='esctop_avalista_create'),
    path('atualiza-avalista-esctop/<int:pk>/', login_required(v.EsctopFiadorUpdate.as_view()), name='esctop_avalista_update'),
    path('avalistas-esctop/', login_required(v.EsctopAvalistaList.as_view()), name='esctop_avalista_list'),
]
