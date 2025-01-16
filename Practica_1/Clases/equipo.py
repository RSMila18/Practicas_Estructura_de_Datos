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

    def get_equipos(self):
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
        return f'{self._empleado.get_nombre()} {self._empleado.get_id()} {self._nombre} {self._numero_placa} {self._fecha_compra.get_dia()} {self._fecha_compra.get_mes()} {self._fecha_compra.get_A()} {self._valor_compra}'

    def buscar(placa):
        current = Equipo.equipos.first()
        for _ in range(Equipo.equipos.size()):
            if int(placa) == current.get_Data().get_numero_placa():
                return current.get_Data()
            else:
                current = current.get_Next()

    def toFile(empleados, filename='InventarioGeneral.txt'):
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
                #Pedro-Gomez 1075689 MONITOR_DELL 50245325 1 4 2016 300000
                new_employees = Empleado.buscar(int(new_linea[1]))
                new_fecha = Fecha(new_linea[4], new_linea[5], new_linea[6])
                new_product = Equipo(new_linea[2], int(new_linea[3]), new_fecha, int(new_linea[7]), new_employees)
                new_employees.agregar_inventario(new_product)
                Equipo.equipos.add_last(new_product)
                #print(f"{new_product}")
            archivo.close()
    
    def consultar_inventario():
        current = Equipo.equipos.first()
        for _ in range(Equipo.equipos.size()):
            print(current.get_Data())
            current = current.get_Next()