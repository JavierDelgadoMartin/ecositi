from rest_framework import viewsets
from .models import Category
from rest_framework.response import Response
from .serializers import CategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    