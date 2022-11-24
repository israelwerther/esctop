from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from projeto.cliente.models import Cliente
from projeto.cliente_cnpj.models import Cliente_cnpj
from projeto.avalista.models import Avalista

from itertools import chain

from .forms import CreateUserForm, User


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

        aniversariantes_representante_esctop = Cliente_cnpj.objects.filter(
            rep_data_nasc__month=date.today().month,
            rep_data_nasc__day=date.today().day
        )

        aniversariantes_fiador_esctop = Avalista.objects.filter(
            fiador_data_nasc__month=date.today().month,
            fiador_data_nasc__day=date.today().day
        )

        total_aniversariantes = aniversariantes_credcoop.count() + aniversariantes_representante_esctop.count() + aniversariantes_fiador_esctop.count()
        
        context['total_aniversariantes'] = total_aniversariantes

        return context


class Aniversariantes(LoginRequiredMixin, TemplateView):
    template_name = 'aniversariantes_lista.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super(Aniversariantes, self).get_context_data(**kwargs)

        aniversariantes_credcoop = Cliente.objects.filter(
            data_nasc__month=date.today().month,
            data_nasc__day=date.today().day
        )

        aniversariantes_representante_esctop = Cliente_cnpj.objects.filter(
            rep_data_nasc__month=date.today().month,
            rep_data_nasc__day=date.today().day
        )

        aniversariantes_fiador_esctop = Avalista.objects.filter(
            fiador_data_nasc__month=date.today().month,
            fiador_data_nasc__day=date.today().day
        )

        result_list = list(chain(aniversariantes_credcoop, aniversariantes_representante_esctop, aniversariantes_fiador_esctop))
        
        context['aniversariantes'] = result_list

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


class SignUpView(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    queryset = User.objects.all()

    def get_success_url(self):
        return reverse('login')


index = Index.as_view()
aniversariantes = Aniversariantes.as_view()
