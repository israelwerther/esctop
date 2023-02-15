from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator
from .models import Cliente
from .forms import ClienteForm

from django.db.models.query_utils import Q


class CredcoopClienteList(ListView):
    model=Cliente
    template_name='cliente_list.html'
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


@login_required
def cliente_detail(request, pk):
    template_name='credcoop_detail.html'
    obj=Cliente.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)


class ClienteCreate(CreateView):
    model=Cliente    
    template_name='cliente_form.html'
    form_class=ClienteForm


class CredcoopCreate(CreateView):
    model=Cliente
    template_name='credcoop_form.html'
    form_class=ClienteForm


class CredcoopUpdate(UpdateView):
    model=Cliente
    template_name='credcoop_form.html'
    form_class = ClienteForm
    #fazer aqui receber o form dos emprestimos filtrados apenas dele


class CredcoopFiadorCreate(CreateView):
    model=Cliente       
    template_name='credcoop_fiador_form.html'
    form_class=ClienteForm
    success_url = reverse_lazy('cliente:credcoop_cliente_list')


class CredcoopDecision(CreateView):
    model=Cliente
    template_name='credcoop_decision.html'
    form_class=ClienteForm


class FiadorCreate(CreateView):
    model=Cliente       
    template_name='fiador_form.html'
    form_class=ClienteForm
    success_url = reverse_lazy('cliente:credcoop_cliente_list')

    
# def ClienteCreate(request):
#     template_name='cliente_form.html'    
#     if request.method == 'POST':
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ClienteForm()
#     context = {
#         'form': form
#     }    
#     return render(request, template_name, context)
    
    
class ClienteUpdate(UpdateView):
    model=Cliente
    template_name='cliente_form.html'
    form_class = ClienteForm
    #fazer aqui receber o form dos emprestimos filtrados apenas dele
    

class ClienteDelete(DeleteView):
    model=Cliente
    template_name ='cliente_delete.html'    
    success_url = reverse_lazy('cliente:credcoop_cliente_list')
    

    

    
    