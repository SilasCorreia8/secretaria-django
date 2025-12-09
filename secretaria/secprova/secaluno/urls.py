from django.urls import path
from . import views

urlpatterns = [
    path('secaluno/listar/', views.listar, name='listar'),
    path('secaluno/', views.alunos, name='secaluno'),
]