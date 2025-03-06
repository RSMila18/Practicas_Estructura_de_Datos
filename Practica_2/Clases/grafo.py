import networkx as nx

class Grafo:
    
    def __init__(self):
        self.grafo = nx.Graph()
        
    def agregar_arista(self, ciudad_a, ciudad_b, distancia, tiempo):
        self.grafo.add_edge(ciudad_a, ciudad_b, distancia=distancia, tiempo=tiempo)
        
    def estan_ciudades_conectadas(self, ciudad_a, ciudad_b):
        return self.grafo.has_edge(ciudad_a, ciudad_b)
    
    def camino_mas_corto_distancia(self, ciudad_a, ciudad_b):
        try:
            return nx.dijkstra_path(self.grafo, ciudad_a, ciudad_b, weight='distancia')
        except nx.NetworkXNoPath:
            return f"No hay camino entre {ciudad_a} y {ciudad_b}"
        except nx.NodeNotFound:
            return f"Una o ambas ciudades no se encuentra en el grafo"

    def camino_mas_corto_tiempo(self, ciudad_a, ciudad_b):
        try:
            return nx.dijkstra_path(self.grafo, ciudad_a, ciudad_b, weight='tiempo')
        except nx.NetworkXNoPath:
            return f"No hay camino entre {ciudad_a} y {ciudad_b}"
        except nx.NodeNotFound:
            return f"Una o ambas ciudades no se encuentra en el grafo"