from django.urls import path
from . import views

urlpatterns = [
    path('secaluno/listar/', views.listar, name='listar'),
    path('secaluno/add/', views.addAluno, name='add'),
    path('secaluno/', views.alunos, name='secaluno'),
]