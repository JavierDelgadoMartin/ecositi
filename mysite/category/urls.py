from rest_framework import routers
from category import views


routerCategory = routers.SimpleRouter()
routerCategory.register(r'category',views.CategoryViewSet)