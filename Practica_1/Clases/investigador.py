from Clases.empleado import Empleado
from Clases.inventario import Inventario
from Clases.fecha import Fecha
from Clases.solicitud import Solicitud
from Clases.equipo import Equipo

class Investigador(Empleado):

    def __init__(self, nombre = None, identificacion = None, fecha_nacimiento = None, ciudad_nacimiento = None, telefono = None, email = None, direccion = None, password = None, descripcion = "investigador"):
        super().__init__(nombre,identificacion,fecha_nacimiento,ciudad_nacimiento,telefono,email,direccion,password,descripcion)
    
    def __str__(self):
        super().__str__()
    
    def solicitar_agregar_equipo(empleado):
        while True:
            print("Ingrese los datos del equipo que desee agregar")
            nombre = input(str("Nombre del equipo: "))
            while True:
                numero_placa = (input("Número de placa del equipo: "))
                if len(numero_placa) == 8: 
                    break
                else:
                    print("Número de placa inválido, debe ser de 8 dígitos.") 
            fecha_compra = str(input("Fecha de compra del quipo (DD/MM/AAAA): "))
            linea = fecha_compra.split("/")
            fecha = Fecha(linea[0],linea[1],linea[2])
            valor_compra = int(input("valor de compra de quipo: "))
            
            equipo = Equipo(nombre, numero_placa, fecha, valor_compra)
            solicitud = Solicitud(empleado, "Agregar", equipo)
            empleado.get_solicitudes().add_last(solicitud)
            print(f"Su solicitud quedó tramitada correctamente con los siguientes datos:\n{solicitud}")
            Solicitud.toFile_1(solicitud, "Solicitudes_agregar.txt")
            break

    def solicitar_eliminar_equipo(empleado):
            while True:
                numero_placa = input("Número de placa del equipo que desea eliminar: ")
                
                equipo = Inventario.buscar(numero_placa)
                if numero_placa.isdigit() and len(numero_placa) == 8 and equipo != -1: 
                    razon = input("Describa resumidamente el por qué desea eliminar este equipo de su inventario: ")
                    solicitud_eliminar = Solicitud(empleado, "Eliminar", equipo)
                    empleado.get_solicitudes().add_last(solicitud_eliminar)
                    solicitud_eliminar.set_justificacion(razon)
                    print(f"Su solicitud quedó tramitada correctamente con los siguientes datos:\n{solicitud_eliminar}")
                    Solicitud.toFile_1(solicitud_eliminar, "Solicitudes_editar.txt")
                    break
                else:
                    print("Placa inválida, revise nuevamente.") 
    
    @classmethod
    def consultar_estado_solicitudes(cls, empleado):
        from Clases.control_cambios import ControlCambios
        L = ControlCambios.buscar_por_id(int(empleado.get_id()))
        
        for linea in L:
                cambio = linea.split(" ")
                #34568910 50109773 Editar 22 1 2025 2025-01-22 12:49:25.158712 rechazado
                #   0         1       2   3   4 5       6               7          8
                print(f"Estado de su solicitud del tipo ({cambio[2]}), asociado al equipo con numero de placa: {cambio[1]} fue ==> {cambio[8]}")


        

    def descarga(e):
        D = e.get_inventario()
        c = []
        current = D.first()
        for _ in range(D.size()):
            c.append(current.get_Data())
            current = current.get_Next()
            filename = str(e.get_nombre()) + " " + str(e.get_id())
            Solicitud.toFile(c, filename)










































        
        