import pandas as pd
import pathlib as path

class Datos:
    
    def __init__(self, ruta_archivo):
        self.ruta_archivo = path(__file__).parent / ruta_archivo
        
    def leer_archivo(self):
        return pd.read_csv(self.ruta_archivo)
    
    def cargar_grafo(self, grafo):
        datos = self.leer_archivo()
        for index, row in datos.iterrows():
            grafo.agregar_arista(row['A'], row['B'], row['KM'], row['Minutos'])