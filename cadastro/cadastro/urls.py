
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #pagina inicial
    path('',views.home, name='home'),
    #pagina de usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
