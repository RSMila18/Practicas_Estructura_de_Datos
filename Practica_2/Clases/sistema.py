from Clases.datos import Datos
from Clases.grafo import Grafo

class Sistema:
    
    def __init__(self):
        self.lector = Datos("Datos/Datos vias.csv")
        self.grafo = Grafo()
        self.lector.cargar_grafo(self.grafo)
    
    def solicitar_ciudades(self):
        ciudad_a = input("Ingrese la ciudad de origen: ").strip().lower().title()
        ciudad_b = input("Ingrese la ciudad de destino: ").strip().lower().title()
        return ciudad_a, ciudad_b    
    
    def menu(self):
        
        while True:
            print("1. Verificar si dos ciudades están conectadas")
            print("2. Encontrar el camino más corto por distancia entre dos ciudades")
            print("3. Encontrar el camino más corto por tiempo entre dos ciudades")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                ciudad_a, ciudad_b = self.solicitar_ciudades()
                if self.grafo.estan_ciudades_conectadas(ciudad_a, ciudad_b):
                    print(f"\n{ciudad_a} y {ciudad_b} están conectadas. \n")
                else:
                    print(f"\n{ciudad_a} y {ciudad_b} no están conectadas. \n")
                    
            elif opcion == "2":
                ciudad_a, ciudad_b = self.solicitar_ciudades()
                camino = self.grafo.camino_mas_corto_distancia(ciudad_a, ciudad_b)
                print(f"\nEl camino más corto entre {ciudad_a} y {ciudad_b} por la distancia es: {camino} \n")
            
            elif opcion == "3":
                ciudad_a, ciudad_b = self.solicitar_ciudades()
                camino = self.grafo.camino_mas_corto_tiempo(ciudad_a, ciudad_b)
                print(f"\nEl camino más corto entre {ciudad_a} y {ciudad_b} por el tiempo es: {camino} \n")
                
            elif opcion == "4":
                break 
            
            else:
                print("\nOpción inválida. \n")
