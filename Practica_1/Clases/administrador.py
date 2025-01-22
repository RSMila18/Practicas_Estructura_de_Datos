from Clases.control_cambios import ControlCambios
from Clases.empleado import Empleado
from Clases.fecha import Fecha
from Listas.doble_node import DoubleNode
from Clases.solicitud import Solicitud
from Listas.lista_simple import List
from Clases.direccion import Direccion

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
        direccion = Direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
        password = input("Ingrese una contraseña: ")
        descripcion = input("Ingrese el rol del empleado: ")
        
        empleado = Empleado(nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion, password, descripcion)
        Empleado.empleados.add_last(empleado)
        
        empleados_actua = []
        current = Empleado.empleados.first()
        while current is not None:
            empleados_actua.append(str(current.get_Data()))
            current= current.get_Next()
        Empleado.toFile(empleados_actua, "Empleados.txt")
        Empleado.toFile_password(empleado.get_password, "Password.txt")
    
    
    @classmethod
    def eliminar_usuario(cls,  identificacion):
        print(f"Intentando eliminar el usuario con ID: {identificacion}")
        identificacion = int(identificacion)
        nodo = Empleado.buscar(identificacion) #nodo = Empleado | -1(Int)
        found = False

        if nodo is not None and nodo != -1:
            print(f"Verificando empleado: {nodo.get_id()}")
            if nodo.get_id() ==  identificacion: 
                found = Empleado.eliminar(nodo)
        if found:
            print("Usuario eliminado exitosamente.")
            empleados_actua = []
            current = super().empleados.first()
            while current is not None:
                empleados_actua.append(str(current.get_Data()))
                current = current.get_Next()
            Empleado.toFile(empleados_actua, "Empleados.txt")  

            conrtra_ac = []
            current = super().empleados.first()
            while current is not None:
                conrtra_ac.append(str(current.get_Data().get_password()))
                current = current.get_Next()
            Empleado.toFile_password(conrtra_ac, "Password.txt")

        else:
            print("Usuario no encontrado.")
    @classmethod        
    def cambiar_contraseña(self):
        identificacion = input("Ingrese la identificación del empleado: ")
        current = super().empleados.first()
        while current is not None:
            empleado = current.get_Data()
            #if empleado.identificacion == identificacion:
            if empleado.get_id() == int(identificacion):
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                empleado.set_password(nueva_contraseña)  

                conrtra_ac = []
                current = super().empleados.first()
                while current is not None:
                    conrtra_ac.append(str(current.get_Data().get_password()))
                    current = current.get_Next()
                Empleado.toFile_password(conrtra_ac, "Password.txt")

                print("Contraseña actualizada exitosamente.")
                return
            current = current.get_Next()  
        print("Empleado no encontrado.")

    def eliminar_de_lista(lista, nodo_a_eliminar):
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
    @classmethod   
    def responder_solicitudes(self):
        changes = []
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

            decision = input("¿ 1. Aprobar o 2. Rechazar? ")
            decision = int(decision)

            eq = solicitud.get_equipo()
            emp = solicitud.get_empleado()
            if decision == 1:
                if solicitud.get_tipo() == "Agregar":
                    from Clases.equipo import Equipo
                    if Equipo.buscar(int(eq.get_numero_placa())) != None:
                        if eq.get_empleado().get_nombre() != solicitud.get_empleado().get_nombre():
                            print("No se puede Aprobar esta solicitud porque el equipo esta asociado a otro empleado.")
                            continue
                        else:
                            eq.set_empleado(emp)
                            solicitud.aprobar_solicitud()
                            
                            emp.agregar_inventario(eq)
                            print("Solicitud Aprobada con exito.")
                            solicitud.get_cambios()
                            ControlCambios.registrar_cambio(solicitud.get_empleado().get_id(), solicitud.get_equipo().get_numero_placa(), solicitud.get_tipo(), "aprobada")
                    else:
                        print("El numero de placa no existe.")
                        continue
                elif solicitud.get_tipo() == "Editar":
                    if Equipo.buscar(int(eq.get_numero_placa())) != None:
                        if eq.get_empleado().get_nombre() != solicitud.get_empleado().get_nombre():
                            print("No se puede Aprobar esta solicitud porque el equipo esta asociado a otro empleado.")
                            continue
                        else:
                            temp = emp.get_inventario().first() #primer equipo inventario
                            
                            while temp is not None:
                                if temp.get_Data() == eq:
                                    emp.get_inventario().remove(temp)
                                    eq.set_empleado(None)
                                    break
                                temp = temp.get_Next()
                             
                            solicitud.aprobar_solicitud()
                            solicitud.get_cambios()
                            ControlCambios.registrar_cambio(solicitud.get_empleado().get_id(), solicitud.get_equipo().get_numero_placa(), solicitud.get_tipo(), "aprobada")
                            print("Solicitud Aprobada con exito.")
                    else:
                        print("El numero de placa no existe.")
                        continue
                
                else:
                    print("El tipo de la solicitud es invalido.")
                    continue

            elif decision == 2:
                solicitud.rechazar_solicitud()
                solicitud.get_cambios()
                ControlCambios.registrar_cambio(solicitud.get_empleado().get_id(), solicitud.get_equipo().get_numero_placa(), solicitud.get_tipo(), "rechazado")
                
                #(self, id_empleado = None, numero_placa = None, tipo_cambio = None)
                print("Solicitud Rechazada con exito.")
            else:
                print("Decisión inválida. Saltando a la siguiente solicitud.")
                current = current.get_Next()
                continue
            
            if solicitud.get_estado()== "Pendiente":
                if solicitud.get_tipo()== "Agregar":
                    solicitudes_agregar.add_Last(str(solicitud))
                elif solicitud.get_tipo()== "Editar":
                    solicitudes_eliminar.add_Last(str(solicitud))
                    
                    
            siguiente = current.get_Next()
            if solicitud.get_estado() != "Pendiente":
                self.eliminar_de_lista(Solicitud.solicitudes, current)
            current = siguiente

        solicitudes_data = []
        current = solicitudes_agregar.first()
        while current is not None:
            solicitudes_data.append(str(current.get_data()))
            current= current.get_Next()
            Solicitud.toFil_()
        Solicitud.toFile(solicitudes_data, "Solicitudes_agregar.txt")

        
        solicitudes_data_eliminar = []
        current = solicitudes_eliminar.first()
        while current is not None:
            solicitudes_data_eliminar.append(str(current.get_data()))
            current= current.get_Next()
            Solicitud.toFil_()
        Solicitud.toFile(solicitudes_data, "Solicitudes_eliminar.txt")

        Solicitud.toFil_()