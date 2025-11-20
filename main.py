import networkx as nx
import matplotlib.pyplot as plt 
from mapdata import grafo_base, agregar_POIs
#prueba para verificar usuario de github

def encontrar_ruta(graph, origen, destino):
    try:
        ruta = nx.dijkstra_path(graph, source=origen, target=destino, weight='weight')
        longitud = nx.dijkstra_path_length(graph, source=origen, target=destino, weight='weight')
        return ruta, longitud
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return None, None

def procesar_input(valor_input):
    if valor_input.isdigit():
        return int(valor_input)
    else:
        return valor_input

def opcion_b_ruta_con_parada(graph, origen, parada, destino):

    ruta1, longitud1 = encontrar_ruta(graph, origen, parada)
    
    ruta2, longitud2 = encontrar_ruta(graph, parada, destino)
    
    if ruta1 and ruta2:
        ruta_completa = ruta1 + ruta2[1:]
        longitud_total = longitud1 + longitud2
        
        print(f"\n--- Ruta con parada en '{parada}' ---")
        print(f"Tramo 1 ({origen} -> {parada}): {longitud1:.2f} km")
        print(f"Tramo 2 ({parada} -> {destino}): {longitud2:.2f} km")
        print(f"\nCamino: {' -> '.join(map(str, ruta_completa))}")
        print(f"Distancia Total: {longitud_total:.2f} km")
    else:
        print("\nNo se pudo calcular la ruta")

def opcion_c_ruta_con_obstaculo(graph, origen, destino, obstaculo):

    mapa_temporal = graph.copy()
    
    if mapa_temporal.has_node(obstaculo):
        mapa_temporal.remove_node(obstaculo)
        print(f"\n--- Calculando ruta evitando '{obstaculo}' ---")
        
        ruta, longitud = encontrar_ruta(mapa_temporal, origen, destino)
        
        if ruta:
            print(f"Camino: {' -> '.join(map(str, ruta))}")
            print(f"Distancia total: {longitud:.2f} km")
        else:
            print(f"No hay ruta de'{origen}' a '{destino}' evitando '{obstaculo}'.")
    else:
        print(f"\nError '{obstaculo}' ")

if __name__ == "__main__":
    
    mapa_base = grafo_base()
    mapa_completo = agregar_POIs(mapa_base)
    
    while True:
        print("\n" + "="*40)
        print("          Seleccion una opcion")
        print("="*40)
        print("a) Ruta mas rapida (de A a B)")
        print("b) Ruta con parada (de A a B, pasando por C)")
        print("c) Ruta con obstaculo (de A a B, evitando C)")
        print("Escriba 'x' para cerrar el programa.")
        print("-"*40)
        
        opcion = input("Seleccione una opción (a, b, c): ").lower()
        
        if opcion == 'x':
            print("Programa finalizado, Chao (～￣▽￣)～")
            break
            
        elif opcion == 'a':
            origen = procesar_input(input("Punto de inicio: "))
            destino = procesar_input(input("Destino: "))
            ruta, longitud = encontrar_ruta(mapa_completo, origen, destino)
            if ruta:
                print(f"\n--- Ruta encontrada de '{origen}' a '{destino}' ---")
                print(f"Camino: {' -> '.join(map(str, ruta))}")
                print(f"Distancia total: {longitud:.2f} km")
            else:
                print(f"\nNo se encontro una ruta")

        elif opcion == 'b':
            origen = procesar_input(input("Punto de inicio (A): "))
            parada = procesar_input(input("Parada (C): "))
            destino = procesar_input(input("Destino (B): "))
            opcion_b_ruta_con_parada(mapa_completo, origen, parada, destino)

        elif opcion == 'c':
            origen = procesar_input(input("Punto de inicio (A): "))
            destino = procesar_input(input("Destino (B): "))
            obstaculo = procesar_input(input("Punto a evitar (C): "))
            opcion_c_ruta_con_obstaculo(mapa_completo, origen, destino, obstaculo)

        else:
            print("\nEscoja a, b, c o x")