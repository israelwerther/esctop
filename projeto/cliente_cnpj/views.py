from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from .models import Cliente_cnpj
from projeto.avalista.models import Avalista
from .forms import Cliente_cnpjForm
from projeto.avalista.forms import AvalistaForm
from projeto.emprestimo.models import Emprestimo

from django.db.models.query_utils import Q


class EsctopClienteDecision(CreateView):
    model=Cliente_cnpj
    template_name='esctop_cliente_decision.html'
    form_class=Cliente_cnpjForm


class EsctopClienteDelete(DeleteView):
    model=Cliente_cnpj
    template_name ='esctop_cliente_delete.html'
    success_url = reverse_lazy('cliente_cnpj:esctop_cliente_list')


class EsctopClienteDetail(DetailView):
    model=Cliente_cnpj
    template_name='esctop_cliente_detail.html'
    form_class=Cliente_cnpjForm


class EsctopClienteCreate(CreateView):
    model=Cliente_cnpj
    template_name='esctop_cliente_form.html'
    form_class=Cliente_cnpjForm


class EsctopClienteUpdate(UpdateView):
    model=Cliente_cnpj
    template_name='esctop_cliente_form.html'
    form_class = Cliente_cnpjForm


class EsctopClientList(ListView):
    model=Cliente_cnpj
    template_name='esctop_cliente_list.html'
    paginate_by = 20
    context_object_name = "objects"

    def get_queryset(self):
        queryset=super().get_queryset()

        if self.request.GET.get('search_by'):
            queryset = queryset.filter(
                Q(
                    Q(razao_social__icontains=self.request.GET.get('search_by'))|
                    Q(nome_fantasia__icontains=self.request.GET.get('search_by'))|
                    Q(rep_nome__icontains=self.request.GET.get('search_by'))|
                    Q(cnpj__icontains=self.request.GET.get('search_by'))
                )
            )

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(EsctopClientList, self).get_context_data(**kwargs)
        context['params'] = self.request.META['QUERY_STRING']		
        context['search_by'] = self.request.GET.get('search_by')
        context['page_title'] = "Clientes Esctop"

        return context


class EsctopDashboard(TemplateView):
    template_name='esctop_dashboard.html'

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super(EsctopDashboard, self).get_context_data(**kwargs)

        context['total_loans_esctop'] = Emprestimo.objects.filter(
            cliente_cnpj__pk__isnull=False
        ).count()
        
        context['total_clients_esctop'] = Cliente_cnpj.objects.all().count()

        print("==============", context['total_clients_esctop'])

        return context





# ***********************NÃO APAGAR ESTA VIEW COMENTADA ABAIXO************************
# @login_required
# def cliente_cnpjupdate(request, pk):
#     data = {}
#     cliente_cnpj = Cliente_cnpj.objects.get(pk=pk)
#     form = Cliente_cnpjForm(request.POST or None, instance=cliente_cnpj)
#     data['cliente_cnpj'] = cliente_cnpj
#     data['form'] = form

#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('cliente_cnpj:cliente_cnpj_list')
#         else:
#             # messages.error(request, 'Dados inválidos')
#             return render(request, 'cliente_cnpj_form.html', data)  
#     else:
#         return render(request, 'cliente_cnpj_form.html', data) 