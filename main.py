import networkx as nx
import matplotlib.pyplot as plt 
from mapdata import grafo_base, agregar_POIs

def encontrar_ruta(graph, origen, destino):
    try:
        ruta = nx.dijkstra_path(graph, source=origen, target=destino, weight='weight')
        longitud = nx.dijkstra_path_length(graph, source=origen, target=destino, weight='weight')
        
        print(f"\n--- Ruta de '{origen}' a '{destino}' ---")
        print(f"Camino: {' -> '.join(map(str, ruta))}")
        print(f"Distancia total: {longitud:.2f} km")
        
        return ruta
    except nx.NetworkXNoPath:
        print(f"\nNo hay ruta de '{origen}' a '{destino}'.")
        return []
    except nx.NodeNotFound:
        print(f"\nError")
        return []

if __name__ == "__main__":
    
    mapa_base = grafo_base()
    mapa_completo = agregar_POIs(mapa_base)
    print("-" * 30)
    while True:
        origen_input = input("Punto de partida (o 'salir' para terminar): ")
        
        if origen_input.lower() == 'salir':
            print("Programa finalizado")
            break  

        destino_input = input("Destino: ")
 
        if origen_input.isdigit():
            origen = int(origen_input)
        else:
            origen = origen_input
            
        if destino_input.isdigit():
            destino = int(destino_input)
        else:
            destino = destino_input

        encontrar_ruta(mapa_completo, origen, destino)
        
        print("-" * 30)