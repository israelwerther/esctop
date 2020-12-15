from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.avalista import views as v

app_name='avalista' 

urlpatterns = [      
    path('avalista/', v.avalista_list, name='avalista_list'),
    path('<int:pk>/', v.avalista_detail, name='avalista_detail'),
    path('cadastra/', v.avalista_cadastra, name='avalista_cadastra'),
    path('avalista_add/', v.avalista_add, name='avalista_add'),
    path('<int:pk>/edit/', login_required(v.AvalistaUpdate.as_view()), name='avalista_edit'),
    # path('avalista_add/', login_required(v.AvalistaCreate.as_view()), name='avalista_add'),
    path('<int:pk>/delete/', login_required(v.AvalistaDelete.as_view()), name='avalista_delete'),

]
