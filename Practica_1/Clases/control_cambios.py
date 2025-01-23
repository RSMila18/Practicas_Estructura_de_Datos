import os
from datetime import datetime
from Listas.lista_simple import List
from Clases.fecha import Fecha

class ControlCambios:

    registro_cambios = List()

    def __init__(self, id_empleado = None, numero_placa = None, tipo_cambio = None, razon = None):
        self._id_empleado = id_empleado
        self._numero_placa = numero_placa
        self._tipo_cambio = tipo_cambio
        fecha_actual = Fecha(datetime.now().day, datetime.now().month, datetime.now().year) 
        self._fecha = fecha_actual
        self._hora = datetime.now()
        self._razon = razon
    
    def get_list():
        return ControlCambios.registrar_cambio
    def get_razon(self):
        return self._razon
    def set_razon(self, razon):
        self._razon = razon
    def get_id_empleado(self):
        return self._id_empleado
    def set_id_empleado(self, ide):
        self._id_empleado = ide
    def get_numero_placa(self):
        return self._numero_placa
    def set_numero_placa(self, num):
        self._numero_placa = num
    def get_tipo_cambio(self):
        return self._tipo_cambio
    def set_tipo_cambio(self, tipo):
        self._tipo_cambio = tipo
    def get_fecha(self):
        return self._fecha
    def set_fecha(self,fecha):
        self._fecha = fecha
    def get_hora(self):
        return self._hora    
    def __str__(self):
    
        return f'{self._id_empleado} {self._numero_placa} {self._tipo_cambio} {self._fecha.get_dia()} {self._fecha.get_mes()} {self._fecha.get_A()} {self._hora} {self._razon}'

    def toFile(changes, filename='Control_de_cambios.txt'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, "Datos", filename)
        #full_path = "Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:
            for cambios in changes:
                archivo.write(str(cambios) + "\n")
            archivo.close()

    def registrar_cambio(id_empleado, numero_placa, tipo_cambio, razon):
        
        cambio = ControlCambios(id_empleado, numero_placa, tipo_cambio, razon)
        ControlCambios.registro_cambios.add_Last(cambio)
        print(f"El Cambio ha sido registrado: {cambio}")
        
        cambios_data = []
        current = ControlCambios.registro_cambios.first()
        while current is not None:
            cambios_data.append(str(current.get_Data()))
            current = current.get_Next()
        ControlCambios.toFile(cambios_data)
        print(f"Los cambios han sido guardados con exito")

    def import_control():
        from Clases.empleado import Empleado
        from Clases.equipo import Equipo
        try:
            # Obtener la ruta completa del archivo
            current_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(current_dir, "Datos", "Control_de_cambios.txt")
            
            # Abre el archivo en modo lectura usando la ruta completa
            with open(full_path, "r") as archivo:
                for linea in archivo:
                    # Limpia y divide la línea en sus componentes
                    linea = linea.strip()
                    datos = linea.split(" ")  # Separar por espacios
                    #2345934 50245333 Agregar 22 1 2025 2025-01-22 22:21:15.612433 aprobada
                    #    0        1       2       345       6             7         8
                    empleado_id = int(datos[0])
                    numero_placa = int(datos[1])
                    tipo_cambio = datos[2]
                    estado = datos[8]

                    # Validar que el estado sea "Aprobado"
                    if estado == "aprobada":
                        # Buscar el equipo usando el método de la clase Equipo
                        equipo = Equipo.buscar(numero_placa)

                        if not equipo:
                            print(f"Error: El equipo con placa {numero_placa} no existe.")
                            continue

                        empleado_asociado = equipo.get_empleado()
                        empleado_actual_id = empleado_asociado.get_id() if empleado_asociado else None

                        if tipo_cambio == "Agregar":
                            # Validar que el empleado esté asociado al equipo
                            if empleado_actual_id != empleado_id:
                                print(f"Error: El empleado {empleado_id} no está asociado al equipo {numero_placa}.")
                                E = Empleado.buscar(empleado_id)
                                E.agregar_inventario(equipo)
                                #print("Error resuelto.")
                                continue

                            #print(f"Validación exitosa: El empleado {empleado_id} está asociado al equipo {numero_placa}.")

                        elif tipo_cambio == "Eliminar":
                            # Verificar si el empleado está asociado al equipo
                            if empleado_actual_id == empleado_id:
                                # Eliminar la asociación desde el equipo
                                equipo.set_empleado(None)

                                # Desasociar también desde el empleado
                                empleado = Empleado.buscar(empleado_id)
                                if empleado:
                                    empleado.eliminar_equipo(equipo)

                                #print(f"Eliminación exitosa: El equipo {numero_placa} ha sido eliminado del inventario de {empleado_id}.")
                            else:
                                print(f"Error: El equipo {numero_placa} no está asociado al empleado {empleado_id}.")

                        elif tipo_cambio == "Editar":
                            # Verificar que el equipo no esté asociado al empleado
                            if empleado_actual_id == empleado_id:
                                #print(f"Error: No se puede editar porque el empleado {empleado_id} aún está asociado al equipo {numero_placa}.")
                                continue

                            #print(f"Validación exitosa: Se puede editar el equipo {numero_placa} para el empleado {empleado_id}.")

                        else:
                            print(f"Info: Tipo de cambio '{tipo_cambio}' no reconocido. Línea ignorada.")
                    #else:
                        #print(f"Info: El cambio no está aprobado. Línea ignorada.")

        except FileNotFoundError:
            print(f"Error: El archivo 'Control_de_cambios.txt' no se encuentra en la ruta especificada.")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def buscar_por_id(id_empleado, filename="Control_de_cambios.txt"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(current_dir, "Datos", filename)
        
        cambios_asociados = []
        
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()  # Remueve saltos de línea y espacios innecesarios
                    if linea:  # Asegurarse de que no es una línea vacía
                        partes = linea.split(" ")  # Divide la línea por espacios
                        if partes[0] == str(id_empleado):  # Compara el ID del empleado
                            cambios_asociados.append(linea)
        except FileNotFoundError:
            print(f"El archivo {filename} no existe.")
        
        return cambios_asociados