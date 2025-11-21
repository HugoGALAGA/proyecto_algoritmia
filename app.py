import streamlit as st
import networkx as nx
from pyvis.network import Network
import tempfile

# 1. Grafo

def grafo_base():

    G = nx.DiGraph()

    principal_nodes= range (1,60)
    G.add_nodes_from(principal_nodes)


    #primera fila, la del nodo 1 a la 14 de la 4A calle que es el limite superior
    #va de izquierda a derecha 
    G.add_edge(1,2, weight = 0.2)
    G.add_edge(2,3, weight = 0.14)
    G.add_edge(3,4, weight = 0.11)
    G.add_edge(4,5, weight = 0.15)
    G.add_edge(5,6, weight = 0.12)
    G.add_edge(6,7, weight = 0.1)
    G.add_edge(7,8, weight = 0.1)
    G.add_edge(8,9, weight = 0.15)
    G.add_edge(9,10, weight = 0.16)
    G.add_edge(10,11, weight = 0.1)
    G.add_edge(11,12, weight = 0.07)
    G.add_edge(12,13, weight = 0.08)
    G.add_edge(13,14, weight = 0.18)

    #6A calle Segunda fila, va del nodo 15 al 26, de derecha a izquierda

    G.add_edge(26,25, weight = 0.11)
    G.add_edge(25,24, weight = 0.15)
    G.add_edge(24,23, weight = 0.02)
    G.add_edge(23,22, weight = 0.15)
    G.add_edge(22,21, weight = 0.09)
    G.add_edge(21,20, weight = 0.09)
    G.add_edge(20,19, weight = 0.12)
    G.add_edge(19,18, weight = 0.15)
    G.add_edge(18,17, weight = 0.11)
    G.add_edge(17,16, weight = 0.13)
    G.add_edge(16,15, weight = 0.21)

    #Tercera fila, esta es la 7A calle, va de derecha a izquierda 

    G.add_edge(27,28, weight = 0.19)
    G.add_edge(28,29, weight = 0.14)
    G.add_edge(29,30, weight = 0.115)
    G.add_edge(30,31, weight = 0.16)
    G.add_edge(31,32, weight = 0.12)
    G.add_edge(33,34, weight = 0.11)
    G.add_edge(34,35, weight = 0.07)
    G.add_edge(35,36, weight = 0.08)
    G.add_edge(36,37, weight = 0.17)

    #8A Calle, cuarta fila, izquierda a derecha
    G.add_edge(47,46, weight = 0.17)
    G.add_edge(46,45, weight = 0.15)
    G.add_edge(45,44, weight = 0.12)
    G.add_edge(43,42, weight = 0.13)
    G.add_edge(42,41, weight = 0.15)
    G.add_edge(41,40, weight = 0.11)
    G.add_edge(40,39, weight = 0.14)
    G.add_edge(39,38, weight = 0.22)

    #9A Calle, quinta fila, derecha a izquierda
    
    G.add_edge(48,49, weight = 0.24)
    G.add_edge(49,50, weight = 0.16)
    G.add_edge(50,51, weight = 0.12)
    G.add_edge(51,52, weight = 0.141)
    G.add_edge(52,53, weight = 0.12)
    G.add_edge(53,54, weight = 0.18)
    G.add_edge(54,55, weight = 0.16)
    G.add_edge(55,56, weight = 0.15)
    G.add_edge(56,57, weight = 0.11)
    G.add_edge(57,58, weight = 0.15)
    G.add_edge(58,59, weight = 0.18)

    #Carretera Ca - 9, es la unica bidireccional

    G.add_edge(1, 15, weight=0.07)
    G.add_edge(15, 1, weight=0.07)
    G.add_edge(15, 27, weight=0.1)
    G.add_edge(27, 15, weight=0.1)
    G.add_edge(27, 38, weight=0.055)
    G.add_edge(38, 27, weight=0.055)
    G.add_edge(38, 48, weight=0.13)
    G.add_edge(48, 38, weight=0.13)

    #1A Avenida abajo a arriba

    G.add_edge(49, 39, weight=0.12)
    G.add_edge(39, 28, weight=0.056)
    G.add_edge(28, 16, weight=0.11)
    G.add_edge(16, 2, weight=0.08)

    #2A Avenida arriba a abajo

    G.add_edge(3, 17, weight=0.07)
    G.add_edge(17, 29, weight=0.1)
    G.add_edge(29, 40, weight=0.055)
    G.add_edge(40, 50, weight=0.115)

    #3A Avenida abajo a arriba
    
    G.add_edge(51, 41, weight=0.12)
    G.add_edge(41, 30, weight=0.056)
    G.add_edge(30, 18, weight=0.1)
    G.add_edge(18, 4, weight=0.09)

    #4A Avenida arriba a abajo

    G.add_edge(5, 19, weight=0.08)
    G.add_edge(19, 31, weight=0.1)
    G.add_edge(31, 42, weight=0.055)
    G.add_edge(42, 52, weight=0.13)
    
    #5A Avenida abajo a arriba

    G.add_edge(53, 43, weight=0.13)
    G.add_edge(53, 32, weight=0.055)
    G.add_edge(32, 20, weight=0.1)
    G.add_edge(20, 6, weight=0.08)

    #6A Avenida abajo a arriba
    #Aqui hay mas pero en si son caminos de pie, no para auto o vehiculo asi que mejor no los puse

    G.add_edge(7, 21, weight=0.08)

    #7A Avenida abajo a arriba

    G.add_edge(54, 22, weight=0.29)
    G.add_edge(22,8, weight=0.08)

    #8AA Avenida

    G.add_edge(9,23, weight=0.09)

    #8A Avenida

    G.add_edge(24,55, weight=0.292)

    #9A Avenida

    G.add_edge(56, 44, weight=0.13)
    G.add_edge(44, 33, weight=0.055)
    G.add_edge(33, 25, weight=0.1)
    G.add_edge(25, 10, weight=0.07)

    #10A Avenida

    G.add_edge(11, 26, weight=0.08)
    G.add_edge(26, 34, weight=0.11)
    G.add_edge(34, 45, weight=0.06)
    G.add_edge(45, 57, weight=0.135)

    #10AA Avenida

    G.add_edge(12, 35, weight=0.19)

    #11A Avenida

    G.add_edge(58, 46, weight=0.135)
    G.add_edge(46, 36, weight=0.06)
    G.add_edge(36, 13, weight=0.19)

    #12A Avenida

    G.add_edge(14, 37, weight=0.2)
    G.add_edge(37, 47, weight=0.06)
    G.add_edge(47, 59, weight=0.135)
    
    return G

def agregar_POIs(G):

    poi_centro_tecnico = "Centro técnico Guatemalteco"
    G.add_node(poi_centro_tecnico)
    G.add_edge(1, poi_centro_tecnico, weight=0.02)
    G.add_edge(poi_centro_tecnico, 1, weight=0.02)
    G.add_edge(15, poi_centro_tecnico, weight=0.05)
    G.add_edge(poi_centro_tecnico, 15, weight=0.05)

    poi_conacmi = "CONACMI"
    G.add_node(poi_conacmi)
    G.add_edge(3, poi_conacmi, weight=0.035)
    G.add_edge(poi_conacmi, 17, weight=0.035)

    poi_colegio_anglo = "Colegio Anglo Guatemalteco"
    G.add_node(poi_colegio_anglo)
    G.add_edge(27, poi_colegio_anglo, weight=0.08)
    G.add_edge(poi_colegio_anglo, 28, weight=0.11)

    poi_pnc = "PNC"
    G.add_node(poi_pnc)
    G.add_edge(30, poi_pnc, weight=0.02)
    G.add_edge(poi_pnc, 18, weight=0.08)
    
    poi_santuario = "Santuario de Guadalupe"
    G.add_node(poi_santuario)
    G.add_edge(40, poi_santuario, weight=0.7)
    G.add_edge(poi_santuario, 39, weight=0.7)
    
    poi_gyt = "G&T" 
    G.add_node(poi_gyt)
    G.add_edge(42, poi_gyt, weight=0.075)
    G.add_edge(poi_gyt, 41, weight=0.075)

    poi_parque_jbm = "Parque José Batres Montufar"
    G.add_node(poi_parque_jbm)
    G.add_edge(3, poi_parque_jbm, weight=0.09)
    G.add_edge(poi_parque_jbm, 4, weight=0.02)

    poi_la_torre = "Supermercado La Torre"
    G.add_node(poi_la_torre)
    G.add_edge(20, poi_la_torre, weight=0.1)
    G.add_edge(poi_la_torre, 19, weight=0.02)

    poi_patsy = "PATSY"
    G.add_node(poi_patsy)
    G.add_edge(20, poi_patsy, weight=0.02)
    G.add_edge(poi_patsy, 6, weight=0.06)

    poi_palacio_nacional = "Palacio Nacional de la Cultura"
    G.add_node(poi_palacio_nacional)
    G.add_edge(22, poi_palacio_nacional, weight=0.05)
    G.add_edge(poi_palacio_nacional, 21, weight=0.05)

    poi_pizza_hut = "Pizza Hut"
    G.add_node(poi_pizza_hut)
    G.add_edge(54, poi_pizza_hut, weight=0.11)
    G.add_edge(poi_pizza_hut, 22, weight=0.18)

    poi_alma_cisne = "Almacén el Cisne"
    G.add_node(poi_alma_cisne)
    G.add_edge(25, poi_alma_cisne, weight=0.05)
    G.add_edge(poi_alma_cisne, 24, weight=0.1)

    #revisar este si hay problemas por que me quedo duda de este mapeo
    poi_sis_peniten = "Direccion General del Sistema Peninteciario"
    G.add_node(poi_sis_peniten)
    G.add_edge(35, poi_sis_peniten, weight=0.04)
    G.add_edge(poi_sis_peniten, 36, weight=0.04)

    poi_hotel = "Hotel"
    G.add_node(poi_hotel)
    G.add_edge(13, poi_hotel, weight=0.05)
    G.add_edge(poi_hotel, 14, weight=0.13)
    
    poi_parque_colon = "Parque Colón"
    G.add_node(poi_parque_colon)
    G.add_edge(47, poi_parque_colon, weight=0.085)
    G.add_edge(poi_parque_colon, 46, weight=0.085)
    G.add_edge(58, poi_parque_colon, weight=0.065)
    G.add_edge(poi_parque_colon, 46, weight=0.065)

    poi_merc_central = "Mercado Central"
    G.add_node(poi_merc_central)
    G.add_edge(44, poi_merc_central, weight=0.028)
    G.add_edge(poi_merc_central, 33, weight=0.027)

    poi_plaza = "Plaza de la constitucion"
    G.add_node(poi_plaza)
    G.add_edge(54, poi_plaza, weight=0.13)
    G.add_edge(poi_plaza, 22, weight=0.16)
    G.add_edge(43, poi_plaza, weight=0.028)
    G.add_edge(poi_plaza, 32, weight=0.027)

    return G 


# 2. RUTAS

def encontrar_ruta(graph, origen, destino):
    try:
        ruta = nx.dijkstra_path(graph, source=origen, target=destino, weight='weight')
        longitud = nx.dijkstra_path_length(graph, source=origen, target=destino, weight='weight')
        return ruta, longitud
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return None, None

# 3. VISUALIZACION

def visualizar_grafo(G, ruta_resaltada=None, obstaculo=None):
    # Crear red de Pyvis
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", directed=True)
    
    # Generar posiciones estilo "Grid/Laberinto" (Opcional pero recomendado para calles)
    # Si no usas esto, el grafo será una "nube" desordenada.
    # Aquí hacemos un layout automático simple, pero para un mapa real
    # idealmente asignarías coordenadas X, Y fijas a cada nodo.
    pos = nx.kamada_kawai_layout(G) 

    for node in G.nodes():
        x, y = pos[node][0] * 1000, pos[node][1] * 1000 # Escalar para Pyvis
        
        color = "#00bfff" # Azul por defecto (calles)
        size = 15
        label = str(node)
        
        # Colores especiales
        if isinstance(node, str): # Es un POI
            color = "#00ff00" # Verde
            size = 20
        
        if obstaculo and node == obstaculo:
            color = "#ff0000" # Rojo (Obstáculo)
            shape = "box"
        
        # Si hay una ruta y este nodo es parte de ella
        if ruta_resaltada and node in ruta_resaltada:
            color = "#ffff00" # Amarillo (Ruta)
            if node == ruta_resaltada[0]: color = "#ff00ff" # Inicio
            if node == ruta_resaltada[-1]: color = "#ff00ff" # Fin

        net.add_node(node, label=label, x=x, y=y, color=color, size=size, title=str(node))

    # Agregar las aristas
    for u, v, data in G.edges(data=True):
        color = "#444444" # Gris oscuro por defecto
        width = 1
        
        # Si la arista es parte de la ruta
        if ruta_resaltada:
            # Verificar si la conexión u->v está en la ruta secuencial
            if u in ruta_resaltada and v in ruta_resaltada:
                # Chequeo estricto de secuencia
                idx_u = ruta_resaltada.index(u)
                if idx_u + 1 < len(ruta_resaltada) and ruta_resaltada[idx_u + 1] == v:
                    color = "#ffff00"
                    width = 4

        weight_label = str(data.get('weight', ''))
        net.add_edge(u, v, title=f"Dist: {weight_label}", color=color, width=width)

    # Opciones de física (desactivar para que parezca mapa fijo)
    net.toggle_physics(False)
    return net

# 4. INTERFAZ

st.set_page_config(layout="wide", page_title="Pathfinder Ciudad")

# Cargar grafo (IMPORTANTE: Asegúrate de importar tu grafo completo aquí)
# Para el ejemplo, usaré los imports de tu archivo si existen, sino el dummy
try:
    from mapdata import grafo_base, agregar_POIs
    mapa_base = grafo_base()
    mapa_completo = agregar_POIs(mapa_base)
except ImportError:
    # Fallback si no encuentra el archivo mapdata
    st.warning("No se encontró mapdata.py, usando grafo de ejemplo vacio.")
    mapa_completo = nx.DiGraph()
    mapa_completo.add_node(1)

st.title("📍 Visualizador de Rutas (Pathfinder)")

col1, col2 = st.columns([1, 3])

with col1:
    st.header("Controles")
    modo = st.radio("Modo de ruta:", ["A) Ruta Rápida", "B) Con Parada", "C) Con Obstáculo"])
    
    lista_nodos = list(mapa_completo.nodes())
    
    origen = st.selectbox("Origen", lista_nodos, index=0)
    destino = st.selectbox("Destino", lista_nodos, index=1 if len(lista_nodos)>1 else 0)
    
    ruta_calculada = []
    distancia_total = 0
    nodo_obstaculo = None

    if modo == "A) Ruta Rápida":
        if st.button("Calcular Ruta"):
            ruta_calculada, distancia_total = encontrar_ruta(mapa_completo, origen, destino)

    elif modo == "B) Con Parada":
        parada = st.selectbox("Punto de Parada", lista_nodos)
        if st.button("Calcular Ruta con Parada"):
            r1, d1 = encontrar_ruta(mapa_completo, origen, parada)
            r2, d2 = encontrar_ruta(mapa_completo, parada, destino)
            if r1 and r2:
                ruta_calculada = r1 + r2[1:]
                distancia_total = d1 + d2

    elif modo == "C) Con Obstáculo":
        nodo_obstaculo = st.selectbox("Evitar nodo:", lista_nodos)
        if st.button("Calcular evitando obstáculo"):
            mapa_temp = mapa_completo.copy()
            if mapa_temp.has_node(nodo_obstaculo):
                mapa_temp.remove_node(nodo_obstaculo)
                ruta_calculada, distancia_total = encontrar_ruta(mapa_temp, origen, destino)

    if ruta_calculada:
        st.success(f"Distancia Total: {distancia_total:.2f} km")
        st.write(f"Ruta: {' → '.join(map(str, ruta_calculada))}")
    else:
        st.info("Selecciona puntos y calcula la ruta.")

with col2:
    st.header("Mapa Interactivo")
    # Generar y mostrar el grafo
    net = visualizar_grafo(mapa_completo, ruta_calculada, obstaculo=nodo_obstaculo)
    
    # Guardar en temporal para renderizar en Streamlit
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
        net.save_graph(tmp.name)
        with open(tmp.name, 'r', encoding='utf-8') as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=650)