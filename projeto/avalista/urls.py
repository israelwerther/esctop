from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.avalista import views as v

app_name='avalista' 

urlpatterns = [  
    path('avalista-lista/', login_required(v.AvalistaList.as_view()), name='avalista_list'),
    path('<int:pk>/', v.avalista_detail, name='avalista_detail'),
    # path('decision/', v.avalista_decision, name='avalista_decision'),
    path('<int:pk>/edit/', login_required(v.AvalistaUpdate.as_view()), name='avalista_edit'),
    # path('avalista_add/', login_required(v.AvalistaCreate.as_view()), name='avalista_add'),
    path('<int:pk>/delete/', login_required(v.AvalistaDelete.as_view()), name='avalista_delete'),

    # NOVO
    path('formulario-fiador-esctop/', login_required(v.EsctopAvalistaCreate.as_view()), name='esctop_avalista_add'),
    path('<int:pk>/atualiza-avalista-esctop/', login_required(v.EsctopFiadorUpdate.as_view()), name='esctop_avalista_edit'),

]
