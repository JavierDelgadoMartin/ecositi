from rest_framework import serializers
from .models import Category
from django.

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name','description')