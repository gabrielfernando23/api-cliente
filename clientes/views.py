from rest_framework import viewsets, filters
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
class ClientesViewSet(viewsets.ModelViewSet):
    """Listando todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']