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
        
        while True:
            print("1. Verificar si dos ciudades están conectadas")
            print("2. Encontrar el camino más corto por distancia entre dos ciudades")
            print("3. Encontrar el camino más corto por tiempo entre dos ciudades")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                ciudad_a, ciudad_b = self.solicitar_ciudades()
                if self.grafo.estan_ciudades_conectadas(ciudad_a, ciudad_b):
                    print(f"{ciudad_a} y {ciudad_b} están conectadas.")
                else:
                    print(f"{ciudad_a} y {ciudad_b} no están conectadas.")
                    
            elif opcion == "2":
                ciudad_a, ciudad_b = self.solicitar_ciudades()
                camino = self.grafo.camino_mas_corto_distancia(ciudad_a, ciudad_b)
                print(f"El camino más corto entre {ciudad_a} y {ciudad_b} por la distancia es: {camino}")
            
            elif opcion == "3":
                ciudad_a, ciudad_b = self.solicitar_ciudades()
                camino = self.grafo.camino_mas_corto_tiempo(ciudad_a, ciudad_b)
                print(f"El camino más corto entre {ciudad_a} y {ciudad_b} por el tiempo es: {camino}")
                
            elif opcion == "4":
                break 
            
            else:
                print("Opción inválida.")
