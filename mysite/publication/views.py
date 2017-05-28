from django.shortcuts import render
from .models import Publication
from .serializers import PublicationSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class PublicationListAll(ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    paginate_by = 20

class PublicationForUser(ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    paginate_by = 20

    def get_queryset(self):
        return self.queryset.filter
'''class PublicationDetail():

'''