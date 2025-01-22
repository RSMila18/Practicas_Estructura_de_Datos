import os
from datetime import datetime
from Listas.lista_simple import List
from Clases.fecha import Fecha

class ControlCambios:

    registro_cambios = List()

    def __init__(self, id_empleado = None, numero_placa = None, tipo_cambio = None, razon = None):
        self._id_empleado = id_empleado
        self._numero_placa = numero_placa
        self._tipo_cambio = tipo_cambio
        fecha_actual = Fecha(datetime.now().day, datetime.now().month, datetime.now().year) 
        self._fecha = fecha_actual
        self._hora = datetime.now()
        self._razon = razon
    
    def get_list():
        return ControlCambios.registrar_cambio
    def get_razon(self):
        return self._razon
    def set_razon(self, razon):
        self._razon = razon
    def get_id_empleado(self):
        return self._id_empleado
    def set_id_empleado(self, ide):
        self._id_empleado = ide
    def get_numero_placa(self):
        return self._numero_placa
    def set_numero_placa(self, num):
        self._numero_placa = num
    def get_tipo_cambio(self):
        return self._tipo_cambio
    def set_tipo_cambio(self, tipo):
        self._tipo_cambio = tipo
    def get_fecha(self):
        return self._fecha
    def set_fecha(self,fecha):
        self._fecha = fecha
    def get_hora(self):
        return self._hora    
    def __str__(self):
    
        return f'{self._id_empleado} {self._numero_placa} {self._tipo_cambio} {self._fecha.get_dia()} {self._fecha.get_mes()} {self._fecha.get_A()} {self._hora} {self._razon}'

    def toFile(changes, filename='Control_de_cambios.txt'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, "Datos", filename)
        #full_path = "Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:
            for cambios in changes:
                archivo.write(str(cambios) + "\n")
            archivo.close()

    def registrar_cambio(id_empleado, numero_placa, tipo_cambio, razon):
        
        cambio = ControlCambios(id_empleado, numero_placa, tipo_cambio, razon)
        ControlCambios.registro_cambios.add_Last(cambio)
        print(f"El Cambio ha sido registrado: {cambio}")
        
        cambios_data = []
        current = ControlCambios.registro_cambios.first()
        while current is not None:
            cambios_data.append(str(current.get_Data()))
            current = current.get_Next()
        ControlCambios.toFile(cambios_data)
        print(f"Los cambios han sido guardados con exito")

    def import_control(filename="Control_de_cambios.txt"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(current_dir, "Datos", filename)
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()  
                new_linea = linea.split(" ")
                #34568910 50109774 Editar 16 1 2025 2025-01-16 14:54:37.019185 8
                #0          1       2       345       6          7
                S = ControlCambios.get_list()
                N = ControlCambios(new_linea[0], new_linea[1], new_linea[2], new_linea[8])
                F = new_linea[6].split("-")
                N.set_fecha(Fecha(F[0],F[1],F[2]))
                #print(f"Empleado: {new_employees} \n")
            archivo.close()