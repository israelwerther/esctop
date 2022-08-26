from django.contrib.auth.decorators import login_required
from django.urls import path, include
from projeto.emprestimo import views as v
# from .views import emprestimo_pagamento

app_name='emprestimo' 

urlpatterns = [
    
    path('create_esctop_composto/', login_required(v.EmprestimoCompostoCreateEsctop.as_view()), name='create_esctop_composto'),

    path('cnpj_list', v.emprestimo_cnpj_list, name='emprestimo_cnpj_list'),
    path('<int:pk>/delete/', login_required(v.EmprestimoDelete.as_view()), name='emprestimo_delete'),
    path('<int:pk>/carne/', login_required(v.EmprestimoCarne.as_view()), name='emprestimo_carne'),
    path('<int:pk>/promissoria/', login_required(v.EmprestimoPromissoria.as_view()), name='emprestimo_promissoria'),
    path('<int:pk>/promissoria_renegociacao/', login_required(v.EmprestimoPromissoriaRenegociacao.as_view()), name='emprestimo_promissoria_renegociacao'),
    # path('<int:pk>/contrato/', login_required(v.EmprestimoContrato.as_view()), name='emprestimo_contrato'),
    path('<int:pk>/contrato_cnpj/', login_required(v.EmprestimoContratoCNPJ.as_view()), name='emprestimo_contrato_cnpj'),
    path('<int:pk>/contrato_cnpj_renegociacao/', login_required(v.EmprestimoContratoCNPJRenegociacao.as_view()), name='emprestimo_contrato_cnpj_renegociacao'),
    path('<int:pk>/contrato_cpf/', login_required(v.EmprestimoContratoCPF.as_view()), name='emprestimo_contrato_cpf'),
    path('<int:pk>/contrato_cpf_renegociacao/', login_required(v.EmprestimoContratoCPFRenegociacao.as_view()), name='emprestimo_contrato_cpf_renegociacao'),
    path('<int:pk>/', v.emprestimo_detail, name='emprestimo_detail'),

    # Lembrar de verificar necessidade de manter esta url abaixo ou talvez criar uma tela oculta de edião de meprestimo
    # para treino apenas.
    # path('<int:pk>/edit/', login_required(v.EmprestimoUpdate.as_view()), name='emprestimo_edit'),

    path('<int:pk>/pagamento_add/', v.emprestimo_pagamento_add, name='emprestimo_pagamento_add'),
    path('<int:pk>/pagamento/', v.emprestimo_pagamento, name='emprestimo_pagamento'),
    path('<int:pk>/pagamento_list/', v.emprestimo_pagamento_list, name='emprestimo_pagamento_list'),
    path('simular/', v.EmprestimoCreateView.as_view(), name='form_emprestimo'),

    # Credcoop
    path('create_credcoop_composto/', login_required(v.EmprestimoCompostoCreateCredcoop.as_view()), name='create_credcoop_composto'),
    path('', v.emprestimo_list, name='emprestimo_list'),

    # Impressões Credcoop
    path('<int:pk>/credcoop_promissoria/', login_required(v.CredcoopPromissoria.as_view()), name='credcoop_promissoria'),
    path('<int:pk>/credcoop_contrato/', login_required(v.CredcoopContrato.as_view()), name='credcoop_contrato'),
    path('<int:pk>/credcoop_contrato_e_promissoria/', login_required(v.CredcoopContratoPromissoria.as_view()), name='credcoop_contrato_e_promissoria'),

    # Esctop

    # Impressões Esctop
    path('<int:pk>/esctop_promissoria/', login_required(v.EsctopPromissoria.as_view()), name='esctop_promissoria'),
    path('<int:pk>/esctop_contrato/', login_required(v.EsctopContrato.as_view()), name='esctop_contrato'),
    path('<int:pk>/esctop_contrato_e_promissoria/', login_required(v.EsctopContratoPromissoria.as_view()), name='esctop_contrato_e_promissoria'),

]