from rest_framework import viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend

from clients.serializers import ClientSerializer
from clients.models import Client

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    """List all clients"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'cpf']
    ordering_fields = ['name']
    filterset_fields = ["active"]