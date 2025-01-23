import os
from Clases.usuario import Usuario
from Listas.doble_list import DoubleList
from Clases.fecha import Fecha
from Clases.direccion import Direccion


class Empleado(Usuario):

    empleados = DoubleList()

    def __init__(self, nombre = None, identificacion = None, fecha_nacimiento = None, ciudad_nacimiento = None, telefono = None, email = None, direccion = None, password = None, descripcion = None):
        super().__init__(nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion)
        self._password = password
        self._descripcion = descripcion
        self._inventario = DoubleList()
        self._solicitudes = DoubleList()
        self.Data = None
    
    def agregar_inventario(self,e):
        self._inventario.add_last(e)
    def agregar_solicitud(self,s):
        self._solicitudes.add_last(s)
    def get_id(self):
        return super().get_id()    
    def get_inventario(self):
        return self._inventario
    def get_solicitudes(self):
        return self._solicitudes
    def get_password(self):
        return self._password
    def set_password(self, csñ):
        self._password = csñ
    def get_descripcion(self):
        return self._descripcion
    def set_descripcion(self, tipo):
        self._descripcion = tipo
    def get_Data(self):
        return self.Data

    def __str__(self):
        return f'{self._nombre} {self._id} {self._fecha_nacimiento.get_dia()} {self._fecha_nacimiento.get_mes()} {self._fecha_nacimiento.get_A()} {self._ciudad_nacimiento} {self._tel} {self._email} {self._dir.get_calle()} {self._dir.get_nomenclatura()} {self._dir.get_barrio()} {self._dir.get_ciudad()} {self._dir.get_edificio()} {self._dir.get_apto()}'
    
    @classmethod
    def buscar(cls, identificacion):
        if Empleado.empleados.is_Empty():
            return None
        current = Empleado.empleados.first()
        for _ in range(Empleado.empleados.size()):
            
            if identificacion == current.get_Data().get_id():
                return current.get_Data()
                
            else:
                current = current.get_Next()       
    @classmethod
    def agregar(cls, e):
        if cls.buscar(e.get_id()) != None:
                return False
        else:
            Empleado.empleados.add_last(e)
            return True
        
    @classmethod
    def eliminar(cls, Objeto):
        temp = cls.empleados.first()

        if temp is None:  # Si la lista está vacía
            return False

        if Objeto == temp.get_Data():  # Si el objeto es el primer nodo
            return cls.empleados.remove_first()

        while temp is not None:
            if temp.get_Data() == Objeto:  # Encuentra el nodo a eliminar
                anterior = temp.get_Prev()
                siguiente = temp.get_Next()

                if siguiente is None:  # Si es el último nodo
                    anterior.set_Next(None)
                else:  # Si no es el último nodo
                    anterior.set_Next(siguiente)
                    siguiente.set_Prev(anterior)

                temp.set_Prev(None)
                temp.set_Next(None)
                print(f"Nodo eliminado: {temp.get_Data()}")
                return True

            temp = temp.get_Next()

        print("Objeto no encontrado en la lista.")
        return False
    
    def eliminar_equipo(self, Objeto):
        temp = self._inventario.first()

        if temp is None:  # Si la lista está vacía
            return False

        if Objeto == temp.get_Data():  # Si el objeto es el primer nodo
            return self._inventario.remove_first()

        while temp is not None:
            if temp.get_Data() == Objeto:  # Encuentra el nodo a eliminar
                anterior = temp.get_Prev()
                siguiente = temp.get_Next()

                if siguiente is None:  # Si es el último nodo
                    anterior.set_Next(None)
                else:  # Si no es el último nodo
                    anterior.set_Next(siguiente)
                    siguiente.set_Prev(anterior)

                temp.set_Prev(None)
                temp.set_Next(None)
                print(f"Nodo eliminado: {temp.get_Data()}")
                return True

            temp = temp.get_Next()

        print("Objeto no encontrado en la lista.")
        return False
            

    def toFile(empleados, filename='Empleados.txt'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, "Datos", filename)
        with open(full_path, "w", encoding="utf-8") as archivo:
            current = Empleado.empleados.first()
            while current is not None:
                empleado = current.get_Data()
                archivo.write(str(empleado) + "\n") 
                current = current.get_Next()

    @staticmethod
    def import_empleados(filename="Empleados.txt"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(current_dir, "Datos", filename)
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()  
                new_linea = linea.split(" ")
                new_fecha = Fecha(new_linea[2], new_linea[3], new_linea[4])
                new_direccion = Direccion(new_linea[8], new_linea[9], new_linea[10], new_linea[11], new_linea[12], new_linea[13])
                new_employees = Empleado(new_linea[0], int(new_linea[1]), new_fecha, new_linea[5], int(new_linea[6]), new_linea[7], new_direccion)
                Empleado.agregar(new_employees)
                #print(f"Empleado: {new_employees} \n")
            archivo.close()

    @staticmethod
    def import_password(filename="Password.txt"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(current_dir, "Datos", filename)
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()  
                new_linea = linea.split(" ")
                employee = Empleado.buscar(int(new_linea[0]))
                if employee != None:
                    employee.set_password(new_linea[1])
                    employee.set_descripcion(new_linea[2])
                    #print(f"ID: {employee.get_id()} Contraseña: {employee.get_password()} Descripción: {employee.get_descripcion()} \n")
                else:
                    print(f"El empleado de cedula: {new_linea[0]}, no se encuentra en el registro \n")
            archivo.close()

    def toFile_password(_password, filename='Password.txt'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, "Datos", filename)
        with open(full_path, "w", encoding="utf-8") as archivo:
            current = Empleado.empleados.first()
            while current is not None:
                empleado = current.get_Data()
                archivo.write(f"{empleado.get_id()} {empleado.get_password()} {empleado.get_descripcion()}\n")
                current = current.get_Next()
                    
    @staticmethod
    def consultar_inventario_E(e):
        from Clases.equipo import Equipo
        if e.get_descripcion() == "administrador":
            print("\n--- Consultar Inventario ---")
            print("1. Inventario General")
            print("2. Invertario Especifico")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                Equipo.consultar_inventario()
            elif opcion == "2":
                ident = input("Ingrese la identificación(cédula) del empleado al que le desea ver el inventario: ")
                user = Empleado.buscar(int(ident))
                if user == None:
                    print("Empleado no encontrado.")
                else:
                    print(f"Inventario del empleado: {user.get_nombre()}")
                    L = user.get_inventario()
                    if L.is_Empty():
                        print("El inventario del empleado se encuentra vacio.")
                    else:
                        current = L.first()
                        if current is not None: 
                            for _ in range(L.size()):
                                print(current.get_Data())
                                current = current.get_Next() 
            else:
                print("Opción no válida.")

        if e.get_descripcion() == "investigador":
            D = e.get_inventario()
            if D.is_Empty():
                print("El inventario del empleado se encuentra vacio.")
            else:
                print("Este es su inventario:\n")
                current = D.first()
                for _ in range(D.size()):
                    if current is not None:
                        print(current.get_Data())
                        current = current.get_Next()