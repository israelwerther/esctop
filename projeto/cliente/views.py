from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from django.core.paginator import Paginator
from .models import Cliente
from .forms import ClienteForm

from django.db.models.query_utils import Q


# Views do Cliente Credcoop
class CredcoopClienteDecision(CreateView):
    model=Cliente
    template_name='credcoop_cliente_decision.html'
    form_class=ClienteForm


class CredcoopClienteDelete(DeleteView):
    model=Cliente
    template_name ='credcoop_cliente_delete.html'    
    success_url = reverse_lazy('cliente:credcoop_cliente_list')


class CredcoopClienteDetail(DetailView):
    model=Cliente
    template_name='credcoop_cliente_detail.html'
    form_class=ClienteForm


class CredcoopClienteCreate(CreateView):
    model=Cliente
    template_name='credcoop_cliente_form.html'
    form_class=ClienteForm


class CredcoopClienteUpdate(UpdateView):
    model=Cliente
    template_name='credcoop_cliente_form.html'
    form_class = ClienteForm
    #fazer aqui receber o form dos emprestimos filtrados apenas dele


class CredcoopClienteList(ListView):
    model=Cliente
    template_name='credcoop_cliente_list.html'
    paginate_by = 20
    context_object_name = "objects"

    def get_queryset(self):
        queryset=super().get_queryset()

        if self.request.GET.get('search_by'):
            queryset = queryset.filter(
                Q(
                    Q(nome__icontains=self.request.GET.get('search_by'))|
                    Q(rg__icontains=self.request.GET.get('search_by'))|
                    Q(cpf__icontains=self.request.GET.get('search_by'))
                )
            )

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(CredcoopClienteList, self).get_context_data(**kwargs)
        context['params'] = self.request.META['QUERY_STRING']
		
        context['search_by'] = self.request.GET.get('search_by')

        return context


# Views do Fiador Credcoop
class CredcoopFiadorCreate(CreateView):
    model=Cliente       
    template_name='credcoop_fiador_form.html'
    form_class=ClienteForm
    success_url = reverse_lazy('cliente:credcoop_cliente_list')


class CredcoopDashboard(TemplateView):
    template_name='credcoop_dashboard.html'

    def test_func(self):
        return self.request.user.is_superuser

