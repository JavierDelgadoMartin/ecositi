from rest_framework import routers
from publication import views


routerPublication = routers.SimpleRouter()
routerPublication.register(r'publication',views.PublicationViewSet)