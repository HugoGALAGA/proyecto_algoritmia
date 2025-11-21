from flask import Flask, render_template, request, jsonify
import networkx as nx

app = Flask(__name__)

# DATOS (Nombre se usa internamente para el grafo, pero el usuario verá números)
LUGARES = {
    1:  {"nombre": "Centro Técnico",      "conn": [(1, 0.02), (15, 0.05)]},
    2:  {"nombre": "Colegio Anglo",       "conn": [(27, 0.08), (28, 0.11)]},
    3:  {"nombre": "CONACMI",             "conn": [(3, 0.035), (17, 0.035)]},
    4:  {"nombre": "PNC",                 "conn": [(30, 0.02), (18, 0.08)]},
    5:  {"nombre": "Parque J. Batres",    "conn": [(3, 0.09), (4, 0.02)]},
    6:  {"nombre": "La Torre",            "conn": [(20, 0.1), (19, 0.02)]},
    7:  {"nombre": "PATSY",               "conn": [(20, 0.02), (6, 0.06)]},
    8:  {"nombre": "Palacio Nacional",    "conn": [(22, 0.05), (21, 0.05)]},
    9:  {"nombre": "Plaza Constitución",  "conn": [(54, 0.13), (22, 0.16)]},
    10: {"nombre": "Pizza Hut",           "conn": [(54, 0.11), (22, 0.18)]},
    11: {"nombre": "Almacén el Cisne",    "conn": [(25, 0.05), (24, 0.1)]},
    12: {"nombre": "Mercado Central",     "conn": [(44, 0.028), (33, 0.027)]},
    13: {"nombre": "Sist. Penitenciario", "conn": [(35, 0.04), (36, 0.04)]},
    14: {"nombre": "Hotel",               "conn": [(13, 0.05), (14, 0.13)]},
    15: {"nombre": "Parque Colón",        "conn": [(47, 0.085), (46, 0.085)]},
    16: {"nombre": "Santuario Guadalupe", "conn": [(40, 0.7), (39, 0.7)]},
    17: {"nombre": "G&T",                 "conn": [(42, 0.075), (41, 0.075)]}
}

def construir_grafo():
    G = nx.DiGraph()
    
    # Calles
    G.add_weighted_edges_from([(1,2,0.2), (2,3,0.14), (3,4,0.11), (4,5,0.15), (5,6,0.12), (6,7,0.1), (7,8,0.1), (8,9,0.15), (9,10,0.16), (10,11,0.1), (11,12,0.07), (12,13,0.08), (13,14,0.18)])
    G.add_weighted_edges_from([(26,25,0.11), (25,24,0.15), (24,23,0.02), (23,22,0.15), (22,21,0.09), (21,20,0.09), (20,19,0.12), (19,18,0.15), (18,17,0.11), (17,16,0.13), (16,15,0.21)])
    G.add_weighted_edges_from([(27,28,0.19), (28,29,0.14), (29,30,0.115), (30,31,0.16), (31,32,0.12), (33,34,0.11), (34,35,0.07), (35,36,0.08), (36,37,0.17)])
    G.add_weighted_edges_from([(47,46,0.17), (46,45,0.15), (45,44,0.12), (43,42,0.13), (42,41,0.15), (41,40,0.11), (40,39,0.14), (39,38,0.22)])
    G.add_weighted_edges_from([(48,49,0.24), (49,50,0.16), (50,51,0.12), (51,52,0.141), (52,53,0.12), (53,54,0.18), (54,55,0.16), (55,56,0.15), (56,57,0.11), (57,58,0.15), (58,59,0.18)])

    # Avenidas
    avenidas = [
        (1,15,0.07), (15,1,0.07), (15,27,0.1), (27,15,0.1), (27,38,0.055), (38,27,0.055), (38,48,0.13), (48,38,0.13),
        (49,39,0.12), (39,28,0.056), (28,16,0.11), (16,2,0.08),
        (3,17,0.07), (17,29,0.1), (29,40,0.055), (40,50,0.115),
        (51,41,0.12), (41,30,0.056), (30,18,0.1), (18,4,0.09),
        (5,19,0.08), (19,31,0.1), (31,42,0.055), (42,52,0.13),
        (53,43,0.13), (53,32,0.055), (32,20,0.1), (20,6,0.08),
        (7,21,0.08), (54,22,0.29), (22,8,0.08), (9,23,0.09), (24,55,0.292),
        (56,44,0.13), (44,33,0.055), (33,25,0.1), (25,10,0.07),
        (11,26,0.08), (26,34,0.11), (34,45,0.06), (45,57,0.135),
        (12,35,0.19), (58,46,0.135), (46,36,0.06), (36,13,0.19),
        (14,37,0.2), (37,47,0.06), (47,59,0.135)
    ]
    for u, v, w in avenidas:
        G.add_edge(u, v, weight=w)

    for id_lugar, data in LUGARES.items():
        nombre = data['nombre']
        G.add_node(nombre)
        for nodo_calle, peso in data['conn']:
            G.add_edge(nombre, nodo_calle, weight=peso)
            G.add_edge(nodo_calle, nombre, weight=peso)

    return G

mapa_completo = construir_grafo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    return jsonify(LUGARES)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    try:
        id_origen = int(data.get('origen'))
        id_destino = int(data.get('destino'))
        nombre_origen = LUGARES[id_origen]['nombre']
        nombre_destino = LUGARES[id_destino]['nombre']
        
        ruta = nx.dijkstra_path(mapa_completo, nombre_origen, nombre_destino, weight='weight')
        dist = nx.dijkstra_path_length(mapa_completo, nombre_origen, nombre_destino, weight='weight')
        
        return jsonify({'success': True, 'ruta': ruta, 'distancia': round(dist, 3)})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)