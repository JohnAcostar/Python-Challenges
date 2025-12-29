# prim_structure.py
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as d
from DataStructures.List import array_list as al

def new_prim_structure(source, g_order):
    structure = {
        "source": source,
        "edge_from": mp.new_map(g_order, 0.5),
        "dist_to": mp.new_map(g_order, 0.5),
        "marked": mp.new_map(g_order, 0.5),
        "pq": pq.new_heap()
    }
    return structure

def prim(grafo, origen):
    """
    Compute a Prim-style MST structure starting at 'origen'.
    Returns a dict with keys: source, edge_from (map), dist_to (map), marked (map), pq (heap).
    Edge weights are taken from digraph.get_edge(grafo, u, v)["weight"].
    """
    order = d.order(grafo)
    prim_struct = new_prim_structure(origen, order)

    # initialize maps for every vertex
    vertices = d.vertices(grafo)
    for i in range(al.size(vertices)):
        v = al.get_element(vertices, i)
        mp.put(prim_struct["dist_to"], v, float("inf"))
        mp.put(prim_struct["edge_from"], v, None)
        mp.put(prim_struct["marked"], v, False)

    mp.put(prim_struct["dist_to"], origen, 0.0)
    # insert (priority, value)
    pq.insert(prim_struct["pq"], 0.0, origen)

    while not pq.is_empty(prim_struct["pq"]):
        u = pq.remove(prim_struct["pq"])
        # if u was removed but somehow already marked, skip
        if mp.get(prim_struct["marked"], u):
            continue
        mp.put(prim_struct["marked"], u, True)

        # use public API to get adjacents
        try:
            adj_keys = d.adjacents(grafo, u)  # should return array_list of keys
        except Exception:
            adj_keys = al.new_list()

        for j in range(al.size(adj_keys)):
            v = al.get_element(adj_keys, j)
            edge = d.get_edge(grafo, u, v)
            if edge is None:
                continue
            # edge is an edge object (entry["value"]) with 'weight'
            weight = edge.get("weight", None) if isinstance(edge, dict) else None
            if weight is None:
                # try alternative structure: maybe edge is entry with ["weight"]
                try:
                    weight = edge["weight"]
                except Exception:
                    continue

            marked_v = mp.get(prim_struct["marked"], v)
            if marked_v is None:
                marked_v = False

            if not marked_v:
                dist_v = mp.get(prim_struct["dist_to"], v)
                if dist_v is None:
                    dist_v = float("inf")
                if weight < dist_v:
                    mp.put(prim_struct["dist_to"], v, weight)
                    mp.put(prim_struct["edge_from"], v, u)
                    # update pq
                    if pq.contains(prim_struct["pq"], v):
                        pq.improve_priority(prim_struct["pq"], weight, v)
                    else:
                        pq.insert(prim_struct["pq"], weight, v)

    return prim_struct
