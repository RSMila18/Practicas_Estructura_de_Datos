from __future__ import annotations
import os
from Listas.doble_list import DoubleList
from Clases.fecha import Fecha

class Equipo:
    equipos = DoubleList()
    def __init__(self, nombre = None, numero_placa = None, fecha_compra = None, valor_compra = None, empleado = None):
        self._nombre = nombre
        self._numero_placa = numero_placa
        self._fecha_compra = fecha_compra
        self._valor_compra = valor_compra
        self._empleado = empleado

    def get_equipos():
        return Equipo.equipos
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
        nombre = "None"
        ident = "None"
        if self.get_empleado() != None:
            nombre = self._empleado.get_nombre()
            ident = self._empleado.get_id()
            
        return f'{nombre} {ident} {self._nombre} {self._numero_placa} {self._fecha_compra.get_dia()} {self._fecha_compra.get_mes()} {self._fecha_compra.get_A()} {self._valor_compra}'

    def buscar(placa):
        a = None
        current = Equipo.equipos.first()
        for _ in range(Equipo.equipos.size()):
            if current is not None:
                if int(placa) == current.get_Data().get_numero_placa():
                    a = current.get_Data()
                    return a
                else:
                    current = current.get_Next()

    def agregar(e):
        if Equipo.equipos.is_Empty() == False and Equipo.buscar(e.get_numero_placa()) != None:
                #print("El equipo ya existe")
                return False
        else:
            if e.get_empleado() == None or e.get_empleado() == "None":
                Equipo.equipos.add_last(e)
                Equipo.toFile()
                return True
            else:
                new_employees = e.get_empleado()
                new_employees.agregar_inventario(e)
                Equipo.equipos.add_last(e)
                Equipo.toFile()
                #print("El equipo ha sido agregado con exito")
                return True

    def toFile(filename='InventarioGeneral.txt'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, "Datos", filename)
        with open(full_path, "w", encoding="utf-8") as archivo:
            current = Equipo.equipos.first()
            while current is not None:
                equipo = current.get_Data()
                archivo.write(str(equipo) + "\n") 
                current = current.get_Next()


    @staticmethod
    def import_equipos(filename="InventarioGeneral.txt"):
        from Clases.empleado import Empleado
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(current_dir, "Datos", filename)
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()  
                new_linea = linea.split(" ")
                #def __init__(self, nombre = None, numero_placa = None, fecha_compra = None, valor_compra = None, empleado = None
                #Pedro-Gomez 1075689 MONITOR_DELL 50245325 1 4 2016 300000}
                if new_linea[0] == None or new_linea[0] == "None":
                    new_employees = None
                else:
                    new_employees = Empleado.buscar(int(new_linea[1]))

                new_fecha = Fecha(new_linea[4], new_linea[5], new_linea[6])
                new_product = Equipo(new_linea[2], int(new_linea[3]), new_fecha, int(new_linea[7]), new_employees)
                Equipo.agregar(new_product)
                #print(f"{new_product}")
            archivo.close()
    
    def consultar_inventario():
        current = Equipo.equipos.first()
        for _ in range(Equipo.equipos.size()):
            if current is not None:
                print(current.get_Data())
                current = current.get_Next()

    @classmethod
    def eliminar(cls, Objeto):
        temp = cls.equipos.first()

        if temp is None:  # Si la lista está vacía
            return False

        if Objeto == temp.get_Data():  # Si el objeto es el primer nodo
            return cls.equipos.remove_first()

        while temp is not None:
            if temp.get_Data() == Objeto:  # Encuentra el nodo a eliminar
                new = temp.get_Data()
                anterior = temp.get_Prev()
                siguiente = temp.get_Next()

                if siguiente is None:  # Si es el último nodo
                    anterior.set_Next(None)
                else:  # Si no es el último nodo
                    anterior.set_Next(siguiente)
                    siguiente.set_Prev(anterior)

                temp.set_Prev(None)
                temp.set_Next(None)
                print(f"Nodo eliminado: {temp.get_Data()}")
                

                new.set_empleado(None)
                cls.agregar(new)
                print(f"Nodo nuevo: {new}")
                return True

            temp = temp.get_Next()

        print("Objeto no encontrado en la lista.")
        return False