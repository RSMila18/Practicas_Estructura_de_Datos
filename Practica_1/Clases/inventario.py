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
        current = Equipo.equipos.first()
        for _ in range(Equipo.equipos.size(),1):
            if placa == current.get_Data().get_numero_placa():
                return current
            else:
                current = current.get_Next()       
        return -1

    def ordenar_por_placa(self):
        
        equipos_lista = []
        current = self.equipos.first()
    
        while current is not None:
            equipos_lista.append(current.get_Data())
            current = current.get_Next()
    
        
        for i in range(1, len(equipos_lista)):
            key = equipos_lista[i]
            j = i - 1
            
            while j >= 0 and int(equipos_lista[j].get_numero_placa()) > int(key.get_numero_placa()):
                equipos_lista[j + 1] = equipos_lista[j]
                j -= 1
            equipos_lista[j + 1] = key
    
        
        self.equipos = DoubleList()  
        for equipo in equipos_lista:
            self.equipos.add_last(equipo)
            print("Equipos ordenados por número de placa.")

    #agregar_equipo(equipo Equipo): Boolean
    def agregar_equipo(self, equipo: Equipo):
        # Verificar si el equipo ya existe en la lista de equipos (por número de placa)
        current = self.equipos.first()
        while current is not None:
            if current.get_Data().get_numero_placa() == equipo.get_numero_placa():
                print("Ya existe un equipo con esta placa.")
                return False
            current = current.get_Next()
    
        # Si el equipo no existe, agregarlo al inventario (DoubleList)
        self.equipos.add_last(equipo)
        print(f"Equipo {equipo.get_nombre()} agregado al inventario.")
        return True

    #eliminar_equipo(num_placa int): Boolean
    def eliminar_equipo(self, num_placa: int):
        # Buscar el equipo por número de placa
        current = self.equipos.first()
        while current is not None:
            if current.get_Data().get_numero_placa() == num_placa:
                # Si el equipo se encuentra, eliminarlo de la lista
                self.equipos.remove(current)
                print(f"Equipo con número de placa {num_placa} eliminado del inventario.")
                return True
            current = current.get_Next()
    
        # Si el equipo no se encuentra
        print(f"Equipo con número de placa {num_placa} no encontrado en el inventario.")
        return False

    #consultar_inventario(): DoubleList<Equipo>
    def consultar_inventario(self):
        return self.equipos
