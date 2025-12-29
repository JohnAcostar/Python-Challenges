from DataStructures.Map import map_linear_probing as mlp
from DataStructures.List import array_list as al
from DataStructures.Stack import stack as st
from DataStructures.Graph import digraph as dg


def new_dfs_structure(graph, source):
    """
    Estructura de búsqueda para DFS:
    - source: vértice inicial
    - marked: mapa de visitados
    - edge_to: mapa con el predecesor de cada vértice
    """
    n = dg.order(graph)

    search = {
        "source": source,
        "marked": mlp.new_map(num_elements=n, load_factor=0.5),
        "edge_to": mlp.new_map(num_elements=n, load_factor=0.5)
    }
    return search


def dfs(graph, source):
    """
    Ejecuta DFS desde el vertice source.
    Si el vértice no existe en el grafo, retorna None.
    """
    if not dg.contains_vertex(graph, source):
        return None

    search = new_dfs_structure(graph, source)
    dfs_vertex(graph, search, source)
    return search


def dfs_vertex(graph, search, vertex):
    """
    DFS recursivo desde vertex.
    Marca vertex y explora sus adyacentes no visitados.
    """

    # Si el vértice no existe en el grafo, no seguimos
    if not dg.contains_vertex(graph, vertex):
        return

    # Si ya estaba marcado, no lo volvemos a procesar
    if mlp.contains(search["marked"], vertex):
        return

    # Marcar como visitado
    mlp.put(search["marked"], vertex, True)

    # Obtener lista de vecinos (array_list con ids de vértices)
    adj_list = dg.adjacents(graph, vertex)

    # Si no tiene vecinos, terminamos
    if adj_list is None or al.size(adj_list) == 0:
        return

    # Recorrer la array_list de vecinos
    size = al.size(adj_list)
    for i in range(size):
        adj = al.get_element(adj_list, i)
        if not mlp.contains(search["marked"], adj):
            # Guardar predecesor
            mlp.put(search["edge_to"], adj, vertex)
            dfs_vertex(graph, search, adj)


def has_path_to(search, vertex):
    """
    Indica si vertex es alcanzable desde el source.
    """
    return mlp.contains(search["marked"], vertex)


def path_to(search, vertex):
    """
    Retorna el camino desde source hasta vertex en forma de pila.
    Si no hay camino, retorna None.
    """
    if not has_path_to(search, vertex):
        return None

    path = st.new_stack()
    current = vertex

    while current != search["source"]:
        st.push(path, current)
        # mlp.get devuelve directamente el valor almacenado (el predecesor)
        current = mlp.get(search["edge_to"], current)

    st.push(path, search["source"])
    return path