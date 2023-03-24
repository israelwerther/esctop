"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    # project
    path('api/', include('projeto.public.urls')),
    path('accounts/', include('projeto.accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('projeto.core.urls')),
    path('produto/', include('projeto.produto.urls')),
    path('emprestimo/', include('projeto.emprestimo.urls')),   
    path('estoque/', include('projeto.estoque.urls')),
    path('credcoop/', include('projeto.cliente.urls')),
    path('esctop/', include('projeto.cliente_cnpj.urls')),
    path('avalista/', include('projeto.avalista.urls')),
    path('accounts-user/', include('django.contrib.auth.urls')),
    
    # Files
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    # API
    path('api/auth/', include('rest_framework.urls'))
]
