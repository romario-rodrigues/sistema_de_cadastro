from django.urls import path
from app_cad_usuarios import views # Erro corrigido nessa linha no app_cad_usuarios. Faltava o s em usuarios

urlpatterns = [
    # rota, view responsável, nome de referência
    #usuarios.com
    path('',views.home, name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
