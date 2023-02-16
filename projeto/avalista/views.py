from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.core.paginator import Paginator
from .models import Avalista
from .forms import AvalistaForm

from django.db.models.query_utils import Q


class EsctopAvalistaDelete(DeleteView):
    model=Avalista
    template_name ='esctop_avalista_delete.html'
    success_url = reverse_lazy('avalista:esctop_avalista_list')


class EsctopAvalistaCreate(CreateView):
    model=Avalista
    template_name='esctop_avalista_form.html'
    form_class=AvalistaForm


class EsctopAvalistaList(ListView):
    model=Avalista
    template_name='esctop_avalista_list.html'
    paginate_by = 20
    context_object_name = "objects"

    def get_queryset(self):
        queryset=super().get_queryset()

        if self.request.GET.get('search_by'):
            queryset = queryset.filter(
                Q(
                    Q(fiador_nome__icontains=self.request.GET.get('search_by'))|                    
                    Q(fiador_cpf__icontains=self.request.GET.get('search_by'))
                )
            )

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(EsctopAvalistaList, self).get_context_data(**kwargs)
        context['params'] = self.request.META['QUERY_STRING']
		
        context['search_by'] = self.request.GET.get('search_by')		

        return context


class EsctopAvalistaDetail(DetailView):
    model = Avalista
    template_name = 'esctop_avalista_detail.html'
    form_class=AvalistaForm


class AvalistaUpdate(UpdateView):
    model=Avalista
    template_name='avalista_form.html'
    form_class = AvalistaForm
    success_url = reverse_lazy('avalista:esctop_avalista_list')


class EsctopFiadorUpdate(UpdateView):
    model=Avalista
    template_name='esctop_avalista_form.html'
    form_class = AvalistaForm
    success_url = reverse_lazy('avalista:esctop_avalista_list')



