
class Equipo:

    def __init__(self, nombre = None, numero_placa = None, fecha_compra = None, valor_compra = None, empleado = None):
        self._nombre = nombre
        self._numero_placa = numero_placa
        self._fecha_compra = fecha_compra
        self._valor_compra = valor_compra
        self._empleado = empleado

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nomnbre):
        self._nombre = nomnbre
    def get_numero_placa(self):
        return self._numero_placa
    def set_numero_placa(self, numero_placa):
        self._numero_placa = numero_placa
    def get_fecha_compra(self):
        return self._fecha_compra
    def set_fecha_compra(self, fecha):
        self._fecha_compra = fecha
    def get_valor_compra(self):
        return self._valor_compra
    def set_valor_compra(self, valor):
        self._valor_compra = valor
    def get_empleado(self):
        return self._empleado
    def set_empleado(self, empleado):
        self._empleado = empleado
    def __str__(self):
        return f'{self._nombre},{self._numero_placa},{self._fecha_compra},{self._valor_compra}, {self._empleado}'

