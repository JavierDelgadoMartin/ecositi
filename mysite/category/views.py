from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer

from rest_framework import viewsets

from .serializers import CategorySerializer

from django.contrib.auth.models import User

# Create your views here.


class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
        content = JSONParser().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

	def user_detail(request):
		try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)
