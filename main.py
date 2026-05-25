from Subject_manager import Subject_manager
from Subject import Subject
from Task import Task
from Graphs_creator import Graphs_creator
class Program:
    def __init__(self, subject_mn):
        self.running = True
        self.options = [
            {
                "name": "0. Salir",
                "function": self.stop_running
            },
            {
                "name": "1. Ver estado de mis materias",
                "function": self.see_status
            },
            {
                "name": "2. Ver materias",
                "function": self.show_subjects
            },
        ]
        self.subject_manager = subject_mn
        self.graph = Graphs_creator(subject_mn)

    def main(self):
        while self.running:
            self.print_options()
            option = int(input("¿Que opcion elige? \n> "))

            while option > len(self.options) - 1 or option < 0:
                option = int(input("Opción invalida, intente nuevamente \n> "))
            
            selected_option = self.options[option]
            selected_option["function"]()

    def print_options(self):
        for option in self.options:
            print(option["name"])

    def see_status(self):
        self.graph.draw_graph()

    def show_subjects(self):
        for subject in self.subject_manager.get_subjects():
            print(subject.name)

    def stop_running(self):
        self.running = False
"""
matematica = Subject("Analisis matematico", 1)
tarea_matematica = Task(1, "Hacer ejercicios", "", "", 2)
tarea_matematica2 = Task(2, "Estudiar", "", "", 1)
tarea_matematica3 = Task(3, "Parcial", "", "", 3)
tarea_matematica.mark_done()
tarea_matematica2.mark_done()
matematica.add_task(tarea_matematica)
matematica.add_task(tarea_matematica2)
matematica.add_task(tarea_matematica3)

lengua = Subject("Ingeniería y Sociedad", 1)
tarea_lengua = Task(1, "Hacer poema", "", "", 2)
tarea_lengua2 = Task(2, "Estudiar", "", "", 1)
tarea_lengua3 = Task(3, "Parcial", "", "", 3)
tarea_lengua.mark_done()
tarea_lengua2.mark_done()
tarea_lengua3.mark_done()
lengua.add_task(tarea_lengua)
lengua.add_task(tarea_lengua2)
lengua.add_task(tarea_lengua3)

comunicacion = Subject("Comunicacion de datos", 1)
tarea_comunicacion = Task(1, "Hacer telecomunicacion", "", "", 2)
tarea_comunicacion.mark_done()
comunicacion.add_task(tarea_comunicacion)

disenio = Subject("diseño", 1)
tarea_disenio = Task(1, "Hacer diseño", "", "", 2)
disenio.add_task(tarea_disenio)

ux = Subject("UX/UI", 1)
tarea_ux = Task(1, "Hacer UX/UI", "", "", 2)
tarea_ux2 = Task(2, "Hacer UX/UI", "", "", 2)
tarea_ux2.mark_done()
tarea_ux3 = Task(3, "Hacer UX/UI", "", "", 2)
tarea_ux3.mark_done()
ux.add_task(tarea_ux)
ux.add_task(tarea_ux2)
ux.add_task(tarea_ux3)

subject_manager = Subject_manager([matematica, lengua, comunicacion, disenio, ux])
"""
programa = Program(subject_manager)
programa.main()