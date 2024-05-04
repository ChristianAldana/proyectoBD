from django.http import HttpResponse
from django.template.loader import get_template

class HomeView:

    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def paciente(self):
        plantilla = get_template('paciente.html')
        return HttpResponse(plantilla.render())

    def formulario(self):
        plantilla = get_template('formulario.html')
        return HttpResponse(plantilla.render())

    def agregar_paciente(self):
        plantilla = get_template('agregarPaciente.html')
        return HttpResponse(plantilla.render())

    def editar_paciente(self):
        plantilla = get_template('editarPaciente.html')
        return HttpResponse(plantilla.render())

    def eliminar_paciente(self):
        plantilla = get_template('eliminarPaciente.html')
        return HttpResponse(plantilla.render())

    def datos_doctor(self):
        plantilla = get_template('datosDoctor.html')
        return HttpResponse(plantilla.render())

    def editar_doctor(self):
        plantilla = get_template('editarDoctor.html')
        return HttpResponse(plantilla.render())


    def agregar_doctor(self):
        plantilla = get_template('agregarDoctor.html')
        return HttpResponse(plantilla.render())


    def eliminar_doctor(self):
        plantilla = get_template('eliminarDoctor.html')
        return HttpResponse(plantilla.render())












