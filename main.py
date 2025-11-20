import networkx as nx
import matplotlib.pyplot as plt

def grafo_base():

    G = nx.Graph()

    principal_nodes= range (1,60)

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

    G.add_Edge(24,55, weight=0.292)

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

    print("Grafo base")
    return G









    







