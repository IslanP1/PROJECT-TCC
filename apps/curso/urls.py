from django.urls import path
from .views import *

urlpatterns = [
    path('', CursoList.as_view(), name='index'),
    path('criar/curso/', CursoCreate.as_view(), name='criar_cursos'),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name='editar_cursos'),
    path('deletar/curso/<int:pk>/', CursoDelete.as_view(), name='deletar_cursos'),
    path('listar/curso/', CursoList.as_view(), name='listar_cursos'),
]