import os

def cargar_datos(archivo):
    if not os.path.exists(archivo):
        return []
    with open(archivo, "r") as f:
        return [line.strip() for line in f]

def guardar_datos(archivo, datos):
    with open(archivo, "w") as f:
        f.write("\\n".join(datos))


def toFile(self, filename='agenda.txt'):
        full_path = "Laboratorios/Laboratorio_2_y_3/Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:
            for usuario in self.registro:
                archivo.write(str(usuario) + "\n")
            archivo.close()

    
def import_Data(self, filename="agenda.txt"):
    ruta = "Laboratorios/Laboratorio_2_y_3/Datos/" + filename
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()  # Eliminar saltos de línea o espacios extra
            new_linea = linea.split(",")
            fecha = new_linea[2].split("-")
            new_fecha = Fecha(fecha[0], fecha[1], fecha[2])
            new_direccion = Direccion(new_linea[6], new_linea[7], new_linea[8], new_linea[9], new_linea[10], new_linea[11])
            new_user = Usuario(new_linea[0], int(new_linea[1]), new_fecha, new_linea[3], int(new_linea[4]), new_linea[5], new_direccion)
            self.agregar(new_user)
        archivo.close()