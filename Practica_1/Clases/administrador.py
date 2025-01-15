from Clases.inventario import Inventario
from Clases.empleado import Empleado
from Clases.fecha import Fecha
from Listas.doble_node import DoubleNode
from Clases.solicitud import Solicitud
from Listas.lista_simple import List

class Administrador(Empleado):

    def __init__(self, nombre = None, identificacion = None, fecha_nacimiento = None, ciudad_nacimiento = None, telefono = None, email = None, direccion = None, password = None, descripcion = "administrador"):
        super().__init__(nombre,identificacion,fecha_nacimiento,ciudad_nacimiento,telefono,email,direccion,password,descripcion)
    
    def __str__(self):
        super().__str__()
    
    def crear_usuario():
        nombre = input("Nombre: ")
        identificacion = int(input("Número de Identificación: "))
        fecha_ = input("Fecha de Nacimiento (dd/mm/aaaa): ")
        dia, mes, anio = fecha_.split('/')
        fecha_nacimiento = Fecha(dia, mes, anio)
        ciudad_nacimiento = input("Ciudad de Nacimiento: ")
        telefono = int(input("Teléfono: "))
        email = input("Correo Electrónico: ")
        print("Ingrese dirección de vivienda")
        calle = input("Calle: ")
        nomenclatura = input("Nomenclatura: ")
        barrio = input("Barrio: ")
        ciudad = input("Ciudad: ")
        edificio = input("Urbanización: ")
        apto = input("Apartamento: ")
        direccion = (calle, nomenclatura, barrio, ciudad, edificio, apto)
        password = input("Ingrese una contraseña: ")
        descripcion = input("Ingrese el rol del empleado: ")
        
        empleado = Empleado(nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion, password, descripcion)
        super().empleados.add_last(empleado)
    
    def eliminar_usuario(self, identificacion_):
        identificacion_ = input("Ingrese la identificación del usuario a eliminar: ")

        current = super().empleados.first() 
        found = False
        while current is not None:
            empleado = current.get_Data()
            if empleado.identificacion == identificacion_: 
                super().empleados.remove(current)  
                found = True
                break
            current = current.get_Next()
        if found:
            self._password.pop(identificacion_, None) 
            print("Usuario eliminado exitosamente.")
        else:
            print("Usuario no encontrado.")
            
    def cambiar_contraseña(self):
        identificacion = input("Ingrese la identificación del empleado: ")
        current = super().empleados.first()
        while current is not None:
            empleado = current.get_Data()
            if empleado.identificacion == identificacion:
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                empleado.set_password(nueva_contraseña)  
                print("Contraseña actualizada exitosamente.")
                return
            current = current.get_Next()  
        print("Empleado no encontrado.")
               
    def eliminar_de_lista(self, lista, nodo_a_eliminar):
        current = lista.first()
        previous = None
        while current is not None:
            if current == nodo_a_eliminar:
                if previous is None:
                    lista.remove_First()
                else:
                    previous.set_Next(current.get_Next())
                    lista.set_Size(lista.size() - 1)
                return
            previous = current
            current = current.get_Next()
        
    def responder_solicitudes(self):
        current = Solicitud.solicitudes.first()
        if current is None:
            print("No hay solicitudes pendientes para gestionar.")
        
        solicitudes_agregar = List()
        solicitudes_eliminar = List()
        
        while current is not None:
            solicitud = current.get_Data() 
            print("\n--- Solicitud ---")
            print(f"Empleado: {solicitud.get_empleado().get_nombre()}")
            print(f"ID: {solicitud.get_empleado().get_id()}")
            print(f"Tipo: {solicitud.get_tipo()}")
            print(f"Estado: {solicitud.get_estado()}")
            print(f"Nombre del Equipo: {solicitud.get_equipo().get_nombre()}")
            print(f"Placa del Equipo: {solicitud.get_equipo().get_numero_placa()}")
            print(f"Fecha de Compra: {solicitud.get_equipo().get_fecha_compra()}")
            print(f"Valor de Compra: {solicitud.get_equipo().get_valor_compra()}")
            print(f"Justificación: {solicitud.get_justificacion()}")

            decision = input("¿Aprobar o Rechazar? ").strip().upper()

            eq = Inventario.buscar(solicitud.get_numero_placa())
            emp = solicitud.get_empleado()
            if decision == "Aprobar":
                if solicitud.get_tipo() == "Agregar":
                    if eq != -1:
                        if eq.get_empleado().get_nombre() != None:
                            print("No se puede Aprobar esta solicitud porque el equipo esta asociado a otro empleado.")
                            continue
                        else:
                            eq.set_empleado(emp)
                            solicitud.aprobar_solicitud()
                            print("Solicitud Aprobada con exito.")
                    else:
                        print("El numero de placa no existe.")
                        continue
                elif solicitud.get_tipo() == "Eliminar":
                    if eq != -1:
                        if eq.get_empleado().get_nombre() != solicitud.get_empleado().get_nombre():
                            print("No se puede Aprobar esta solicitud porque el equipo esta asociado a otro empleado.")
                            continue
                        else:
                            node = DoubleNode(eq)
                            emp.get_inventario().remove(node) #Eliminar el equipo del inventario
                            eq.set_empleado(None) #Desasociar el equipo del empleado
                            solicitud.aprobar_solicitud()
                            print("Solicitud Aprobada con exito.")
                    else:
                        print("El numero de placa no existe.")
                        continue
                
                else:
                    print("El tipo de la solicitud es invalido.")
                    continue

            elif decision == "Rechazar":
                solicitud.rechazar_solicitud()
                print("Solicitud Rechazada con exito.")
            else:
                print("Decisión inválida. Saltando a la siguiente solicitud.")
                current = current.get_Next()
                continue
            
            if Solicitud.get_estado(self)== "Pendiente":
                if solicitud.get_tipo()== "Agregar":
                    solicitudes_agregar.add_Last(str(solicitud))
                elif solicitud.get_tipo()== "Eliminar":
                    solicitudes_eliminar.add_Last(str(solicitud))
                    
                    
            siguiente = current.get_Next()
            self.eliminar_de_lista(solicitud.solicitudes, current)
            current = siguiente
        
        solicitudes_data = []
        current = solicitudes_agregar.first()
        while current is not None:
            solicitudes_data.append(str(current.get_data()))
            current= current.get_Next()
        Solicitud.toFile(solicitudes_data, "Solicitudes_agregar.txt")
#        guardar_datos("Solicitudes_agregar.txt", solicitudes_data)
        
        solicitudes_data_eliminar = []
        current = solicitudes_eliminar.first()
        while current is not None:
            solicitudes_data_eliminar.append(str(current.get_data()))
            current= current.get_Next()
        Solicitud.toFile(solicitudes_data, "Solicitudes_eliminar.txt")
#        guardar_datos("Solicitudes_eliminar.txt", solicitudes_data)

    #crear_usuario( usuario Usuario): Boolean
    #eliminar_usuario( id Int): Boolean
    #cambiar_contraseña( id Int, csñ String): Boolean
    #responder_solicitud(id_s Int, action String): Boolean