from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deletar/<int:pk>/', views.deletar_paciente, name='deletar_paciente'),
]