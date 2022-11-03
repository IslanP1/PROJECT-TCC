from django.urls import path
from .views import *

urlpatterns = [
    path('', TrabalhoList.as_view(), name='index'),
    path('criar/tcc/', TrabalhoCreate.as_view(), name='criar_trabalhos'),
    path('editar/tcc/<int:pk>/', TrabalhoUpdate.as_view(), name='editar_trabalhos'),
    path('deletar/tcc/<int:pk>/', TrabalhoDelete.as_view(), name='deletar_trabalhos'),
    path('listar/tcc/', TrabalhoList.as_view(), name='listar_trabalhos'),
]