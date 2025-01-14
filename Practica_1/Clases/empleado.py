from Clases.usuario import Usuario
from Listas.doble_list import DoubleList
from Listas.doble_node import DoubleNode
from Clases.fecha import Fecha
from Clases.direccion import Direccion

class Empleado(Usuario):

    empleados = DoubleList()

    def __init__(self, nombre = None, identificacion = None, fecha_nacimiento = None, ciudad_nacimiento = None, telefono = None, email = None, direccion = None, password = None, descripcion = None):
        super().__init__(nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion)
        self._password = password
        self._descripcion = descripcion
        

    def get_password(self):
        return self._password
    def set_password(self, csñ):
        self._password = csñ
    def get_descripcion(self):
        return self._descripcion
    def set_descripcion(self, tipo):
        self._descripcion = tipo

    def __str__(self):
        base_str = super().__str__()
        return f'{base_str},{self._password},{self._descripcion}'
    
    def buscar(self, identificacion):
        current = Empleado.empleados.first()
        for _ in range(Empleado.empleados.size(),1):
            if identificacion == current.get_Data().get_id():
                return current
            else:
                current = current.get_Next()       
        return -1

    def agregar(self, e):
        if self.buscar(e.get_id()) != -1:
                return False
        else:
            N = Empleado.empleados.last()
            new = DoubleNode(e)
            N.set_Next() = new
            new.set_Prev() = N
            
            return True
    
    def toFile(self, filename='Empleados.txt'):
        full_path = "Practica_1/Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:
            employees = []
            current = Empleado.empleados._head
            for _ in range(Empleado.empleados.size(),1):
                employees.append(current)
                current = current.get_Next().get_Data()

            for empleado in employees:
                archivo.write(str(empleado) + "\n")
            archivo.close()

    
    def import_Data(self, filename="Empleados.txt"):
        ruta = "Practica_1/Datos/" + filename
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()  # Eliminar saltos de línea o espacios extra
                new_linea = linea.split(",")
                fecha = new_linea[2].split("-")
                new_fecha = Fecha(fecha[0], fecha[1], fecha[2])
                new_direccion = Direccion(new_linea[6], new_linea[7], new_linea[8], new_linea[9], new_linea[10], new_linea[11])
                new_employees = Empleado(new_linea[0], int(new_linea[1]), new_fecha, new_linea[3], int(new_linea[4]), new_linea[5], new_direccion, new_linea[12], new_linea[13])
                self.agregar(new_employees)
            archivo.close()


    def ingresar_sistema(self, identificacion, password):
        if str(self._id) == str(identificacion) and self._password == password:
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Identificación y/o contraseña incorrecta.")
            return False

    #ingresar_sistema(id Int, password String): Bolean
    #consultar_inventario(): List<Equipo>
    