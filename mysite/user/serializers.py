from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name','email','')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.passwd = validated_data.get('passwd', instance.passwd)
        instance.email = validated_data.get('email', instance.email)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance

    def delete (self,validated_data):
        return User.objects.delete(**validated_data)