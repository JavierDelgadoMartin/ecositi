from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(self,data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


    def user_detail(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
        except user.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = UserSerializer(user)
            return JSONResponse(serializer.data)

        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = UserSerializer(user, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        if request.method == 'DELETE':
            user.delete()
            return HttpResponse(status=204)

