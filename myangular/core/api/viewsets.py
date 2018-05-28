from rest_framework import viewsets, filters
from myangular.core.models import Agenda
from .serializers import AgendaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

#from rest_framework.authentication import SessionAuthentication

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('agenda_id', 'nome', 'telefone')
    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]