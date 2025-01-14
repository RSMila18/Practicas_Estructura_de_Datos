from Clases.inventario import Inventario
from Listas.lista_simple import List
class Solicitud:

    solicitudes = List()

    def __init__(self, empleado = None, tipo = None, estado = "pendiente", numero_placa = None, justificacion = None):
        self._empleado = empleado #Empleado
        self._tipo = tipo
        self._estado = estado
        self._numero_placa = numero_placa
        self._justificacion = justificacion
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
    
    def get_numero_placa(self):
        return self._numero_placa
    
    def set_numero_placa(self, num):
        self._numero_placa = num
        
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
    
    def toFile(self, requests, filename='Solicitudes.txt'):
        full_path = "Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:

            for solicitud in requests:
                archivo.write(str(solicitud) + "\n")
            archivo.close()
            
    def __str__(self):
        #Juan-Perez 24567898 MONITOR_DELL 50245329 23 10 2022 745000
        equipo = Inventario.buscar(self._numero_placa)
        return f'{self._empleado.get_nombre()} {self._empleado.get_id()} {equipo.get_nombre()} {self._numero_placa} {equipo.get_fecha_compra().get_dia()} {equipo.get_fecha_compra().get_mes()} {equipo.get_fecha_compra().get_A()} {equipo.get_valor_compra()}'  