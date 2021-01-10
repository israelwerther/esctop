from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Cliente_cnpj
from projeto.avalista.models import Avalista
from .forms import Cliente_cnpjForm
from projeto.avalista.forms import AvalistaForm

@login_required
def cliente_cnpj_list(request):
    template_name='cliente_cnpj_list.html'
    objects=Cliente_cnpj.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)
    


@login_required
def cliente_cnpj_cadastra(request):
    cnpjs = Cliente_cnpj.objects.all()    
    form = Cliente_cnpjForm()    
    data = {'cnpjs': cnpjs,'form': form} 
    return render(request, 'cliente_cnpj_form.html', data)

@login_required
def cliente_cep(request):
    cnpjs = Cliente_cnpj.objects.all()    
    form = Cliente_cnpjForm()    
    data = {'cnpjs': cnpjs,'form': form} 
    return render(request, 'testecep.html', data)


@login_required
def cliente_cnpj_add(request): 
    form=Cliente_cnpjForm(request.POST or None)    
    if form.is_valid():
        form.save()       
    return redirect('cliente_cnpj:cliente_cnpj_list')


@login_required
def cliente_cnpj_detail(request, pk):
    template_name='cliente_cnpj_detail.html'
    obj=Cliente_cnpj.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)
    # template_name='cliente_cnpj_form.html'
    # form_class=Cliente_cnpjForm
    # form1 = AvalistaForm(request.POST or None)
    # form2 = TesteForm(request.POST or None)


@login_required
def cliente_cnpjupdate(request, pk):
    data = {}
    cliente_cnpj = Cliente_cnpj.objects.get(pk=pk)
    form = Cliente_cnpjForm(request.POST or None, instance=cliente_cnpj)
    data['cliente_cnpj'] = cliente_cnpj
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cliente_cnpj:cliente_cnpj_list')
        else:
            # messages.error(request, 'Dados inválidos')
            return render(request, 'cliente_cnpj_form.html', data)  
    else:
        return render(request, 'cliente_cnpj_form.html', data) 


class Cliente_cnpjDelete(DeleteView):
    model=Cliente_cnpj
    template_name ='cliente_cnpj_delete.html'    
    success_url = reverse_lazy('cliente_cnpj:cliente_cnpj_list')

    

# class Cliente_cnpjUpdate(UpdateView):
#     model=Cliente_cnpj   
#     model1=Avalista   
#     template_name='cliente_cnpj_form.html'
#     form_class = Cliente_cnpjForm

