from django.shortcuts import render
from .models import Publication
from .serializers import PublicationSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from utilities.permissions import IsOwner

# Create your views here.

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    paginate_by = 20
    permission_classes = (IsOwner,)