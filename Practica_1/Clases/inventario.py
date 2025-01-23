from Listas.doble_list import DoubleList
from Listas.doble_node import DoubleNode
from Clases.empleado import Empleado
from Clases.equipo import Equipo

class Inventario(Equipo):

    def get_inventario(self):
        return super().equipos
    def agregar_equipo(equipo, id_empleado):
        empleado = Empleado.buscar(id_empleado)
        if empleado == -1:
            print("El empleado asociado a esta cedula no se encuentra")
            return False    
        current = Equipo.equipos.first()
        while current is not None:
            if current.get_Data().get_numero_placa() == equipo.get_numero_placa():
                print("Ya Existe un equipo con esta placa")
                return False
            current = current.get_Next()
        equipo.set_empleado(empleado)
        Equipo.equipos.add_last(equipo)
        empleado.get_inventario().add_last(equipo)
        print(f"Equipo agregado")
        return True

    def eliminar_equipo(self, numero_placa):
        current = self.equipos.first()
        while current is not None:
            if current.get_Data().get_numero_placa()==numero_placa:
                self.equipos.remove(current)
                print(f"Equipo eliminado")
                return True
    
    def buscar(placa):
        return Equipo.buscar(placa)
    
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
        
    def modificar_empleado_en_archivo(id_empleado, placa):
        try:
            # Abrimos el archivo en modo lectura
            with open("InventarioGeneral.txt", "r") as archivo:
                lineas = archivo.readlines()
            
            # Volvemos a abrir el archivo en modo escritura
            with open("InventarioGeneral.txt", "w") as archivo:
                for linea in lineas:
                    # Si la línea contiene el ID del empleado, lo modificamos
                    if str(id_empleado) and str(placa) in linea:
                        # Reemplazamos los datos del empleado por 'None'
                        partes = linea.split()
                        partes[0] = 'None'  # Nombre del empleado
                        partes[1] = 'None'  # Apellido del empleado
                        # Escribimos la línea modificada
                        archivo.write(" ".join(partes) + "\n")
                    else:
                        # Si no corresponde al empleado, simplemente escribimos la línea original
                        archivo.write(linea)
            
            print(f"Los datos del empleado con ID {id_empleado} han sido modificados.")
            return True

        except FileNotFoundError:
            print("El archivo InventarioGeneral.txt no fue encontrado.")
            return False
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return False

