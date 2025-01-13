from Listas.doble_list import DoubleList
from Clases.equipo import Equipo

class Inventario:
    def __init__(self):
        self.equipos = DoubleList()

    #agregar_equipo(equipo Equipo): Boolean
    #eliminar_equipo(num_placa int): Boolean
    #consultar_inventario(): DoubleList<Equipo>