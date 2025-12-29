import time
import csv
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import digraph as dg
from DataStructures.Graph import dijkstra as dj
from DataStructures.Graph import bfs
from DataStructures.Graph import dfs
from DataStructures.Stack import stack as st
from DataStructures.Graph import prim_structure as prim_s

from DataStructures.Queue import queue as qu

from datetime import datetime
import math


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    eventos_estimados = 25000
    catalog = {
        "events": lt.new_list(),                 
        "nodes": lt.new_list(),                 
        "nodes_by_id": mp.new_map(eventos_estimados, 0.7),
        "event_to_node": mp.new_map(eventos_estimados, 0.7),
        "tags": mp.new_map(128, 0.7),        
        "graph_distance": dg.new_graph(eventos_estimados),
        "graph_water": dg.new_graph(eventos_estimados),
    }


    return catalog


# Funciones para la carga de datos
def encontrar_cerca(catalog, lat, lon):
    nodos = catalog["nodes"]
    best_id = None
    best_dist = 1e18

    for i in range(lt.size(nodos)):
        nd = lt.get_element(nodos, i)
        d = haversine_km(lat, lon, nd["lat"], nd["lon"])
        if d < best_dist:
            best_dist = d
            best_id = nd["id"]

    return best_id


def cmp_events_by_timestamp(e1, e2):
    return e1["timestamp"] < e2["timestamp"]

def cmp_nodos(n1, n2):

    return n1["events_count"] < n2["events_count"]


def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = phi2 - phi1
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * (2*math.atan2(math.sqrt(a), math.sqrt(1-a)))


def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    
    inicial = get_time()
    ruta = "Data/" + filename

    g_dist = catalog["graph_distance"]
    g_water = catalog["graph_water"]
    eventos = catalog["events"]
    nodos = catalog["nodes"]
    nodos_id = catalog["nodes_by_id"]
    ev_to_node = catalog["event_to_node"]
    tags = catalog["tags"]


    # 1) LECTURA


    with open(ruta, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            e_id = row["event-id"]

            lat = float(row["location-lat"])
            lon = float(row["location-long"])
            t = datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S.%f")

            c = row["comments"]
            if c == "":
                dist_agua_km = 0.0
            else:
                dist_agua_km = float(c) / 1000.0

            tg = row["tag-local-identifier"]
            if tg.isdigit():
                tg = int(tg)

            ev = {
                "event-id": e_id,
                "lat": lat,
                "lon": lon,
                "timestamp": t,
                "dist_agua_km": dist_agua_km,
                "tag": tg
            }

            lt.add_last(eventos, ev)

            if not mp.contains(tags, tg):
                mp.put(tags, tg, True)

    total_ev = lt.size(eventos)

    # 2) ORDENAR


    if total_ev > 1:
        eventos = lt.merge_sort(eventos, cmp_events_by_timestamp)
        catalog["events"] = eventos


    # 3) AGRUPAR EVENTOS EN NODOS


    for i in range(total_ev):

        ev = lt.get_element(eventos, i)

        e_id = ev["event-id"]
        lat = ev["lat"]
        lon = ev["lon"]
        t = ev["timestamp"]
        d_agua = ev["dist_agua_km"]
        tg = ev["tag"]

        nodo_exist = None

        # buscar si cae en nodo existente
        for j in range(lt.size(nodos)):
            nd = lt.get_element(nodos, j)

            dt_h = abs((t - nd["creation_timestamp"]).total_seconds()) / 3600.0
            d_km = haversine_km(nd["lat"], nd["lon"], lat, lon)

            if d_km < 3.0 and dt_h < 3.0:
                nodo_exist = nd
                break

        # nodo YA EXISTE
        if nodo_exist is not None:

            lt.add_last(nodo_exist["events"], ev)
            nodo_exist["events_count"] += 1

            # agregar tag si no existe
            tl = nodo_exist["tags"]
            encontrado = False
            for k in range(lt.size(tl)):
                if lt.get_element(tl, k) == tg:
                    encontrado = True
                    break
            if not encontrado:
                lt.add_last(tl, tg)

            # actualizar promedio agua
            c = nodo_exist["events_count"]
            old = nodo_exist["prom_distancia_agua"]
            nodo_exist["prom_distancia_agua"] = (old * (c - 1) + d_agua) / c

            mp.put(ev_to_node, e_id, nodo_exist["id"])

        # nodo NUEVO
        else:
            nd_id = e_id

            nd = {
                "id": nd_id,
                "lat": lat,
                "lon": lon,
                "creation_timestamp": t,
                "tags": lt.new_list(),
                "events": lt.new_list(),
                "events_count": 1,
                "prom_distancia_agua": d_agua
            }

            lt.add_last(nd["events"], ev)
            lt.add_last(nd["tags"], tg)

            lt.add_last(nodos, nd)
            mp.put(nodos_id, nd_id, nd)

            dg.insert_vertex(g_dist, nd_id, nd)
            dg.insert_vertex(g_water, nd_id, nd)

            mp.put(ev_to_node, e_id, nd_id)


    # 4) CONSTRUIR MAPA DE ARCOS


    last_by_tag = mp.new_map(mp.size(tags) + 1, 0.7)
    dist_map = mp.new_map(lt.size(nodos) + 1, 0.7)
    water_map = mp.new_map(lt.size(nodos) + 1, 0.7)

    for i in range(total_ev):

        ev = lt.get_element(eventos, i)
        tg = ev["tag"]
        eid = ev["event-id"]

        nd_id = mp.get(ev_to_node, eid)
        prev = mp.get(last_by_tag, tg)

        if prev is None:
            mp.put(last_by_tag, tg, nd_id)
            continue

        if nd_id != prev:

            nd_prev = mp.get(nodos_id, prev)
            nd_act = mp.get(nodos_id, nd_id)

            d_km = haversine_km(
                nd_prev["lat"], nd_prev["lon"],
                nd_act["lat"], nd_act["lon"]
            )

            # distancia
            sub = mp.get(dist_map, prev)
            if sub is None:
                sub = mp.new_map(4, 0.7)
                mp.put(dist_map, prev, sub)

            agg = mp.get(sub, nd_id)
            if agg is None:
                agg = {"sum": 0.0, "count": 0}

            agg["sum"] += d_km
            agg["count"] += 1
            mp.put(sub, nd_id, agg)

            # agua
            a = nd_act["prom_distancia_agua"]

            sub_h = mp.get(water_map, prev)
            if sub_h is None:
                sub_h = mp.new_map(4, 0.7)
                mp.put(water_map, prev, sub_h)

            agg_h = mp.get(sub_h, nd_id)
            if agg_h is None:
                agg_h = {"sum": 0.0, "count": 0}

            agg_h["sum"] += a
            agg_h["count"] += 1
            mp.put(sub_h, nd_id, agg_h)

        mp.put(last_by_tag, tg, nd_id)


    # 5) INSERTAR ARCOS EN GRAFOS


    ks_u = mp.key_set(dist_map)
    for i in range(lt.size(ks_u)):
        u = lt.get_element(ks_u, i)
        sub = mp.get(dist_map, u)
        ks_v = mp.key_set(sub)
        for j in range(lt.size(ks_v)):
            v = lt.get_element(ks_v, j)
            agg = mp.get(sub, v)
            peso = agg["sum"] / agg["count"]
            dg.add_edge(g_dist, u, v, peso)

    ks_u = mp.key_set(water_map)
    for i in range(lt.size(ks_u)):
        u = lt.get_element(ks_u, i)
        sub = mp.get(water_map, u)
        ks_v = mp.key_set(sub)
        for j in range(lt.size(ks_v)):
            v = lt.get_element(ks_v, j)
            agg = mp.get(sub, v)
            peso = agg["sum"] / agg["count"]
            dg.add_edge(g_water, u, v, peso)


    # 6) RESUMEN Y RETORNO

    total_tags = mp.size(tags)
    total_nodos = lt.size(nodos)

    # primeros 5 nodos
    primeros_5 = lt.new_list()
    lim = 5 if total_nodos >= 5 else total_nodos
    for i in range(lim):
        lt.add_last(primeros_5, lt.get_element(nodos, i))

    # últimos 5 nodos
    ultimos_5 = lt.new_list()
    lim = 5 if total_nodos >= 5 else total_nodos
    ini = total_nodos - lim
    for i in range(ini, total_nodos):
        lt.add_last(ultimos_5, lt.get_element(nodos, i))

    # arcos
    total_arcos_dist = dg.size(g_dist)

    total_arcos_water = dg.size(g_water)


    final = get_time()
    tiempo = delta_time(inicial, final)

    return (
        catalog,
        tiempo,
        total_tags,
        total_ev,
        total_nodos,
        total_arcos_dist,
        total_arcos_water,
        primeros_5,
        ultimos_5
    )




    
# Funciones de consulta sobre el catálogo


def req_1(catalog, lat_origen, lon_origen, lat_destino, lon_destino, tag_objetivo):
    """
    Requerimiento 1 usando DFS sobre el grafo de fuentes hídricas
    """

    inicial = get_time()

    g = catalog["graph_water"]
    nodos_id = catalog["nodes_by_id"]

    origen = encontrar_cerca(catalog, lat_origen, lon_origen)
    destino = encontrar_cerca(catalog, lat_destino, lon_destino)

    if origen is None or destino is None:
        return {"error": "No se encontraron nodos cercanos"}

    search = dfs.dfs(g, origen)

    if not dfs.has_path_to(search, destino):
        return {"error": "No existe ruta entre los puntos"}

    st_path = dfs.path_to(search, destino)
    ids_camino = lt.new_list()

    while not st.is_empty(st_path):
        lt.add_last(ids_camino, st.pop(st_path))

    n = lt.size(ids_camino)
    camino = lt.new_list()
    total_dist = 0.0
    primer_nodo_tag = "Unknown"

    for i in range(n):
        vid = lt.get_element(ids_camino, i)
        nodo = mp.get(nodos_id, vid)

        tags = nodo["tags"]
        tags_total = lt.size(tags)

        prim = []
        for k in range(min(3, tags_total)):
            prim.append(lt.get_element(tags, k))

        ult = []
        for k in range(min(3, tags_total)):
            ult.append(lt.get_element(tags, tags_total - 1 - k))
        ult = ult[::-1]

        if tag_objetivo in prim or tag_objetivo in ult:
            if primer_nodo_tag == "Unknown":
                primer_nodo_tag = vid

        distancia_sig = None
        if i < n - 1:
            nxt = lt.get_element(ids_camino, i + 1)
            ar = dg.get_edge(g, vid, nxt)
            if ar is not None:
                distancia_sig = ar["weight"]
                total_dist += distancia_sig

        nodo_info = {
            "id": nodo.get("id", "Unknown"),
            "lat": nodo.get("lat", "Unknown"),
            "lon": nodo.get("lon", "Unknown"),
            "num_individuos": tags_total,
            "tags_prim": prim if prim else ["Unknown"],
            "tags_ult": ult if ult else ["Unknown"],
            "distancia_siguiente": distancia_sig
        }

        lt.add_last(camino, nodo_info)

    primeros_5 = lt.new_list()
    ultimos_5 = lt.new_list()

    lim = 5 if n >= 5 else n
    for i in range(lim):
        lt.add_last(primeros_5, lt.get_element(camino, i))

    for i in range(n - lim, n):
        lt.add_last(ultimos_5, lt.get_element(camino, i))

    final = get_time()

    return {
        "primer_nodo_individuo": primer_nodo_tag,
        "distancia_total": total_dist,
        "num_vertices": n,
        "primeros_5": primeros_5,
        "ultimos_5": ultimos_5,
        "tiempo": delta_time(inicial, final)
    }



def req_2(catalog, lat_origen, lon_origen, lat_destino, lon_destino, radio_km):
    """
    Retorna el resultado del requerimiento 2
    """
    inicial = get_time()
    g = catalog["graph_distance"]
    nodos_id = catalog["nodes_by_id"]

    origen = encontrar_cerca(catalog, lat_origen, lon_origen)
    destino = encontrar_cerca(catalog, lat_destino, lon_destino)

    if origen is None or destino is None:
        return {"error": "No se encontraron nodos cercanos"}

    search = bfs.bfs(g, origen)

    if not bfs.has_path_to(search, destino):
        return {"error": "No existe ruta entre los puntos"}

    st_path = bfs.path_to(search, destino)

    camino_ids = lt.new_list()
    while not st.is_empty(st_path):
        v = st.pop(st_path)
        lt.add_last(camino_ids, v)

    n = lt.size(camino_ids)
    camino = lt.new_list()
    total_dist = 0.0
    last_inside = None

    nd_origen = mp.get(nodos_id, origen)

    for i in range(n):
        vid = lt.get_element(camino_ids, i)
        nodo = mp.get(nodos_id, vid)
        lt.add_last(camino, nodo)

        d = haversine_km(nd_origen["lat"], nd_origen["lon"], nodo["lat"], nodo["lon"])
        if d <= radio_km:
            last_inside = nodo["id"]

        if i < n - 1:
            nxt = lt.get_element(camino_ids, i + 1)
            total_dist += dg.get_edge(g, vid, nxt)["weight"]

    primeros_5 = lt.new_list()
    ultimos_5 = lt.new_list()

    lim = 5 if n >= 5 else n
    for i in range(lim):
        lt.add_last(primeros_5, lt.get_element(camino, i))

    for i in range(n - lim, n):
        lt.add_last(ultimos_5, lt.get_element(camino, i))
        
    final = get_time()

    return {
        "ultimo_en_radio": last_inside,
        "distancia_total": total_dist,
        "num_vertices": n,
        "primeros_5": primeros_5,
        "ultimos_5": ultimos_5,
        "camino_completo": camino,
        "tiempo": delta_time(inicial, final)
    }


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    def _dfs_topo(g, u_key, visited, stack):
        """
        Ayuda recursiva para llenar la pila en post-orden inverso
        """
        mp.put(visited, u_key, True)
        
        #Obtener llaves adyacentes
        adj_iter = dg.adjacents(g, u_key) 
        
        for i in range(lt.size(adj_iter)):
            w = lt.get_element(adj_iter, i)
            if not mp.contains(visited, w):
                _dfs_topo(g, w, visited, stack)
                
        st.push(stack, u_key)
        
    inicial = get_time()
    g = catalog["graph_distance"]
    nodos_info = catalog["nodes_by_id"]
    
    #Topological sort
    visited = mp.new_map(dg.order(g), 0.7)
    pila = st.new_stack()
    vertices = dg.vertices(g)

    for i in range(lt.size(vertices)):
        u = lt.get_element(vertices, i)
        if not mp.contains(visited, u):
            _dfs_topo(g, u, visited, pila)

    #Construir Ruta y contar únicos simultáneamente
    ruta = lt.new_list()
    mapa_unicos = mp.new_map(2000, 0.7) # Mapa temporal para contar
    
    while not st.is_empty(pila):
        node_id = st.pop(pila)
        nodo = mp.get(nodos_info, node_id)
        lt.add_last(ruta, nodo)
        
        #Agregar tags de este nodo al conjunto de únicos
        mis_tags = nodo["tags"]
        for k in range(lt.size(mis_tags)):
            tag = lt.get_element(mis_tags, k)
            mp.put(mapa_unicos, tag, True)

    final = get_time()
    return {
        "ruta": ruta, 
        "total_individuos": mp.size(mapa_unicos), #Retornamos el número ya calculado
        "tiempo": delta_time(inicial, final)
    }


def req_4(catalog, lat_origen, lon_origen):
    inicial = get_time()

    g = catalog["graph_water"]
    nodos_id = catalog["nodes_by_id"]

    origen = encontrar_cerca(catalog, lat_origen, lon_origen)
    if origen is None:
        return {"error": "No se encontró un nodo cercano al origen"}

    # use prim implementation
    prim_tree = prim_s.prim(g, origen)

    # get the keys of edge_from (map_linear_probing) as an array_list
    mst_vertices = mp.key_set(prim_tree["edge_from"])
    if lt.size(mst_vertices) == 0:
        return {"error": "No existe red hídrica viable desde el origen"}

    # Build list of (vertex, dist_to) and sort by dist_to ascending
    nodes_with_dist = lt.new_list()
    for i in range(lt.size(mst_vertices)):
        v = lt.get_element(mst_vertices, i)
        dval = mp.get(prim_tree["dist_to"], v)
        if dval is None:
            dval = float("inf")
        lt.add_last(nodes_with_dist, {"id": v, "dist_to": dval})

    # sort nodes_with_dist by dist_to (merge_sort using cmp)
    def cmp_by_dist(a, b):
        return a["dist_to"] < b["dist_to"]
    try:
        nodes_with_dist = lt.merge_sort(nodes_with_dist, cmp_by_dist)
    except Exception:
        # fallback to python sort
        py = [lt.get_element(nodes_with_dist, i) for i in range(lt.size(nodes_with_dist))]
        py.sort(key=lambda x: x["dist_to"])
        nodes_with_dist = lt.new_list()
        for item in py:
            lt.add_last(nodes_with_dist, item)

    total_distance = 0.0
    total_individuals = 0
    puntos = lt.new_list()

    for i in range(lt.size(nodes_with_dist)):
        v = lt.get_element(nodes_with_dist, i)["id"]
        dist = mp.get(prim_tree["dist_to"], v)
        if dist is not None and dist != float("inf"):
            total_distance += dist

        info = mp.get(nodos_id, v)
        if info is None:
            lat = "Unknown"
            lon = "Unknown"
            tags = lt.new_list()
        else:
            lat = info.get("lat", "Unknown")
            lon = info.get("lon", "Unknown")
            tags = info.get("tags", lt.new_list())

        num_individuos = lt.size(tags)
        total_individuals += num_individuos

        prim = []
        for k in range(min(3, num_individuos)):
            prim.append(lt.get_element(tags, k))

        ult = []
        for k in range(min(3, num_individuos)):
            ult.append(lt.get_element(tags, num_individuos - 1 - k))
        ult = ult[::-1]

        punto = {
            "id": v,
            "lat": lat,
            "lon": lon,
            "num_individuos": num_individuos,
            "tags_prim": prim if prim else ["Unknown"],
            "tags_ult": ult if ult else ["Unknown"],
            "dist_to_root": dist if dist is not None else "Unknown"
        }

        lt.add_last(puntos, punto)

    total_puntos = lt.size(puntos)

    primeros_5 = lt.new_list()
    ultimos_5 = lt.new_list()
    lim = 5 if total_puntos >= 5 else total_puntos

    for i in range(lim):
        lt.add_last(primeros_5, lt.get_element(puntos, i))

    for i in range(total_puntos - lim, total_puntos):
        lt.add_last(ultimos_5, lt.get_element(puntos, i))

    final = get_time()

    return {
        "total_points": total_puntos,
        "total_individuals": total_individuals,
        "total_distance": total_distance,
        "primeros_5": primeros_5,
        "ultimos_5": ultimos_5,
        "tiempo": delta_time(inicial, final)
    }




def req_5(catalog, lat_origen, lon_origen, lat_destino, lon_destino, modo):
    """
    Requerimiento 5: ruta óptima (Dijkstra) entre dos puntos.
    """
    inicial = get_time()
    
    if modo == 1:
        g = catalog["graph_distance"]
    elif modo == 2:
        g = catalog["graph_water"]
    else:
        return {"error": "Modo inválido"}

    nodos_id = catalog["nodes_by_id"]

    origen = encontrar_cerca(catalog, lat_origen, lon_origen)
    destino = encontrar_cerca(catalog, lat_destino, lon_destino)

    if origen is None or destino is None:
        return {"error": "No se encontraron nodos cercanos"}

    # Ejecutar Dijkstra (devuelve una estructura aux)
    search = dj.dijkstra(g, origen)

    # Defensive checks
    if search is None:
        return {"error": "Dijkstra retornó None (posible vértice origen inexistente)"}
    if not isinstance(search, dict):
        return {"error": "Estructura de Dijkstra inesperada", "type": str(type(search))}

    # NOTE: has_path_to / path_to / dist_to expect (key_v, aux_structure)
    if not dj.has_path_to(destino, search):
        return {"error": "No existe ruta entre los puntos"}

    st_path = dj.path_to(destino, search)
    if st_path is None:
        return {"error": "No se pudo reconstruir la ruta (path_to devolvió None)"}

    # Convert stack path to ordered list ids_camino (origin -> dest)
    ids_camino = lt.new_list()
    while not st.is_empty(st_path):
        v = st.pop(st_path)
        lt.add_last(ids_camino, v)

    n = lt.size(ids_camino)
    camino = lt.new_list()

    for i in range(n):
        vid = lt.get_element(ids_camino, i)
        nodo = mp.get(nodos_id, vid)

        # safety fallback if node not present
        if nodo is None:
            nodo_info = {
                "id": vid,
                "lat": "Unknown",
                "lon": "Unknown",
                "num_individuos": "Unknown",
                "tags_prim": ["Unknown"],
                "tags_ult": ["Unknown"],
                "distancia_siguiente": "Unknown"
            }
            lt.add_last(camino, nodo_info)
            continue

        distancia_sig = None
        if i < n - 1:
            nxt = lt.get_element(ids_camino, i + 1)
            edge = dg.get_edge(g, vid, nxt)
            if edge is not None:
                # dg.get_edge returns an edge object; keep compatible with both {"weight":...} or entry {"value": {"weight":...}}
                if isinstance(edge, dict) and "weight" in edge:
                    distancia_sig = edge["weight"]
                else:
                    # if edge is wrapped (entry), try to access weight safely
                    try:
                        distancia_sig = edge["value"]["weight"]
                    except Exception:
                        try:
                            distancia_sig = edge["weight"]
                        except Exception:
                            distancia_sig = None

        nodo_info = {
            "id": nodo.get("id", "Unknown"),
            "lat": nodo.get("lat", "Unknown"),
            "lon": nodo.get("lon", "Unknown"),
            "num_individuos": lt.size(nodo.get("tags", lt.new_list())),
            "tags_prim": [lt.get_element(nodo["tags"], k) for k in range(min(3, lt.size(nodo.get("tags", lt.new_list()))))] if lt.size(nodo.get("tags", lt.new_list())) > 0 else ["Unknown"],
            "tags_ult": [lt.get_element(nodo["tags"], lt.size(nodo.get("tags", lt.new_list())) - 1 - k) for k in range(min(3, lt.size(nodo.get("tags", lt.new_list()))))][::-1] if lt.size(nodo.get("tags", lt.new_list())) > 0 else ["Unknown"],
            "distancia_siguiente": distancia_sig
        }

        lt.add_last(camino, nodo_info)

    # primeros y ultimos 5
    primeros_5 = lt.new_list()
    ultimos_5 = lt.new_list()
    lim = 5 if n >= 5 else n
    for i in range(lim):
        lt.add_last(primeros_5, lt.get_element(camino, i))
    for i in range(n - lim, n):
        lt.add_last(ultimos_5, lt.get_element(camino, i))

    final = get_time()
    costo_total = dj.dist_to(destino, search) if hasattr(dj, "dist_to") else "Unknown"

    return {
        "costo_total": costo_total,
        "num_vertices": n,
        "num_arcos": n - 1 if n >= 1 else 0,
        "primeros_5": primeros_5,
        "ultimos_5": ultimos_5,
        "camino_completo": camino,
        "tiempo": delta_time(inicial, final)
    }



def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    
    def _bfs_componente(g, start_node, visited, nodos_info):
        """
        Retorna una lista con todos los nodos alcanzables desde start_node
        """
        comp_nodos = lt.new_list()
        q = qu.new_queue()
        
        qu.enqueue(q, start_node)
        mp.put(visited, start_node, True)
        
        while not qu.is_empty(q):
            curr_key = qu.dequeue(q)
            #Guardamos el nodo completo en la lista de la componente
            lt.add_last(comp_nodos, mp.get(nodos_info, curr_key))
            
            adj_iter = dg.adjacents(g, curr_key)
            for i in range(lt.size(adj_iter)):
                w = lt.get_element(adj_iter, i)
                if not mp.contains(visited, w):
                    mp.put(visited, w, True)
                    qu.enqueue(q, w)
                    
        return comp_nodos
    
    def _comparar_subredes(info_a, info_b):
        """
        Ordena descendentemente por cantidad de nodos
        """
        return info_a["cantidad_nodos"] > info_b["cantidad_nodos"]

    def _procesar_subred(lista_nodos, id_num):
        """
        Recibe la lista de nodos de una componente conexa, calcula rangos, lat/lon y total de individuos únicos
        Retorna un diccionario limpio con la info
        """
        sz = lt.size(lista_nodos)
        
        #Rangos Geográficos y Tags
        min_lat, max_lat = 90.0, -90.0
        min_lon, max_lon = 180.0, -180.0
        mapa_unicos = mp.new_map(200, 0.7) #Para contar tags únicos
        
        for i in range(sz):
            nodo = lt.get_element(lista_nodos, i)
            
            #Geografía
            lat, lon = nodo['lat'], nodo['lon']
            if lat < min_lat: min_lat = lat
            if lat > max_lat: max_lat = lat
            if lon < min_lon: min_lon = lon
            if lon > max_lon: max_lon = lon
            
            #Individuos
            tags = nodo["tags"]
            for k in range(lt.size(tags)):
                t = lt.get_element(tags, k)
                mp.put(mapa_unicos, t, True)
                
        #Retornamos estructura lista para la vista
        return {
            "id": f"Subred_{id_num}",
            "nodos": lista_nodos, #Lista cruda de nodos (para sacar primeros/últimos)
            "cantidad_nodos": sz,
            "total_individuos": mp.size(mapa_unicos),
            "rango_lat": (min_lat, max_lat),
            "rango_lon": (min_lon, max_lon)
        }

    inicial = get_time()
    g = catalog["graph_water"]
    nodos_info = catalog["nodes_by_id"]
    
    visited = mp.new_map(dg.order(g), 0.7)
    lista_final = lt.new_list()
    vertices = dg.vertices(g)
    id_contador = 1
    
    #Detectar Componentes
    for i in range(lt.size(vertices)):
        u = lt.get_element(vertices, i)
        if not mp.contains(visited, u):
            #Obtener nodos con BFS
            nodos_raw = _bfs_componente(g, u, visited, nodos_info)
            
            #Procesar estadísticas
            info_subred = _procesar_subred(nodos_raw, id_contador)
            lt.add_last(lista_final, info_subred)
            id_contador += 1

    #Ordenar por tamaño
    subredes_ordenadas = lt.merge_sort(lista_final, _comparar_subredes)

    return {
        "subredes": subredes_ordenadas,
        "tiempo": delta_time(inicial, get_time())
    }

# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
