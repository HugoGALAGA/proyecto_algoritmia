from flask import Flask, render_template, request, jsonify
import networkx as nx

app = Flask(__name__)

LUGARES = {
    1: "Centro técnico Guatemalteco",
    2: "Colegio Anglo Guatemalteco",
    3: "CONACMI",
    4: "PNC",
    5: "Parque José Batres Montufar",
    6: "Supermercado La Torre",
    7: "PATSY",
    8: "Palacio Nacional de la Cultura",
    9: "Plaza de la constitucion",
    10: "Pizza Hut",
    11: "Almacén el Cisne",
    12: "Mercado Central",
    13: "Direccion General del Sistema Peninteciario",
    14: "Hotel",
    15: "Parque Colón",
    16: "Santuario de Guadalupe",
    17: "G&T"
}

def grafo_base():
    G = nx.DiGraph()
    principal_nodes= range (1,60)
    G.add_nodes_from(principal_nodes)

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

    G.add_edge(27,28, weight = 0.19)
    G.add_edge(28,29, weight = 0.14)
    G.add_edge(29,30, weight = 0.115)
    G.add_edge(30,31, weight = 0.16)
    G.add_edge(31,32, weight = 0.12)
    G.add_edge(33,34, weight = 0.11)
    G.add_edge(34,35, weight = 0.07)
    G.add_edge(35,36, weight = 0.08)
    G.add_edge(36,37, weight = 0.17)

    G.add_edge(47,46, weight = 0.17)
    G.add_edge(46,45, weight = 0.15)
    G.add_edge(45,44, weight = 0.12)
    G.add_edge(43,42, weight = 0.13)
    G.add_edge(42,41, weight = 0.15)
    G.add_edge(41,40, weight = 0.11)
    G.add_edge(40,39, weight = 0.14)
    G.add_edge(39,38, weight = 0.22)

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

    G.add_edge(1, 15, weight=0.07)
    G.add_edge(15, 1, weight=0.07)
    G.add_edge(15, 27, weight=0.1)
    G.add_edge(27, 15, weight=0.1)
    G.add_edge(27, 38, weight=0.055)
    G.add_edge(38, 27, weight=0.055)
    G.add_edge(38, 48, weight=0.13)
    G.add_edge(48, 38, weight=0.13)

    G.add_edge(49, 39, weight=0.12)
    G.add_edge(39, 28, weight=0.056)
    G.add_edge(28, 16, weight=0.11)
    G.add_edge(16, 2, weight=0.08)

    G.add_edge(3, 17, weight=0.07)
    G.add_edge(17, 29, weight=0.1)
    G.add_edge(29, 40, weight=0.055)
    G.add_edge(40, 50, weight=0.115)
    
    G.add_edge(51, 41, weight=0.12)
    G.add_edge(41, 30, weight=0.056)
    G.add_edge(30, 18, weight=0.1)
    G.add_edge(18, 4, weight=0.09)

    G.add_edge(5, 19, weight=0.08)
    G.add_edge(19, 31, weight=0.1)
    G.add_edge(31, 42, weight=0.055)
    G.add_edge(42, 52, weight=0.13)
    
    G.add_edge(53, 43, weight=0.13)
    G.add_edge(53, 32, weight=0.055)
    G.add_edge(32, 20, weight=0.1)
    G.add_edge(20, 6, weight=0.08)

    G.add_edge(7, 21, weight=0.08)

    G.add_edge(54, 22, weight=0.29)
    G.add_edge(22,8, weight=0.08)

    G.add_edge(9,23, weight=0.09)

    G.add_edge(24,55, weight=0.292)

    G.add_edge(56, 44, weight=0.13)
    G.add_edge(44, 33, weight=0.055)
    G.add_edge(33, 25, weight=0.1)
    G.add_edge(25, 10, weight=0.07)

    G.add_edge(11, 26, weight=0.08)
    G.add_edge(26, 34, weight=0.11)
    G.add_edge(34, 45, weight=0.06)
    G.add_edge(45, 57, weight=0.135)

    G.add_edge(12, 35, weight=0.19)

    G.add_edge(58, 46, weight=0.135)
    G.add_edge(46, 36, weight=0.06)
    G.add_edge(36, 13, weight=0.19)

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

def aplicar_trafico(graph, aplicar_pesado, aplicar_ligero):
    mapa_con_trafico = graph.copy()
    factor_pesado = 10.0
    factor_ligero = 5.0 
    
    calles_trafico_pesado = [
        (52, 53), (53, 54), (54, 55), (55, 56), (56, 57),
        (54, 22), (22, 8), (11, 26), (26, 34), (34, 45), (45, 57),
    ]
    
    calles_trafico_ligero = [
        (4, 5), (5, 6), (29, 40), (40, 50),
        (37, 47), (47, 46), (46, 45),
    ]

    if aplicar_pesado:
        for u, v in calles_trafico_pesado:
            if mapa_con_trafico.has_edge(u, v):
                mapa_con_trafico[u][v]['weight'] *= factor_pesado

    if aplicar_ligero:
        for u, v in calles_trafico_ligero:
            if mapa_con_trafico.has_edge(u, v):
                mapa_con_trafico[u][v]['weight'] *= factor_ligero
            
    return mapa_con_trafico

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_pois')
def get_pois():
    return jsonify(LUGARES)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    try:
        id_origen = int(data.get('origen'))
        id_destino = int(data.get('destino'))
        
        modo = data.get('modo') 
        id_intermedio = data.get('intermedio') 
        trafico_pesado = data.get('trafico_pesado', False)
        trafico_ligero = data.get('trafico_ligero', False)

        origen = LUGARES[id_origen]
        destino = LUGARES[id_destino]
        
        graph = grafo_base()
        graph = agregar_POIs(graph)
        graph = aplicar_trafico(graph, trafico_pesado, trafico_ligero)

        ruta = []
        distancia = 0

        if modo == 'simple':
            ruta = nx.dijkstra_path(graph, origen, destino, weight='weight')
            distancia = nx.dijkstra_path_length(graph, origen, destino, weight='weight')

        elif modo == 'parada':
            if id_intermedio:
                intermedio = LUGARES[int(id_intermedio)]
                r1 = nx.dijkstra_path(graph, origen, intermedio, weight='weight')
                d1 = nx.dijkstra_path_length(graph, origen, intermedio, weight='weight')
                r2 = nx.dijkstra_path(graph, intermedio, destino, weight='weight')
                d2 = nx.dijkstra_path_length(graph, intermedio, destino, weight='weight')
                ruta = r1 + r2[1:]
                distancia = d1 + d2

        elif modo == 'obstaculo':
            if id_intermedio:
                obstaculo = LUGARES[int(id_intermedio)]
                if graph.has_node(obstaculo):
                    graph.remove_node(obstaculo)
                ruta = nx.dijkstra_path(graph, origen, destino, weight='weight')
                distancia = nx.dijkstra_path_length(graph, origen, destino, weight='weight')

        return jsonify({'success': True, 'ruta': ruta, 'distancia': round(distancia, 3)})

    except nx.NetworkXNoPath:
        return jsonify({'success': False, 'message': 'No hay ruta posible.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)