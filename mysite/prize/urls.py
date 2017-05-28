from rest_framework import routers
from prize import views


routerPrize = routers.SimpleRouter()
routerPrize.register(r'prize',views.PrizeViewSet)