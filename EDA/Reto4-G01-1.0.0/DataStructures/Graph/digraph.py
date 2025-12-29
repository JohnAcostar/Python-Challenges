from DataStructures.Map import map_linear_probing as mlp
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Graph import vertex as v
from DataStructures.Graph import edge as e


def new_graph(order):
    num_edges = 0
    vertex = mlp.new_map(order, 0.5, prime=109345121)
    
    graph = {'vertices': vertex,
             'num_edges': num_edges}
    
    return graph

def insert_vertex(my_graph, key_u, info_u):
    
    if mlp.contains(my_graph["vertices"], key_u) == True:
        update_vertex_info(my_graph, key_u, info_u)
    else:
        vertice_n = v.new_vertex(key_u, info_u)
        mlp.put(my_graph['vertices'], key_u, vertice_n)
    
    return my_graph 
     
            
def update_vertex_info(my_graph, key_u, new_info):
    
    vertice = mlp.get(my_graph["vertices"], key_u)
    vertice["value"] = new_info
    mlp.put(my_graph["vertices"], key_u, vertice)
    
    return my_graph

def add_edge(my_graph, key_u, key_v, weight=1):
    
    if not mlp.contains(my_graph["vertices"], key_u) or not mlp.contains(my_graph["vertices"], key_v):
        raise Exception("Uno de los vértices no existe")

    vert_u = mlp.get(my_graph["vertices"], key_u)

    adj_u = vert_u["adjacents"]

    if mlp.contains(adj_u, key_v):
        edge = mlp.get(adj_u, key_v)
        edge["weight"] = weight
    else:
        new_edge = e.new_edge(key_v, weight)
        mlp.put(adj_u, key_v, new_edge)
        my_graph["num_edges"] += 1

    return my_graph


def contains_vertex(my_graph, key_u):
   return mlp.contains(my_graph["vertices"], key_u)

def order(my_graph): #Numero de nodos del grafo
    order = mlp.size(my_graph['vertices'])
    return order

def size(my_graph):
    return my_graph["num_edges"]

def degree(my_graph, llave): #Numero de arcos adyacentes al vertice 
    vertice = mlp.get(my_graph['vertices'], llave)
    degree = v.degree(vertice)
    return degree

def adjacents(my_graph, key_u):
    vertice = mlp.get(my_graph['vertices'], key_u)
    adyacentes = v.get_adjacents(vertice)
    lista = mlp.key_set(adyacentes)
    
    return lista


def vertices(my_graph):
    lista = mlp.key_set(my_graph['vertices'])
    
    return lista

def get_edge(my_graph, key_u, key_v):

    if not mlp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice u no existe")

    vertex_obj = mlp.get(my_graph["vertices"], key_u)
    adj_map = v.get_adjacents(vertex_obj)

    if not mlp.contains(adj_map, key_v):
        return None

    edge_entry = mlp.get(adj_map, key_v)
    return edge_entry


def get_vertex(my_graph, key_u):
    vert = mlp.get(my_graph["vertices"], key_u)
    
    if vert is None:
        raise Exception("El vertice no existe")
    
    return vert
    
    
def get_vertex_information(my_graph, key_u):

    if not contains_vertex(my_graph, key_u):
        raise Exception("El vertice no existe")

    vertice = mlp.get(my_graph["vertices"], key_u)

    return vertice["value"]

    