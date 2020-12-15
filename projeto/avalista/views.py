from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Avalista
from .forms import AvalistaForm

@login_required
def avalista_list(request):    
    objects = Avalista.objects.all()   
    template_name='avalista_list.html'
    context={'object_list': objects}
    return render(request, template_name, context)


@login_required
def avalista_detail(request, pk):
    template_name='avalista_detail.html'
    obj=Avalista.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)


@login_required
def avalista_cadastra(request):
    form = AvalistaForm()    
    avalistas = Avalista.objects.all()    
    data = {'avalistas': avalistas,'form': form} 
    return render(request, 'avalista_form.html', data)


@login_required
def avalista_add(request):
    form = AvalistaForm(request.POST or None)   
    if form.is_valid():
        form.save()        
    return redirect('cliente_cnpj:cliente_cnpj_cadastra')


class AvalistaUpdate(UpdateView):
    model=Avalista
    template_name='avalista_form.html'
    form_class = AvalistaForm
    success_url = reverse_lazy('avalista:avalista_list')


class AvalistaDelete(DeleteView):
    model=Avalista
    template_name ='avalista_delete.html'    
    success_url = reverse_lazy('avalista:avalista_list')


# def avalista_add(request):
#     form_avalista = AvalistaForm()
#     form_teste = TesteForm()
#     if request.method == 'POST':
#         if form_avalista.is_valid():
#             form_avalista.save()
#         if form_teste.is_valid():
#             form_teste.save()
#     return render(request, 'avalista_form.html', {'form1': form_avalista, 'form2': form_teste})