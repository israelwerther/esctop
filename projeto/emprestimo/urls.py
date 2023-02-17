from django.contrib.auth.decorators import login_required
from django.urls import path, include
from projeto.emprestimo import views as v

app_name='emprestimo' 

urlpatterns = [

    # Credcoop
    path('formulario-emprestimo-credcoop/', login_required(v.CredcoopEmprestimoCreate.as_view()), name='credcoop_emprestimo_form'),
    path('emprestimos-credcoop/', login_required(v.CredcoopEmprestimoList.as_view()), name='credcoop_emprestimo_list'),

    # Credcoop Impressos
    path('<int:pk>/credcoop_promissoria/', login_required(v.CredcoopPromissoria.as_view()), name='credcoop_promissoria'),
    path('<int:pk>/credcoop_contrato/', login_required(v.CredcoopContrato.as_view()), name='credcoop_contrato'),
    path('<int:pk>/credcoop_contrato_e_promissoria/', login_required(v.CredcoopContratoPromissoria.as_view()), name='credcoop_contrato_e_promissoria'),

    # Esctop
    path('formulario-emprestimo-esctop/', login_required(v.EsctopEmprestimoCreate.as_view()), name='esctop_emprestimo_form'),
    path('emprestimos-esctop/', login_required(v.EsctopEmprestimoList.as_view()), name='esctop_emprestimo_list'),    
    
    # Esctop impressos
    path('<int:pk>/esctop_promissoria/', login_required(v.EsctopPromissoria.as_view()), name='esctop_promissoria'),
    path('<int:pk>/esctop_contrato/', login_required(v.EsctopContrato.as_view()), name='esctop_contrato'),
    path('<int:pk>/esctop_contrato_e_promissoria/', login_required(v.EsctopContratoPromissoria.as_view()), name='esctop_contrato_e_promissoria'),


    path('emprestimo-delete/<int:pk>/', login_required(v.EmprestimoDelete.as_view()), name='emprestimo_delete'),
    path('detalhes-emprestimo/<int:pk>/', login_required(v.EmprestimoDetail.as_view()), name='emprestimo_detail'),

    path('<int:pk>/pagamento_add/', v.emprestimo_pagamento_add, name='emprestimo_pagamento_add'),
    path('<int:pk>/pagamento/', v.emprestimo_pagamento, name='emprestimo_pagamento'),
    path('<int:pk>/pagamento_list/', v.emprestimo_pagamento_list, name='emprestimo_pagamento_list'),
]
