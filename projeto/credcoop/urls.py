from projeto.credcoop.api.credcoopapi import ClienteCredcoopListAPIView
from django.urls import path

app_name='credcoop' 

urlpatterns = [
    
    path('api/credcoop', ClienteCredcoopListAPIView.as_view(), name='api_credcoop'),
]
