class ControlCambios:

    def __init__(self, id_empleado = None, numero_placa = None, tipo_cambio = None, fecha = None, hora = None):
        self._id_empleado = id_empleado
        self._numero_placa = numero_placa
        self._tipo_cambio = tipo_cambio
        self._fecha = fecha
        self._hora = hora
    
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
    def get_hora(self):
        return self._hora
    def set_hora(self, hora):
        self._hora = hora
    def __str__(self):
        return f'{self._id_empleado},{self._numero_placa},{self._tipo_cambio},{self._fecha},{self._hora}'

    #registrar_cambio(id Int, placa Int, tipo String):Boolean