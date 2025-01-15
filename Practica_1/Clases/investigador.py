from Clases.empleado import Empleado
from Clases.inventario import Inventario
from Clases.fecha import Fecha
from Clases.solicitud import Solicitud

class Investigador(Empleado):

    def __str__(self):
        super().__str__()
    
    def solicitar_agregar_equipo(self, empleado):
        while True:
            print("Ingrese los datos del equipo que desee agregar")
            nombre = input("Nombre del equipo: ")
            while True:
                numero_placa = input("Número de placa del equipo: ")
                if numero_placa.isdigit() and len(numero_placa) == 8: 
                    break
                else:
                    print("Número de placa inválido, debe ser de 8 dígitos.") 
            fecha_compra = str(input("Fecha de compra del quipo (DD/MM/AAAA): "))
            linea = fecha_compra.split("/")
            fecha = Fecha(linea[0],linea[1],linea[2])
            valor_compra = int(input("valor de compra de quipo: "))

            equipo = Inventario.buscar(numero_placa)
            if equipo == -1 or equipo.get_fecha_compra() != fecha or equipo.get_valor_compra() != valor_compra:
                print("Los datos del equipo son incorrectos. Ingreselos de nuevo para que su solicitud pueda ser tramitada.")
            
            else:
                solicitud = Solicitud(empleado, "Agregar", equipo)
                empleado.get_solicitudes().add_last(solicitud)
                print(f"Su solicitud quedo tramitada correctamente con los siguientes datos:\n{solicitud}")
                break

    def solicitar_eliminar_equipo(self, empleado):
            while True:
                numero_placa = input("Número de placa del equipo que desea eliminar: ")
                
                equipo = Inventario.buscar(numero_placa)
                if numero_placa.isdigit() and len(numero_placa) == 8 and equipo != -1: 
                    razon = input("Describa resumidamente el por qué desea eliminar este equipo de su inventario: ")
                    Solicitud.set_justificacion(razon)
                    solicitud_eliminar = Solicitud(empleado, "Eliminar", equipo)
                    empleado.get_solicitudes().add_last(solicitud_eliminar)
                    print(f"Su solicitud quedó tramitada correctamente con los siguientes datos:\n{solicitud_eliminar}")

                    break
                else:
                    print("Placa inválida, revise nuevamente.") 

    #consultar_estado_solicitudes(): List<Solicitud>