from django.urls import path
from .views import *

urlpatterns = [
    path('', OrientadorList.as_view(), name='index'),
    path('criar/orientador/', OrientadorCreate.as_view(), name='criar_orientadores'),
    path('editar/orientador/<int:pk>/', OrientadorUpdate.as_view(), name='editar_orientadores'),
    path('deletar/orientador/<int:pk>/', OrientadorDelete.as_view(), name='deletar_orientadores'),
    path('listar/orientadores/', OrientadorList.as_view(), name='listar_orientadores'),
]