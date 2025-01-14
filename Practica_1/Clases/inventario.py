from Listas.doble_list import DoubleList
from Listas.doble_node import DoubleNode
from Clases.empleado import Empleado
from Clases.equipo import Equipo

class Inventario:

    equipos = DoubleList()

    def agregar_equipo(self, equipo, id_empleado):
        
        nombre= input("Nombre del Equipo: ")
        numero_placa = input("Número de placa: ")
        fecha_compra= input("Fecha de compra (dd/mm/aaaa)")
        valor_compra = input("Valor de compra: ")
        empleado = Empleado.buscar(id_empleado)
        equipo = None
        if empleado == -1:
            equipo = Equipo(nombre, numero_placa, fecha_compra, valor_compra)
            print("El empleado asociado a esta cedula no se encuentra")
            return False
        
        else:
            equipo = Equipo(nombre, numero_placa, fecha_compra, valor_compra, empleado)
            DN = DoubleNode(equipo)
            empleado.consultar_inventario().add_last(DN)
            current = self.equipos.first()
            while current is not None:
                if current.get_Data().get_numero_placa() == numero_placa:
                    print("Ya Existe un equipo con esta placa")
                    return False
                current = current.get_Next()
                
            self.equipos.add_last(equipo)
            print(f"Equipo agregado")
            return True
    
    def eliminar_equipo(self, numero_placa):
        current = self.equipos.first()
        while current is not None:
            if current.get_Data().get_numero_placa()==numero_placa:
                self.equipos.remove(current)
                print(f"Equipo eliminado")
                return True
    
    def buscar(self, placa):
        current = Inventario.equipos.first()
        for _ in range(Inventario.equipos.size(),1):
            if placa == current.get_Data().get_numero_placa():
                return current
            else:
                current = current.get_Next()       
        return -1

    def consultar_inventario(self):
        return Inventario.equipos
        
    #agregar_equipo(equipo Equipo): Boolean
    #eliminar_equipo(num_placa int): Boolean
    #consultar_inventario(): DoubleList<Equipo>