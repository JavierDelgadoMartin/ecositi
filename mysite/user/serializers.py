from rest_framework import serializers
from .models import Perfil


class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = ('user_fk','first_name', 'last_name', 'city', 'state', 'birth_date', 'photo','point')

