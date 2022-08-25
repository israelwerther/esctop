from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from .models import Emprestimo, EmprestimoPagamento, Cliente, Cliente_cnpj
from .forms import EmprestimoForm, EmprestimoPagamentoForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils import timezone
from django.http import JsonResponse


@login_required
def emprestimo_list(request):    
    template_name='emprestimo_list.html'  
    objects=Emprestimo.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)


@login_required
def emprestimo_cnpj_list(request):    
    template_name='emprestimo_cnpj_list.html'
    objects=Emprestimo.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)


# (LoginRequiredMixin, CreateView):
class EmprestimoCreate(CreateView):
    model=Emprestimo
    template_name='emprestimo_form.html'
    form_class=EmprestimoForm
    
    def form_valid(self, form_class):
        obj = form_class.save(commit=False)
        obj.funcionario = self.request.user
        return super(EmprestimoCreate, self).form_valid(form_class)


class EmprestimoCreateCredcoop(CreateView):
    model=Emprestimo
    template_name='emprestimo_form_credcoop.html'
    form_class=EmprestimoForm
    
    def form_valid(self, form_class):
        obj = form_class.save(commit=False)
        obj.funcionario = self.request.user
        return super(EmprestimoCreateCredcoop, self).form_valid(form_class)


class EmprestimoCompostoCreateCredcoop(CreateView):
    model=Emprestimo
    template_name='emprestimo_form_credcoop_composto.html'
    form_class=EmprestimoForm

    def get_context_data(self, **kwargs):
        context = super(EmprestimoCompostoCreateCredcoop, self).get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context
    
    def form_valid(self, form_class):
        obj = form_class.save(commit=False)
        obj.funcionario = self.request.user
        return super(EmprestimoCompostoCreateCredcoop, self).form_valid(form_class)


class EmprestimoCNPJCreate(CreateView):
    model=Emprestimo
    template_name='emprestimo_cnpj_form.html'
    form_class=EmprestimoForm
    
    def form_valid(self, form_class):
        obj = form_class.save(commit=False)
        obj.funcionario = self.request.user
        return super(EmprestimoCNPJCreate, self).form_valid(form_class)        
    

class EmprestimoCreateEsctop(CreateView):
    model=Emprestimo
    template_name='emprestimo_form_esctop.html'
    form_class=EmprestimoForm
    
    def form_valid(self, form_class):
        obj = form_class.save(commit=False)
        obj.funcionario = self.request.user
        return super(EmprestimoCreateEsctop, self).form_valid(form_class)
    

class EmprestimoCompostoCreateEsctop(CreateView):
    model=Emprestimo
    template_name='emprestimo_form_esctop_composto.html'
    form_class=EmprestimoForm

    def get_context_data(self, **kwargs):
        context = super(EmprestimoCompostoCreateEsctop, self).get_context_data(**kwargs)
        context['clientes_cnpj'] = Cliente_cnpj.objects.all()
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.funcionario = self.request.user
        return super(EmprestimoCompostoCreateEsctop, self).form_valid(form)
    
class EmprestimoUpdate(UpdateView):
    model=Emprestimo
    template_name='emprestimo_form.html'
    form_class=EmprestimoForm

    def form_valid(self, form_class):
        obj = form_class.save(commit=False)
        obj.funcionario = self.request.user
        return super(EmprestimoUpdate, self).form_valid(form_class)

    
class EmprestimoDelete(DeleteView):
    model=Emprestimo
    template_name ='emprestimo_delete.html'    
    success_url = reverse_lazy('emprestimo:emprestimo_list')  


class EmprestimoImpress(UpdateView):
    model=Emprestimo
    template_name='emprestimo_impress.html'
    form_class=EmprestimoForm


class EmprestimoCarne(UpdateView):
    model=Emprestimo
    template_name='emprestimo_carne.html'
    form_class=EmprestimoForm
    

class EmprestimoPromissoria(UpdateView):
    model=Emprestimo
    template_name='emprestimo_promissoria.html'
    form_class=EmprestimoForm

class EmprestimoPromissoriaRenegociacao(UpdateView):
    model=Emprestimo
    template_name='emprestimo_promissoria_renegociacao.html'
    form_class=EmprestimoForm


class EmprestimoContratoCNPJ(UpdateView):
    model=Emprestimo
    template_name='emprestimo_contrato_cnpj.html'
    form_class=EmprestimoForm


class EsctopPromissoria(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='impressos_esctop/esctop_promissoria.html'
    
    def get_context_data(self, **kwargs):
        context = super(EsctopPromissoria, self).get_context_data(**kwargs)
		
        return context

class EsctopContrato(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='impressos_esctop/esctop_contrato.html'
    
    def get_context_data(self, **kwargs):
        context = super(EsctopContrato, self).get_context_data(**kwargs)
		
        return context


class EsctopContratoPromissoria(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='impressos_esctop/esctop_contrato_e_promissoria.html'
    
    def get_context_data(self, **kwargs):
        context = super(EsctopContratoPromissoria, self).get_context_data(**kwargs)
		
        return context


class CredcoopContrato(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='impressos_credcoop/credcoop_contrato.html'
    
    def get_context_data(self, **kwargs):
        context = super(CredcoopContrato, self).get_context_data(**kwargs)
		
        return context


class CredcoopContratoPromissoria(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='impressos_credcoop/credcoop_contrato_e_promissoria.html'
    
    def get_context_data(self, **kwargs):
        context = super(CredcoopContratoPromissoria, self).get_context_data(**kwargs)
		
        return context       


class CredcoopPromissoria(DetailView):
    def test_func(self):
        return self.request.user.is_superuser

    model=Emprestimo
    template_name='impressos_credcoop/credcoop_promissoria.html'
    
    def get_context_data(self, **kwargs):
        context = super(CredcoopPromissoria, self).get_context_data(**kwargs)
		
        return context        


class EmprestimoContratoCNPJRenegociacao(UpdateView):
    model=Emprestimo
    template_name='emprestimo_contrato_cnpj_renegociacao.html'
    form_class=EmprestimoForm

class EmprestimoContratoCPF(UpdateView):
    model=Emprestimo
    template_name='emprestimo_contrato_cpf.html'
    form_class=EmprestimoForm
    
class EmprestimoContratoCPFRenegociacao(UpdateView):
    model=Emprestimo
    template_name='emprestimo_contrato_cpf_renegociacao.html'
    form_class=EmprestimoForm


@login_required
def emprestimo_detail(request, pk):
    template_name='emprestimo_detail.html'
    obj=Emprestimo.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)


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


class EmprestimoCreateView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):    
    template_name = 'form_emprestimo.html'

    def test_func(self):
        return self.request.user.is_superuser

