import pandas as pd
from pathlib import Path

class Datos:
    
    def __init__(self, ruta_archivo):
        self.ruta_archivo = Path(__file__).parent / ruta_archivo
        
    def leer_archivo(self):
        df = pd.read_csv(self.ruta_archivo, sep = ";")
        return df
    
    def cargar_grafo(self, grafo):
        datos = self.leer_archivo()
        for index, row in datos.iterrows():
            grafo.agregar_arista(row['A'], row['B'], row['KM'], row['Minutos'])