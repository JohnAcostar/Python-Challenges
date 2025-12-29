from DataStructures.Map import map_linear_probing as mlp
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Graph import vertex as v
from DataStructures.Graph import edge as e
from DataStructures.Graph import digraph as dg
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s


def bfs(my_graph, source):
    graph_search = mlp.new_map(
        num_elements=dg.order(my_graph),
        load_factor=0.5,
        prime=109345121
    )

    mlp.put(graph_search, source, {
        "edge_from": None,
        "dist_to": 0,
        "marked": False
    })

    bfs_vertex(my_graph, source, graph_search)
    return graph_search


def bfs_vertex(my_graph, source, visited):
    cola = q.new_queue()
    q.enqueue(cola, source)

    while not q.is_empty(cola):
        current_vertex = q.dequeue(cola)

        adj_list = dg.adjacents(my_graph, current_vertex)

        if adj_list is not None:
                   
            for i in range(sl.size(adj_list)):
                neighbor_vertex = al.get_element(adj_list, i)

                if not mlp.contains(visited, neighbor_vertex):
                    prev_info = mlp.get(visited, current_vertex)

                    mlp.put(visited, neighbor_vertex, {
                        "edge_from": current_vertex,
                        "dist_to": prev_info["dist_to"] + 1,
                        "marked": True
                    })

                    q.enqueue(cola, neighbor_vertex)


def has_path_to(v, visited):
    return mlp.contains(visited, v)


def path_to(v, visited):
    if not mlp.contains(visited, v):
        return None

    camino = s.new_stack()

    while v is not None:
        s.push(camino, v)
        info = mlp.get(visited, v)
        v = info["edge_from"]

    return camino