from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from projeto.cliente.models import Cliente
from itertools import chain

from projeto.cliente_cnpj.models import Cliente_cnpj


# @login_required
# def index(request):
#     return render(request, 'index.html')

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    
    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        aniversariantes_credcoop = Cliente.objects.filter(
            data_nasc__month=date.today().month,
            data_nasc__day=date.today().day
        )

        aniversariantes_esctop = Cliente_cnpj.objects.filter(
            fiador__fiador_data_nasc__month=date.today().month,
            fiador__fiador_data_nasc__day=date.today().day
        )

        total_aniversariantes = aniversariantes_credcoop.count() + aniversariantes_esctop.count()
        
        
        
        context['total_aniversariantes'] = total_aniversariantes

        return context


class Aniversariantes(LoginRequiredMixin, TemplateView):
    template_name = 'aniversariantes.html'    

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super(Aniversariantes, self).get_context_data(**kwargs)

        aniversariantes_credcoop = Cliente.objects.filter(
            data_nasc__month=date.today().month,
            data_nasc__day=date.today().day
        )

        aniversariantes_esctop = Cliente_cnpj.objects.filter(
            fiador__fiador_data_nasc__month=date.today().month,
            fiador__fiador_data_nasc__day=date.today().day
        )

        result_list = list(chain(aniversariantes_credcoop, aniversariantes_esctop))
        
        print("@@@@@@@@@@@@@@@@@@@@", result_list)
        
        context['aniversariantes_credcoop'] = result_list

        return context


@login_required
def cliente_select(request):
    return render(request, 'cliente_select.html')


@login_required
def fiador_decision(request):
    return render(request, 'fiador_decision.html')


@login_required
def fiador_decision_1(request):
    return render(request, 'fiador_decision_1.html')

index = Index.as_view()
aniversariantes = Aniversariantes.as_view()
