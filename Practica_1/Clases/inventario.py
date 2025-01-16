from Listas.doble_list import DoubleList
from Listas.doble_node import DoubleNode
from Clases.empleado import Empleado
from Clases.equipo import Equipo

class Inventario(Equipo):

    def get_inventario(self):
        return super().equipos
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
            equipo = super().__init__(nombre, numero_placa, fecha_compra, valor_compra, empleado)
            DN = DoubleNode(equipo)
            empleado.get_inventario().add_last(DN)
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
        super().buscar()

    def ordenar_por_placa(self):

        current = self.equipos.first()
        
        for i in range(self.equipos.size()):
            current = self.equipos.first()
            for j in range(self.equipos.size() - i - 1):
                if int(current.get_Data().get_numero_placa()) > int(current.get_Next().get_Data().get_numero_placa()):
                    temp = current.get_Data()
                    current.set_Data(current.get_Next().get_Data())
                    current.get_Next().set_Data(temp)
                current = current.get_Next()

        print("Equipos ordenados por número de placa.")

