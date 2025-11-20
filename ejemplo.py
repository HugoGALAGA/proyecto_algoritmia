import networkx as nx
import matplotlib.pyplot as plt # Usaremos esto para una visualización simple

def crear_grafo_base():
    """
    Esta función crea y devuelve el grafo base de la Zona 1 
    basado en el diagrama.
    """
    # 1. Crear un Grafo Dirigido
    # Usamos DiGraph porque las calles tienen una dirección específica.
    G = nx.DiGraph()

    # 2. Añadir todos los Nodos de Intersección
    # Tu diagrama tiene hasta el nodo 59, así que los creamos todos en un bucle.
    # El rango llega a 60 para que incluya el nodo 59.
    nodos_principales = range(1, 60)
    G.add_nodes_from(nodos_principales)

    # 3. Añadir todas las Aristas (Calles) con sus Pesos
    # ¡ESTA ES TU TAREA PRINCIPAL!
    # Aquí es donde traduces tu diagrama línea por línea.
    # Te doy los primeros ejemplos basados en tu imagen:

    # --- Fila Superior (5A Calle) ---
    G.add_edge(1, 2, weight=0.2)
    G.add_edge(2, 3, weight=0.14)
    G.add_edge(3, 4, weight=0.11)
    G.add_edge(4, 5, weight=0.15)
    # ... Continúa con el resto de la fila 5A Calle ...

    # --- Segunda Fila ---
    G.add_edge(16, 15, weight=0.21) # Nota: la flecha va de derecha a izquierda
    G.add_edge(17, 16, weight=0.13)
    # ... Continúa con el resto de esta fila ...

    # --- Conexiones Verticales (Carreras/Avenidas) ---
    G.add_edge(1, 15, weight=0.07)
    G.add_edge(15, 27, weight=0.1)
    G.add_edge(27, 38, weight=0.055)
    # ... Continúa con el resto de las conexiones verticales ...
    
    print("¡Grafo base de intersecciones creado!")
    return G

def anadir_pois(G):
    """
    Esta función añade los Puntos de Interés (POIs) al grafo existente.
    """
    # 4. Añadir Nodos de POI y conectarlos a la intersección más cercana
    # Ejemplo con "Centro técnico Guatemalteco"
    poi_centro_tecnico = "Centro Técnico Guatemalteco"
    nodo_cercano_ct = 15 # Supongamos que es la intersección más cercana
    distancia_ct = 0.02 # Mide o estima esta pequeña distancia en km
    G.add_node(poi_centro_tecnico)
    G.add_edge(nodo_cercano_ct, poi_centro_tecnico, weight=distancia_ct)
    G.add_edge(poi_centro_tecnico, nodo_cercano_ct, weight=distancia_ct)

    # Ejemplo con "Supermercado La Torre"
    poi_la_torre = "Supermercado La Torre"
    nodo_cercano_lt = 19 
    distancia_lt = 0.015
    G.add_node(poi_la_torre)
    G.add_edge(nodo_cercano_lt, poi_la_torre, weight=distancia_lt)
    G.add_edge(poi_la_torre, nodo_cercano_lt, weight=distancia_lt)

    # ... Añade el resto de tus POIs aquí ...
    
    print("¡POIs añadidos al grafo!")
    return G


# --- Código Principal que se Ejecuta ---
if __name__ == "__main__":
    # Creamos el grafo de calles
    mi_mapa = crear_grafo_base()
    
    # Le añadimos los Puntos de Interés
    mi_mapa_con_pois = anadir_pois(mi_mapa)

    # 5. Verificación Rápida
    # Imprimimos el número total de nodos y aristas para confirmar
    print("-" * 30)
    num_nodos = mi_mapa_con_pois.number_of_nodes()
    num_aristas = mi_mapa_con_pois.number_of_edges()
    print(f"Grafo final creado con {num_nodos} nodos y {num_aristas} aristas.")
    
    # Opcional: Visualizar el grafo (puede ser caótico, pero útil)
    # plt.figure(figsize=(15, 10))
    # pos = nx.spring_layout(mi_mapa_con_pois, k=0.5)
    # nx.draw(mi_mapa_con_pois, pos, with_labels=True, node_size=50, font_size=8)
    # plt.show()