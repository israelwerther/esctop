from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Cliente_cnpj
from projeto.avalista.models import Avalista
from .forms import Cliente_cnpjForm
from projeto.avalista.forms import AvalistaForm

from django.db.models.query_utils import Q


class EsctopClienteList(ListView):
    model=Cliente_cnpj
    template_name='cliente_cnpj_list.html'
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
        context = super(EsctopClienteList, self).get_context_data(**kwargs)
        context['params'] = self.request.META['QUERY_STRING']		
        context['search_by'] = self.request.GET.get('search_by')
        context['page_title'] = "Clientes Esctop"

        return context


@login_required
def cliente_cnpj_detail(request, pk):
    template_name='esctop_detail.html'
    obj=Cliente_cnpj.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)


class EsctopCreate(CreateView):
    model=Cliente_cnpj
    template_name='esctop_form.html'
    form_class=Cliente_cnpjForm


class EsctopUpdate(UpdateView):
    model=Cliente_cnpj
    template_name='esctop_form.html'
    form_class = Cliente_cnpjForm


class EsctopDecision(CreateView):
    model=Cliente_cnpj
    template_name='esctop_decision.html'
    form_class=Cliente_cnpjForm


class ClienteCnpjCreate(CreateView):
    model=Cliente_cnpj
    template_name='cliente_cnpj_form.html'
    form_class=Cliente_cnpjForm


class Cliente_cnpjUpdate(UpdateView):
    model=Cliente_cnpj   
    model1=Avalista   
    template_name='cliente_cnpj_form.html'
    form_class = Cliente_cnpjForm


class Cliente_cnpjDelete(DeleteView):
    model=Cliente_cnpj
    template_name ='cliente_cnpj_delete.html'    
    success_url = reverse_lazy('cliente_cnpj:cliente_cnpj_list')


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