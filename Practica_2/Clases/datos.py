import pandas as pd
from pathlib import Path
from Clases.grafo import Grafo

class Datos:
    
    def __init__(self, ruta_archivo):
        self.ruta_archivo = Path(__file__).parent
        
    def leer_archivo(self):
        df = pd.read_csv(self.ruta_archivo, sep = ";", header =None, names=['A', 'B', 'KM', 'Minutos'])
        df["A"] = df["A"].str.strip()
        df["B"] = df["B"].str.strip()
        return df
    
    def cargar_grafo(self, grafo):
        datos = self.leer_archivo()
        for index, row in datos.iterrows():
            Grafo.agregar_arista(row['A'], row['B'], row['KM'], row['Minutos'])