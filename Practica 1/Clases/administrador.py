from Clases.empleado import Empleado
from Clases.fecha import Fecha
from Listas.doble_list import DoubleList
from Clases.solicitud import Solicitud

class Administrador(Empleado):
    
    def crear_usuario(self, nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion, password, descripcion):
        super().__init__(nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion, password, descripcion)
        self.coleccion_empleados = DoubleList()
        
        nombre = input("Nombre: ")
        identificacion = int(input("Número de Identificación: "))
        fecha_ = input("Fecha de Nacimiento (dd/mm/aaaa): ")
        dia, mes, anio = fecha_.split('/')
        fecha_nacimiento = Fecha(dia, mes, anio)
        ciudad_nacimiento = input("Ciudad de Nacimiento: ")
        telefono = int(input("Teléfono: "))
        correo = input("Correo Electrónico: ")
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
        
        empleado = Empleado(nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion, password, descripcion)
        self.coleccion_empleados.add_last(empleado)
        
#Esto está gregando y asociando la id con la contraseña y rol, para lo del inicio de sesión y el reconocimiento del rol
#De igual modo esto es para lo de Password.txt
        self._password[identificacion] = (password, descripcion)
        print(f"El usuario del empleado {nombre} fue correctamente creado y agregado a la base de datos")
    
    def eliminar_usuario(self, identificacion_):
        identificacion_ = input("Ingrese la identificación del usuario a eliminar: ")

        current = self.coleccion_empleados.first() 
        found = False
        while current is not None:
            empleado = current.get_Data()
            if empleado.identificacion == identificacion_: 
                self.coleccion_empleados.remove(current)  
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
        current = self.coleccion_empleados.first()
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
            return
        while current is not None:
            solicitud = current.get_Data() 
            print("\n--- Solicitud ---")
            print(f"ID: {solicitud.get_id_solicitud()}")
            print(f"Tipo: {solicitud.get_tipo()}")
            print(f"Estado: {solicitud.get_estado()}")
            print(f"Placa del Equipo: {solicitud.get_numero_placa()}")
            print(f"Justificación: {solicitud.get_justificacion()}")
            print(f"Fecha y Hora: {solicitud.get_fecha_hora()}")

            decision = input("¿Aprobar (A) o Rechazar (R)? ").strip().upper()

            if decision == "A":
                print(solicitud.aprobar_solicitud())

            elif decision == "R":
                print(solicitud.rechazar_solicitud())
            else:
                print("Decisión inválida. Saltando a la siguiente solicitud.")
                current = current.get_Next()
                continue

            siguiente = current.get_Next()
            self.eliminar_de_lista(Solicitud.solicitudes, current)
            current = siguiente 
        print("Todas las solicitudes pendientes han sido gestionadas.")



    #crear_usuario( usuario Usuario): Boolean
    #eliminar_usuario( id Int): Boolean
    #cambiar_contraseña( id Int, csñ String): Boolean
    #responder_solicitud(id_s Int, action String): Boolean