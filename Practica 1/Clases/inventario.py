from Listas.doble_list import DoubleList
from Clases.equipo import Equipo

class Inventario:
    def __init__(self):
        self.equipos = DoubleList()
        
    def agregar_equipo(self, equipo):
        
        nombre= input("Nombre del Equipo: ")
        numero_placa = input("Número de placa: ")
        fecha_compra= input("Fecha de compra (dd/mm/aaaa)")
        valor_compra = input("Valor de compra: ")
        
        equipo = Equipo(nombre, numero_placa, fecha_compra, valor_compra)
        
        current = self.equipos.first()
        while current is not None:
            if current.get_Data().get_numero_placa() == numero_placa:
                print("Ya Existe un equipo con esta placa")
                return False
            current = current.get_Next()
            
        self.equipos.add_last(equipo)
        print(f"Equipo agregado")
        return True
    #agregar_equipo(equipo Equipo): Boolean
    #eliminar_equipo(num_placa int): Boolean
    #consultar_inventario(): DoubleList<Equipo>