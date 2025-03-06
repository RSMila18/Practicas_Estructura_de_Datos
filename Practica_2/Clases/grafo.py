import networkx as nx

class Grafo:
    
    def __init__(self):
        self.grafo = nx.Graph()
        
    def agregar_arista(self, ciudad_a, ciudad_b, distancia, tiempo):
        self.grado.add_edge(ciudad_a, ciudad_b, distancia=distancia, tiempo=tiempo)
        
    def estan_ciudades_conectadas(self, ciudad_a, ciudad_b):
        return self.grafo.has_edge(ciudad_a, ciudad_b)
    
    def camino_mas_corto_distancia(self, ciudad_a, ciudad_b):
        return nx.dijkstra_path(self.grafo, ciudad_a, ciudad_b, weight='distancia')
    
    def camino_mas_corto_tiempo(self, ciudad_a, ciudad_b):
        return nx.dijkstra_path(self.grafo, ciudad_a, ciudad_b, weight='tiempo')