from rest_framework import routers
from category import views


routerCategory = routers.SimpleRouter()
routerCategory.register(r'Category',views.CategoryViewSet)