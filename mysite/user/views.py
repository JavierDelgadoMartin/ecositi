from rest_framework import viewsets
from .models import Perfil
from rest_framework.response import Response
from .serializers import PerfilSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

    def list(self,request,*args,**kwargs):
        print (request.user)
        return super(PerfilViewSet,self).list(request,*args,**kwargs)