from datetime import datetime
from Listas.lista_simple import List
from Clases.fecha import Fecha
from Funcionalidades.persistencia import guardar_datos

class ControlCambios:

    registro_cambios = List()

    def __init__(self, id_empleado = None, numero_placa = None, tipo_cambio = None, fecha = None):
        self._id_empleado = id_empleado
        self._numero_placa = numero_placa
        self._tipo_cambio = tipo_cambio
        self._fecha = fecha
        self.fecha_hora = datetime.now()
    
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
    def set_fecha (self, fecha):
        self._fecha = fecha
    def get_fecha_hora(self):
        return self.fecha_hora    
    def __str__(self):
        return f'{self._id_empleado},{self._numero_placa},{self._tipo_cambio},{self._fecha},{self.fecha_hora}'

    def registrar_cambio(self, id_empleado, numero_placa, tipo_cambio, fecha, archivo="Control_de_Cambios.txt"):
        
        fecha_actual = Fecha(datetime.now().day, datetime.now().month, datetime.now().year)
        cambio = ControlCambios(
            id_empleado=id_empleado,
            numero_placa=numero_placa,
            tipo_cambio=tipo_cambio,
            fecha= fecha_actual)
        
        ControlCambios.registro_cambios.add_Last(cambio)
        print(f"El Cambio ha sido registrado: {cambio}")
        
        cambios_data = []
        current = ControlCambios.registro_cambios.first()
        while current is not None:
            cambios_data.append(str(current.get_Data()))
            current = current.get_Next()
        guardar_datos(archivo, cambios_data)
        print(f"Cambios guardados en el archivo: {archivo}")

    #registrar_cambio(id Int, placa Int, tipo String):Boolean