from user import views
from rest_framework import routers


routerPerfil = routers.SimpleRouter()
routerPerfil.register(r'perfil',views.PerfilViewSet)