from Clases.datos import Datos
from Clases.grafo import Grafo

class Sistema:
    
    lector = Datos("Datos/Datos vias.csv")
    grafo = Grafo()
    lector.cargar_grafo(grafo)
    
    def solicitar_ciudades(self):
        ciudad_a = input("Ingrese la ciudad de origen: ")
        ciudad_b = input("Ingrese la ciudad de destino: ")
        return ciudad_a, ciudad_b    
    
    def menu(self):
        print("1. Verificar si dos ciudades están conectadas")
        print("2. Encontrar el camino más corto por distancia entre dos ciudades")
        print("3. Encontrar el camino más corto por tiempo entre dos ciudades")
        print("4. Salir")
