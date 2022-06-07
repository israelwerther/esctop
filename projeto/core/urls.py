from django.urls import path
from projeto.core import views as v


app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('aniversariantes_lista/', v.aniversariantes, name='aniversariantes'),
    path('cliente_select/', v.cliente_select, name='cliente_select'),
    path('fiador_decision/', v.fiador_decision, name='fiador_decision'),
    path('fiador_decision_1/', v.fiador_decision_1, name='fiador_decision_1'),
]
