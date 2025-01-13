import os

def cargar_datos(archivo):
    if not os.path.exists(archivo):
        return []
    with open(archivo, "r") as f:
        return [line.strip() for line in f]

def guardar_datos(archivo, datos):
    with open(archivo, "w") as f:
        f.write("\\n".join(datos))
