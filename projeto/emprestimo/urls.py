from django.contrib.auth.decorators import login_required
from django.urls import path, include
from projeto.emprestimo import views as v
# from .views import emprestimo_pagamento

app_name='emprestimo' 

urlpatterns = [
    path('', v.emprestimo_list, name='emprestimo_list'),
    
    path('add/', login_required(v.EmprestimoCreate.as_view()), name='emprestimo_add'),
    path('create_credcoop/', login_required(v.EmprestimoCreateCredcoop.as_view()), name='create_credcoop'),
    path('create_credcoop_composto/', login_required(v.EmprestimoCompostoCreateCredcoop.as_view()), name='create_credcoop_composto'),

    path('cnpj_add/', login_required(v.EmprestimoCNPJCreate.as_view()), name='emprestimo_cnpj_add'),
    path('create_esctop/', login_required(v.EmprestimoCreateEsctop.as_view()), name='create_esctop'),

    path('cnpj_list', v.emprestimo_cnpj_list, name='emprestimo_cnpj_list'),
    path('<int:pk>/delete/', login_required(v.EmprestimoDelete.as_view()), name='emprestimo_delete'),
    path('<int:pk>/impress/', login_required(v.EmprestimoImpress.as_view()), name='emprestimo_impress'),
    path('<int:pk>/carne/', login_required(v.EmprestimoCarne.as_view()), name='emprestimo_carne'),
    path('<int:pk>/promissoria/', login_required(v.EmprestimoPromissoria.as_view()), name='emprestimo_promissoria'),
    path('<int:pk>/promissoria_renegociacao/', login_required(v.EmprestimoPromissoriaRenegociacao.as_view()), name='emprestimo_promissoria_renegociacao'),
    # path('<int:pk>/contrato/', login_required(v.EmprestimoContrato.as_view()), name='emprestimo_contrato'),
    path('<int:pk>/contrato_cnpj/', login_required(v.EmprestimoContratoCNPJ.as_view()), name='emprestimo_contrato_cnpj'),
    path('<int:pk>/contrato_cnpj_renegociacao/', login_required(v.EmprestimoContratoCNPJRenegociacao.as_view()), name='emprestimo_contrato_cnpj_renegociacao'),
    path('<int:pk>/contrato_cpf/', login_required(v.EmprestimoContratoCPF.as_view()), name='emprestimo_contrato_cpf'),
    path('<int:pk>/contrato_cpf_renegociacao/', login_required(v.EmprestimoContratoCPFRenegociacao.as_view()), name='emprestimo_contrato_cpf_renegociacao'),
    path('<int:pk>/', v.emprestimo_detail, name='emprestimo_detail'),
    path('<int:pk>/edit/', login_required(v.EmprestimoUpdate.as_view()), name='emprestimo_edit'),  
    path('<int:pk>/pagamento_add/', v.emprestimo_pagamento_add, name='emprestimo_pagamento_add'),
    path('<int:pk>/pagamento/', v.emprestimo_pagamento, name='emprestimo_pagamento'),
    path('<int:pk>/pagamento_list/', v.emprestimo_pagamento_list, name='emprestimo_pagamento_list'),
    path('simular/', v.EmprestimoCreateView.as_view(), name='form_emprestimo'),
]