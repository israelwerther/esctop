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


# @login_required
# def avalista_decision(request):
#     return render(request, 'avalista_decision.html')


class AvalistaCreate(CreateView):
    model=Avalista
    template_name='avalista_form.html'
    form_class=AvalistaForm
    

class AvalistaUpdate(UpdateView):
    model=Avalista
    template_name='avalista_form.html'
    form_class = AvalistaForm
    success_url = reverse_lazy('avalista:avalista_list')


class AvalistaDelete(DeleteView):
    model=Avalista
    template_name ='avalista_delete.html'    
    success_url = reverse_lazy('avalista:avalista_list')
