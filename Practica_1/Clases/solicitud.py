from Clases.empleado import Empleado
from Clases.equipo import Equipo
from Listas.lista_simple import List
import os
class Solicitud:

    solicitudes = List()

    def __init__(self, empleado = None, tipo = None, equipo = None):
        self._empleado = empleado #Empleado
        self._tipo = tipo
        self._estado = "Pendiente"
        self._equipo = equipo
        self._justificacion = " "
    
    def get_empleado(self):
        return self._empleado
    def set_empleado(self, ide):
        self._empleado = ide
    def get_tipo(self):
        return self._tipo
    def set_tipo(self, tipo):
        self._tipo = tipo
    def get_estado(self):
        return self._estado
    def get_equipo(self):
        return self._equipo
    def set_equipo(self, num):
        self._equipo = num
    def get_justificacion(self):
        return self._justificacion
    def set_justificacion(self, razon):
        self._justificacion = razon
    def get_solicitudes(self):
        return Solicitud.solicitudes
    def aprobar_solicitud(self):
        self._estado = "aprobada"
    def rechazar_solicitud(self):
        self._estado = "rechazada"

    def buscar_solicitud(type_):
        D = Solicitud.solicitudes
        if D.is_Empty():
            print("No hay solicitudes.")
        else:
            print(f"Estas son las Solicitudes de {str(type_)}:\n")
            current = D.first()
            for _ in range(D.size()):
                if current.get_Data().get_tipo() == str(type_):
                    print(current.get_Data())
                    current = current.get_Next()
    
    def agregar(ident, s):
        if ident == '' or Empleado.buscar(ident) == -1:
                print("Empleado no existe")
        else:
            Solicitud.solicitudes.add_Last(s)
            print("Solicitud agregada con exito")
            
    
    def toFile(requests, filename='Solicitudes.txt'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, "Datos", filename)
        #full_path = "Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:

            for solicitud in requests:
                archivo.write(str(solicitud) + "\n")
            archivo.close()

    def import_solicitud(type_, filename="Solicitudes.txt"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(current_dir, "Datos", filename)
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                new_linea = linea.split(" ")
                if len(new_linea) == 7:
                    employee = Empleado.buscar(int(2345934))
                    product = Equipo.buscar(new_linea[2])
                elif len(new_linea) < 7:
                    employee = None
                    product = None
                    
                #Diego-Palacio 34568910 CAMARA_MONOCROMATICA 50109773 9 12 2021 1786000
                #def __init__(self, empleado = None, tipo = None, equipo = None)
                else:
                    employee = Empleado.buscar(int(new_linea[1]))
                    product = Equipo.buscar(new_linea[3])
                new_requests = Solicitud(employee, type_, product)
                if employee != None:
                    employee.agregar_solicitud(new_requests)
                    Solicitud.agregar(int(employee.get_id()), new_requests)
            archivo.close()
            
    def __str__(self):
        #Juan-Perez 24567898 MONITOR_DELL 50245329 23 10 2022 745000
        if self._empleado == None and self._equipo == None:
            return None
        return f'{self._empleado.get_nombre()} {self._empleado.get_id()} {self._equipo.get_nombre()} {self._equipo.get_numero_placa()} {self._equipo.get_fecha_compra().get_dia()} {self._equipo.get_fecha_compra().get_mes()} {self._equipo.get_fecha_compra().get_A()} {self._equipo.get_valor_compra()}'  