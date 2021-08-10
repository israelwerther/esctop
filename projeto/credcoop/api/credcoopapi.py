from projeto.credcoop.models import ClienteCredcoop
from projeto.credcoop.serializers.credcoopserializer import ClienteCredcoopSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.mixins import LoginRequiredMixin

class ClienteCredcoopListAPIView(LoginRequiredMixin, generics.ListAPIView):
    queryset = ClienteCredcoop.objects.all()
    serializer_class = ClienteCredcoopSerializer
    csrf_protect = False