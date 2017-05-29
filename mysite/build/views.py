from rest_framework import viewsets
from .serializers import BuildSerializer
from .models import Build

class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer