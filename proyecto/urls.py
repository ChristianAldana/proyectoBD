"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Views.HomeView import  HomeView

urlpatterns = [
    path('', HomeView.home, name='home'),

    path('formulario/', HomeView.formulario, name='formularioRuta'),
    path('agregarpaciente/', HomeView.agregar_paciente, name='agregarPaciente'),
    path('editarPaciente/', HomeView.editar_paciente, name='editarPaciente'),
    path('eliminarPaciente/', HomeView.eliminar_paciente, name='eliminarPaciente'),

    path('datosDoctor/', HomeView.datos_doctor, name='datosDoctor'),
    path('editarDoctor/', HomeView.editar_doctor, name='editarDoctor'),
    path('agregarDoctor/', HomeView.agregar_doctor, name='agregarDoctor'),
    path('eliminarDoctor/', HomeView.eliminar_doctor, name='eliminarDoctor'),


]
