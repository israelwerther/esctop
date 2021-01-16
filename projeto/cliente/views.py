from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm

@login_required
def cliente_list(request):
    template_name='cliente_list.html'
    objects=Cliente.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)


@login_required
def cliente_detail(request, pk):
    template_name='cliente_detail.html'
    obj=Cliente.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)


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

class ClienteCreate(CreateView):
    model=Cliente
    template_name='cliente_form.html'
    form_class=ClienteForm


class FiadorCreate(CreateView):
    model=Cliente       
    template_name='fiador_form.html'
    form_class=ClienteForm
    success_url = reverse_lazy('cliente:cliente_add')
    
    
class ClienteUpdate(UpdateView):
    model=Cliente
    template_name='cliente_form.html'
    form_class = ClienteForm
    #fazer aqui receber o form dos emprestimos filtrados apenas dele
    

class ClienteDelete(DeleteView):
    model=Cliente
    template_name ='cliente_delete.html'    
    success_url = reverse_lazy('cliente:cliente_list')
    

    

    
    