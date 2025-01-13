from Listas.lista_simple import List
class Solicitud:

    solicitudes = List()

    def __init__(self, id_solicitud = None, tipo = None, estado = None, numero_placa = None, justificacion = None):
        self._id_solicitud = id_solicitud
        self._tipo = tipo
        self._estado = estado
        self._numero_placa = numero_placa
        self._justificacion = justificacion
        Solicitud.solicitudes.append(self)
    
    def get_id_solicitud(self):
        return self._id_solicitud
    def set_id_solicitud(self, ide):
        self._id_solicitud = ide
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
    def str__(self):
        return f'{self._id_solicitud},{self._tipo},{self._estado},{self._numero_placa},{self._justificacion}'

    def aprobar_solicitud(self):
        self._estado = "aprobar"
        return True
    def rechazar_solicitud(self):
        self._estado = "rechazar"
        return True