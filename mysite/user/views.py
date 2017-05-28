from rest_framework import viewsets
from .models import Perfil
from rest_framework.response import Response
from .serializers import PerfilSerializer



class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer