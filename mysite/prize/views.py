from rest_framework import viewsets
from .models import Prize
from rest_framework.response import Response
from .serializers import PrizeSerializer


class PrizeViewSet(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer

