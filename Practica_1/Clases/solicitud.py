from Clases.empleado import Empleado
from Listas.lista_simple import List
class Solicitud:

    solicitudes = List()

    def __init__(self, empleado = None, tipo = None, equipo = None):
        self._empleado = empleado #Empleado
        self._tipo = tipo
        self._estado = "Pendiente"
        self._equipo = equipo
        self._justificacion = " "
        Solicitud.solicitudes.add_Last(self)
    
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
    
    def agregar(ident, s):
        if Empleado.buscar(ident) != -1:
                print("Empleado no existe")
        else:
            Solicitud.solicitudes.add_last(s)
            print("Solicitud agregada con exito")
    
    def toFile(requests, filename='Solicitudes.txt'):
        full_path = "Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:

            for solicitud in requests:
                archivo.write(str(solicitud) + "\n")
            archivo.close()

    def import_solicitud(type_,filename="Empleados.txt"):
        ruta = "Datos/" + filename
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()  # Eliminar saltos de línea o espacios extra
                new_linea = linea.split(" ")
                #Juan-Perez 24567898 MONITOR_DELL 50245329 23 10 2022 745000 (7)
                #(self, empleado = None, tipo = None._equipo = None):
                employee = Empleado.buscar(new_linea[1])
                new_requests = Solicitud(employee, type_, new_linea[3])
                Solicitud.agregar(new_requests)
            archivo.close()
            
    def __str__(self):
        #Juan-Perez 24567898 MONITOR_DELL 50245329 23 10 2022 745000
        return f'{self._empleado.get_nombre()} {self._empleado.get_id()} {self._equipo.get_nombre()} {self._equipo.get_numero_placa()} {self._equipo.get_fecha_compra().get_dia()} {self._equipo.get_fecha_compra().get_mes()} {self._equipo.get_fecha_compra().get_A()} {self._equipo.get_valor_compra()}'  