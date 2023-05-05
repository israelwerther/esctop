from genericpath import exists
from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView, ListView
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.query_utils import Q
from .models import Emprestimo, EmprestimoPagamento, Cliente, Cliente_cnpj
from .forms import EmprestimoForm, EmprestimoPagamentoForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime, timedelta

# Credcoop
class CredcoopEmprestimoCreate(CreateView):
    model=Emprestimo
    template_name='credcoop/credcoop_emprestimo_form.html'
    form_class=EmprestimoForm

    def get_context_data(self, **kwargs):
        context = super(CredcoopEmprestimoCreate, self).get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context
    
    def form_valid(self, form_class):
        obj = form_class.save(commit=False)
        obj.funcionario = self.request.user
        return super(CredcoopEmprestimoCreate, self).form_valid(form_class)


class CredcoopEmprestimoList(ListView):
    model=Emprestimo
    template_name='credcoop/credcoop_emprestimo_list.html'
    paginate_by = 20
    context_object_name = "objects"

    def get_queryset(self):
        queryset=super().get_queryset()
        
        # Filtra apenas clientes credcoop existentes 
        queryset = Emprestimo.objects.filter(
            cliente__isnull=False
        )

        search_by = self.request.GET.get('search_by')
        if search_by:
            queryset = queryset.filter(
                Q(
                    Q(n_contrato__icontains=search_by) |
                    Q(cliente__nome__icontains=search_by)
                )
            )

        data_inicial = self.request.GET.get('data_inicial')
        data_final = self.request.GET.get('data_final')
        
        if data_inicial and data_final:
            data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
            data_final = datetime.strptime(data_final, '%Y-%m-%d')
            data_final += timedelta(days=1)
            queryset = queryset.filter(dt_emprestimo__range=(data_inicial, data_final))

        return queryset

    
    def get_context_data(self, **kwargs):
        context = super(CredcoopEmprestimoList, self).get_context_data(**kwargs)
        context['params'] = self.request.META['QUERY_STRING']		
        context['search_by'] = self.request.GET.get('search_by')
        context['data_inicial'] = self.request.GET.get('data_inicial')
        context['data_final'] = self.request.GET.get('data_final')

        return context


# Credcoop Impressos
class CredcoopContratoPromissoria(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='credcoop_impressos/credcoop_contrato_e_promissoria.html'
    
    def get_context_data(self, **kwargs):
        context = super(CredcoopContratoPromissoria, self).get_context_data(**kwargs)
		
        return context


class CredcoopContrato(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='credcoop_impressos/credcoop_contrato.html'
    
    def get_context_data(self, **kwargs):
        context = super(CredcoopContrato, self).get_context_data(**kwargs)
		
        return context


class CredcoopPromissoria(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='credcoop_impressos/credcoop_promissoria.html'
    
    def get_context_data(self, **kwargs):
        context = super(CredcoopPromissoria, self).get_context_data(**kwargs)
		
        return context


# Esctop
class EsctopEmprestimoCreate(CreateView):
    model=Emprestimo
    template_name='esctop/esctop_emprestimo_form.html'
    form_class=EmprestimoForm

    def get_context_data(self, **kwargs):
        context = super(EsctopEmprestimoCreate, self).get_context_data(**kwargs)
        context['clientes_cnpj'] = Cliente_cnpj.objects.all()
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.funcionario = self.request.user
        return super(EsctopEmprestimoCreate, self).form_valid(form)


class EsctopEmprestimoList(ListView):
    model=Emprestimo
    template_name='esctop/esctop_emprestimo_list.html'
    paginate_by = 20
    context_object_name = "objects"

    def get_queryset(self):
        queryset=super().get_queryset()
        
        # Filtra apenas clientes esctop existentes 
        queryset = Emprestimo.objects.filter(
            cliente_cnpj__isnull=False
        )
        
        if self.request.GET.get('search_by'):
            queryset = queryset.filter(
                Q(
                    Q(cliente_cnpj__razao_social__icontains=self.request.GET.get('search_by'))|
					Q(n_contrato__icontains=self.request.GET.get('search_by'))|
                    Q(cliente_cnpj__cnpj__icontains=self.request.GET.get('search_by'))                    
                )
            )
        
        data_inicial = self.request.GET.get('data_inicial')
        data_final = self.request.GET.get('data_final')
        
        if data_inicial and data_final:
            data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
            data_final = datetime.strptime(data_final, '%Y-%m-%d')
            data_final += timedelta(days=1)
            queryset = queryset.filter(dt_emprestimo__range=(data_inicial, data_final))

        return queryset

    
    def get_context_data(self, **kwargs):
        context = super(EsctopEmprestimoList, self).get_context_data(**kwargs)
        context['params'] = self.request.META['QUERY_STRING']
        context['search_by'] = self.request.GET.get('search_by')
        context['data_inicial'] = self.request.GET.get('data_inicial')
        context['data_final'] = self.request.GET.get('data_final')

        return context


# Esctop Impressos
class EsctopPromissoria(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='esctop_impressos/esctop_promissoria.html'
    
    def get_context_data(self, **kwargs):
        context = super(EsctopPromissoria, self).get_context_data(**kwargs)
		
        return context

class EsctopContrato(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='esctop_impressos/esctop_contrato.html'
    
    def get_context_data(self, **kwargs):
        context = super(EsctopContrato, self).get_context_data(**kwargs)
		
        return context


class EsctopContratoPromissoria(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='esctop_impressos/esctop_contrato_e_promissoria.html'
    
    def get_context_data(self, **kwargs):
        context = super(EsctopContratoPromissoria, self).get_context_data(**kwargs)
		
        return context


# Templates
class EmprestimoDelete(DeleteView):
    model=Emprestimo
    template_name ='emprestimo_delete.html'    
    success_url = reverse_lazy('emprestimo:esctop_emprestimo_list')  


class EmprestimoDetail(DetailView):
    model=Emprestimo
    template_name='emprestimo_detail.html'
    form_class=EmprestimoForm






@login_required
def emprestimo_pagamento_add(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    form = EmprestimoPagamentoForm()
    # pagamentos = emprestimo.emprestimo_set.all()
    context = {'emprestimo': emprestimo, 'form': form}
    return render(request, 'emprestimo_pagamento_add.html', context)

    
@login_required
def emprestimo_pagamento(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    form = EmprestimoPagamentoForm(request.POST or None)
    if form.is_valid():
        emprestimopagamento = form.save(commit=False)
        emprestimopagamento.emprestimo = emprestimo
        emprestimopagamento.save()        
    return redirect('emprestimo:emprestimo_detail', pk)


@login_required
def emprestimo_pagamento_list(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    form = EmprestimoPagamentoForm()
    emprestimos = emprestimo.emprestimopagamento_set.all()
    context = {'emprestimo': emprestimo, 'form': form, 'emprestimos': emprestimos } 
    return render(request, 'emprestimo_pagamento_list.html', context)
