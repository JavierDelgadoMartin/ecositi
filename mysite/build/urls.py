from build import views
from rest_framework import routers

routerBuild = routers.SimpleRouter()
routerBuild.register(r'build',views.BuildViewSet.as_view)