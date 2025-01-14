from datetime import datetime
from Listas.lista_simple import List
from Clases.fecha import Fecha

class ControlCambios:

    registro_cambios = List()

    def __init__(self, id_empleado = None, numero_placa = None, tipo_cambio = None):
        self._id_empleado = id_empleado
        self._numero_placa = numero_placa
        self._tipo_cambio = tipo_cambio
        fecha_actual = Fecha(datetime.now().day, datetime.now().month, datetime.now().year) 
        self._fecha = fecha_actual
        self._hora = datetime.now()
    
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
    def get_hora(self):
        return self._hora    
    def __str__(self):
    
        return f'{self._id_empleado} {self._numero_placa} {self._tipo_cambio} {self._fecha.get_dia()} {self._fecha.get_mes()} {self._fecha.get_A()} {self._hora}'

    def toFile(self, changes, filename='Control_de_cambios.txt'):
        full_path = "Practica_1/Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:

            for cambios in changes:
                archivo.write(str(cambios) + "\n")
            archivo.close()

    def registrar_cambio(self, id_empleado, numero_placa, tipo_cambio):
        
        cambio = ControlCambios(id_empleado, numero_placa, tipo_cambio)
        ControlCambios.registro_cambios.add_Last(cambio)
        print(f"El Cambio ha sido registrado: {cambio}")
        
        cambios_data = []
        current = ControlCambios.registro_cambios.first()
        while current is not None:
            cambios_data.append(str(current.get_Data()))
            current = current.get_Next()
        ControlCambios.toFile(cambios_data)
        print(f"Los cambios han sido guardados con exito")

    #registrar_cambio(id Int, placa Int, tipo String):Boolean