import time
import os
from DataStructures.List import array_list as lt
from DataStructures.Stack import stack as st
from DataStructures.Queue import queue as q
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Map import map_separate_chaining as sp
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Priority_queue import priority_queue  as pq
import csv
import math 
from datetime import datetime

csv.field_size_limit(2147483647)


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        "flights": pq.new_heap(is_min_pq=True)  
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    start_time = get_time()
    filepath = os.path.join("Data", filename)

    with open(filepath, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for flight in reader:
            # Procesar cada registro
            flight_data = {
                "id": flight.get("id", "Unknown"),
                "date": flight.get("date", "Unknown"),
                "dep_time": flight.get("dep_time", "Unknown"),
                "sched_dep_time": flight.get("sched_dep_time", "Unknown"),
                "arr_time": flight.get("arr_time", "Unknown"),
                "sched_arr_time": flight.get("sched_arr_time", "Unknown"),
                "carrier": flight.get("carrier", "Unknown"),
                "flight": flight.get("flight", "Unknown"),
                "tailnum": flight.get("tailnum", "Unknown"),
                "origin": flight.get("origin", "Unknown"),
                "dest": flight.get("dest", "Unknown"),
                "air_time": flight.get("air_time", "Unknown"),
                "distance": flight.get("distance", "Unknown"),
                "name": flight.get("name", "Unknown")
            }

            
            try:
                sched_datetime = datetime.strptime(
                    f"{flight_data['date']} {flight_data['sched_dep_time']}", "%Y-%m-%d %H:%M"
                )
            except Exception:
                sched_datetime = datetime.max  # Unknown / error => ponerlo al final

            pq.insert(catalog["flights"], sched_datetime, flight_data)

    end_time = get_time()
    elapsed = delta_time(start_time, end_time)
    total_flights = pq.size(catalog["flights"])

    first_5 = get_first_flights(catalog, 5)
    last_5 = get_last_flights(catalog, 5)

    return {
        "time_ms": elapsed,
        "total_flights": total_flights,
        "first_5": first_5,
        "last_5": last_5,
    }


def get_first_flights(catalog, n):
    """
    Retorna los primeros N vuelos por orden de salida programada (menor prioridad).
    """
    # Clonar heap para no alterar el original
    temp_heap = clone_heap(catalog["flights"])
    flights = []
    count = 0

    while count < n and not pq.is_empty(temp_heap):
        flight = pq.remove(temp_heap)
        flights.append(flight)
        count += 1

    return flights


def get_last_flights(catalog, n):
    """
    Retorna los últimos N vuelos por orden cronológico (mayor prioridad).
    """
    # Extraer todos para ordenarlos por prioridad inversa
    temp_heap = clone_heap(catalog["flights"])
    all_flights = []

    while not pq.is_empty(temp_heap):
        all_flights.append(pq.remove(temp_heap))

    return all_flights[-n:] if len(all_flights) >= n else all_flights


def clone_heap(heap):
    """Copia  del heap."""
    new_h = pq.new_heap(is_min_pq=True)
    for i in range(1, heap["size"] + 1):
        elem = heap["elements"]["elements"][i]
        if elem:
            pq.insert(new_h, elem["priority"], elem["value"])
    return new_h

def inorden(nodo, lista):
    if nodo is not None:
        inorden(nodo["left"], lista)
        lt.add_last(lista, nodo["value"])
        inorden(nodo["right"], lista)


def req_1(catalog, carrier_code, delay_range):

    #Función para convertir a minutos.
    def hours_to_minutes(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    #Función para calcular la diferencia en minutos.
    def compute_delay_minutes(sched, actual):
        
        delta = actual - sched
        
        #El vuelo se adelantó cruzando la medianoche

        if delta <= -720:
            delta += 1440
            
        # El vuelo se retrasó cruzando la medianoche
        elif delta > 720:
            delta -= 1440
            
        return delta
    
    start_time = time.perf_counter()
    tree = bst.new_map()
    
    flight_nodes = catalog['flights']['elements']['elements']
    min_delay, max_delay = delay_range
    
    for i in range(1, pq.size(catalog['flights']) + 1):
        node = flight_nodes[i]
        flight = node["value"]

        #Se filtra por el código de la aerolínea
        if flight.get("carrier") == carrier_code:
            
            #Se obtienen y convierten los tiempos a minutos
            sched_minutes = hours_to_minutes(flight.get("sched_dep_time"))
            actual_minutes = hours_to_minutes(flight.get("dep_time"))
            
            #Se calcula el retraso
            delay = compute_delay_minutes(sched_minutes, actual_minutes)
            
            if delay is not None:
                
                #Se filtra por el rango de minutos de retraso
                if min_delay <= delay <= max_delay:
                    
                    sort_key = (delay, flight["date"], actual_minutes)

                    #Se crea el diccionario con los datos solicitados para la respuesta
                    flight_result_info = {
                        "ID del vuelo": flight.get("id"),
                        "Código del vuelo": flight.get("flight"),
                        "Fecha": flight.get("date"),
                        "Nombre aerolínea": flight.get("name"),
                        "Código aerolínea": flight.get("carrier"),
                        "Aeropuerto origen": flight.get("origin"),
                        "Aeropuerto destino": flight.get("dest"),
                        "Minutos de retraso": delay
                    }
                    
                    bst.put(tree, sort_key, flight_result_info)

    sorted_flights = []
    
    while not bst.is_empty(tree):
        min_key = bst.get_min(tree)
        flight_data = bst.get(tree, min_key)
        sorted_flights.append(flight_data)
        
        bst.delete_min(tree)
    
    total_found = len(sorted_flights)
    result_list = sorted_flights

    #Se aplica la regla de mostrar los 5 primeros y 5 últimos si hay más de 10
    if total_found > 10:
        first_5 = sorted_flights[:5]
        last_5 = sorted_flights[-5:]
        result_list = first_5 + last_5
        
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000

    return {
        "tiempo_ejecucion_ms": execution_time_ms,
        "total_vuelos": total_found,
        "vuelos": result_list
    }

def req_2(catalog, cod, rango):
    
    
    """
    Retorna el resultado del requerimiento 2

    """
    inicial = get_time()
    
    def hours_to_minutes(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    def compute_delay_minutes(sched, actual):
        
        delta = actual - sched

        if delta <= -720:
            delta += 1440

        elif delta > 720:
            delta -= 1440
            
        return delta
    arbol = rbt.new_map()
    ran = rango.split(",")
    rango_1, rango_2 = ran
    
    
    vuelos = catalog["flights"]["elements"]["elements"]
    
    for i in range(1, pq.size(catalog["flights"])+1):
        vuelo = vuelos[i]["value"]
        if str(vuelo["dest"]) == str(cod):
            prim = hours_to_minutes(vuelo["arr_time"])
            seg = hours_to_minutes(vuelo["sched_arr_time"])
            dif = compute_delay_minutes(seg, prim)
            key = (dif, vuelo["date"], hours_to_minutes(vuelo["arr_time"]))
            if dif <= -int(rango_1) and dif >= -int(rango_2):
                rbt.put(arbol, key, vuelo)

    lista = lt.new_list()
    inorden(arbol["root"], lista)
    
    if lt.size(lista) < 10:
        totales = lt.new_list()
        for i in range(0, lt.size(lista)):
            vuelo = lt.get_element(lista, i)
            prim = hours_to_minutes(vuelo["arr_time"])
            seg = hours_to_minutes(vuelo["sched_arr_time"])
            dif = compute_delay_minutes(seg, prim)
            data = {"id" : vuelo["id"],
                    "codigo": vuelo["flight"],
                    "fecha": vuelo["date"],
                    "aerolinea": vuelo["name"],
                    "ac": vuelo["carrier"],
                    "origen": vuelo["origin"],
                    "dest": vuelo["dest"],
                    "dif": -dif
                    }
            lt.add_last(totales, data)
        final = get_time()
        delta = delta_time(inicial, final)
        retorno = {"delta": delta,
                   "canti": lt.size(lista),
                   "datos": totales}
        
        return retorno
    else:
        totales = lt.new_list()
    
        for i in range(0, 5):
            vuelo = lt.get_element(lista, i)
            prim = hours_to_minutes(vuelo["arr_time"])
            seg = hours_to_minutes(vuelo["sched_arr_time"])
            dif = compute_delay_minutes(seg, prim)
            data = {"id" : vuelo["id"],
                    "codigo": vuelo["flight"],
                    "fecha": vuelo["date"],
                    "aerolinea": vuelo["name"],
                    "ac": vuelo["carrier"],
                    "origen": vuelo["origin"],
                    "dest": vuelo["dest"],
                    "dif": -dif
                    }
            lt.add_last(totales, data)
            
        for i in range(lt.size(lista)-5, lt.size(lista)):
        
            vuelo = lt.get_element(lista, i)
            prim = hours_to_minutes(vuelo["arr_time"])
            seg = hours_to_minutes(vuelo["sched_arr_time"])
            dif = compute_delay_minutes(seg, prim)
            data = {"id" : vuelo["id"],
                    "codigo": vuelo["flight"],
                    "fecha": vuelo["date"],
                    "aerolinea": vuelo["name"],
                    "ac": vuelo["carrier"],
                    "origen": vuelo["origin"],
                    "dest": vuelo["dest"],
                    "dif": -dif
                    }
            lt.add_last(totales, data)

        final = get_time()
        delta = delta_time(inicial, final)
        retorno = {"delta": delta,
                   "canti": lt.size(lista),
                   "datos": totales}
        
        return retorno
    

def req_3(catalog, carrier_code, dest_code, distance_range):
    """
   PARA ESTE REQUERIMIENTO USE RBT
    """
    start = get_time()

    min_dist, max_dist = distance_range

    def parse_arrival_datetime(date_str, time_str):
        try:
            return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        except Exception:
            return datetime.max

    tree = rbt.new_map()

    flights_arr = catalog["flights"]["elements"]["elements"]
    total_flights_in_heap = pq.size(catalog["flights"])

    for i in range(1, total_flights_in_heap + 1):
        node = flights_arr[i]
        if not node:
            continue
        flight = node.get("value", None)
        if not flight:
            continue

        if str(flight.get("carrier", "")).upper() != str(carrier_code).upper():
            continue

        if str(flight.get("dest", "")).upper() != str(dest_code).upper():
            continue

        try:
            dist = int(float(flight.get("distance", "0")))
        except Exception:
            continue

        if dist < min_dist or dist > max_dist:
            continue

        arr_dt = parse_arrival_datetime(flight.get("date", ""), flight.get("arr_time", ""))


        out = {
            "id": flight.get("id"),
            "code": flight.get("flight"),
            "date": flight.get("date"),
            "airline_name": flight.get("name"),
            "carrier": flight.get("carrier"),
            "origin": flight.get("origin"),
            "dest": flight.get("dest"),
            "distance": dist,
            "_arr_dt": arr_dt
        }

        unique_key = (dist, arr_dt, flight.get("id"))
        rbt.put(tree, unique_key, out)

    results = lt.new_list()

    def _inorder_collect(node):
        if node is None:
            return
        _inorder_collect(node["left"])
        lt.add_last(results, node["value"])
        _inorder_collect(node["right"])

    _inorder_collect(tree["root"])

    total = lt.size(results)

    final_list = lt.new_list()
    if total == 0:
        pass
    elif total <= 10:
        for i in range(0, total):
            lt.add_last(final_list, lt.get_element(results, i))
    else:
        for i in range(0, 5):
            lt.add_last(final_list, lt.get_element(results, i))
        for i in range(total - 5, total):
            lt.add_last(final_list, lt.get_element(results, i))

    end = get_time()

    return {
        "time_ms": delta_time(start, end),
        "total_flights": total,
        "flights": final_list
    }

def req_4(catalog, date_range, time_range_str, n):
    """
    Retorna el resultado del requerimiento 4
    """
    
    def hours_to_minutes(t):
        if not t or ":" not in t: return None
        h, m = t.split(":")
        return int(h) * 60 + int(m) if h.isdigit() and m.isdigit() else None

    start_time = time.perf_counter()
    start_date, end_date = date_range
    
    time_parts = time_range_str.split('-')
    start_tm, end_tm = (hours_to_minutes(time_parts[0]), hours_to_minutes(time_parts[1])) if len(time_parts) == 2 else (None, None)

    if start_tm is None or end_tm is None:
        return {"tiempo_ejecucion_ms": 0, "numero_total_aerolineas": n, "aerolineas": []}

    airline_stats = {}
    for i in range(1, pq.size(catalog['flights']) + 1):
        flight = catalog['flights']['elements']['elements'][i]["value"]
        flight_date, sched_time_str = flight.get("date"), flight.get("sched_dep_time")
        
        if flight_date and sched_time_str and start_date <= flight_date <= end_date:
            sched_minutes = hours_to_minutes(sched_time_str)
            if sched_minutes is not None and start_tm <= sched_minutes <= end_tm:
                carrier = flight.get("carrier")
                stats = airline_stats.setdefault(carrier, {"code": carrier, "flight_count": 0, "total_duration": 0.0, "total_distance": 0.0, "shortest_flight_info": None})
                stats["flight_count"] += 1

                air_time_str = flight.get("air_time", "").strip().replace('.', '', 1)
                if air_time_str.isdigit():
                    duration = int(float(flight.get("air_time")))
                    stats["total_duration"] += duration
                    
                    current_shortest = stats["shortest_flight_info"]
                    sched_datetime_str = flight_date + " " + sched_time_str
                    if current_shortest is None or duration < current_shortest["duration"] or (duration == current_shortest["duration"] and sched_datetime_str < current_shortest["sched_datetime"]):
                        stats["shortest_flight_info"] = {"id": flight.get("id"), "code": flight.get("flight"), "sched_datetime": sched_datetime_str, "origin": flight.get("origin"), "destination": flight.get("dest"), "duration": duration}
                
                dist_str = flight.get("distance", "").strip().replace('.', '', 1)
                if dist_str.isdigit():
                    stats["total_distance"] += int(float(flight.get("distance")))
    
    pq_rank = pq.new_heap(is_min_pq=True)
    for carrier, stats in airline_stats.items():
        pq.insert(pq_rank, (-stats["flight_count"], carrier), stats)
        
    top_airlines = []
    while not pq.is_empty(pq_rank) and len(top_airlines) < n:
        stats = pq.remove(pq_rank)
        fc = stats["flight_count"]
        top_airlines.append({
            "Código de la aerolínea": stats["code"], "Número total de vuelos": fc,
            "Duración promedio (min)": round(stats["total_duration"] / fc if fc else 0, 2),
            "Distancia promedio (millas)": round(stats["total_distance"] / fc if fc else 0, 2),
            "Vuelo con menor duración": stats["shortest_flight_info"]
        })
        
    return {"tiempo_ejecucion_ms": (time.perf_counter() - start_time) * 1000, "numero_total_aerolineas": n, "aerolineas": top_airlines}


def req_5(catalog, rango, aero, canti):
    """
    Retorna el resultado del requerimiento 5
    """
    inicial = get_time()
    
    def hours_to_minutes(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    def compute_delay_minutes(sched, actual):
        
        delta = actual - sched

        if delta <= -720:
            delta += 1440

        elif delta > 720:
            delta -= 1440
            
        return delta

    ran = rango.split(",")
    rango_1, rango_2 = ran
    rango_1 = rango_1.strip()
    rango_2 = rango_2.strip()
    
    vuelos = catalog["flights"]["elements"]["elements"]
    
    sop = {}
    
    lista = pq.new_heap(is_min_pq=True)
    
    for i in range(1, pq.size(catalog["flights"])+1):
        vuelo = vuelos[i]["value"]
        if vuelo["dest"] == aero:
            fecha_vuelo = datetime.strptime(vuelo["date"], "%Y-%m-%d")
            fecha_inicio = datetime.strptime(rango_1, "%Y-%m-%d")
            fecha_fin = datetime.strptime(rango_2, "%Y-%m-%d")

            if fecha_inicio <= fecha_vuelo <= fecha_fin:
                uno = hours_to_minutes(vuelo["arr_time"])
                dos = hours_to_minutes(vuelo["sched_arr_time"])
                puntualidad = compute_delay_minutes(dos, uno)
                
                if vuelo["name"] not in sop:
        
                    sop[vuelo["name"]] = {"identificador": vuelo["carrier"],
                                          "vuelos": 1,
                                          "duracion": float(vuelo["air_time"]),
                                          "distancia": float(vuelo["distance"]),
                                          "vuelo_largo": vuelo,
                                          "puntualidad": puntualidad
                                          }
                else:
                    sop[vuelo["name"]]["vuelos"] += 1
                    sop[vuelo["name"]]["duracion"] += float(vuelo["air_time"])
                    sop[vuelo["name"]]["distancia"] += float(vuelo["distance"])
                    sop[vuelo["name"]]["puntualidad"] += puntualidad
                    if float(vuelo["distance"]) > float(sop[vuelo["name"]]["vuelo_largo"]["distance"]):
                        sop[vuelo["name"]]["vuelo_largo"] = vuelo
                        
                
    for vue in sop.values():
        vue["distancia"] = vue["distancia"]/vue["vuelos"]
        vue["duracion"] = vue["duracion"]/vue["vuelos"]
        vue["puntualidad"] = vue["puntualidad"]/vue["vuelos"]
        vue["vuelo_largo"] = {"id": vue["vuelo_largo"]["id"],
                              "codigo": vue["vuelo_largo"]["flight"],
                              "fecha_llega": (vue["vuelo_largo"]["date"], vue["vuelo_largo"]["arr_time"]),
                              "origen": vue["vuelo_largo"]["origin"],
                              "dest": vue["vuelo_largo"]["dest"],                                      
                              "dura": vue["vuelo_largo"]["air_time"]}
   
        pq.insert(lista, (abs(vue["puntualidad"]), vue["identificador"]), vue)
    
    maxi = min(canti, pq.size(lista))
    
    ret = lt.new_list()
    for _ in range(0, maxi):
        
        reto = pq.remove(lista)
        lt.add_last(ret, reto)
    final = get_time()
    delta = delta_time(inicial, final)
    
    retorno = (delta, maxi, ret)
    return retorno

def req_6(catalog, date_range, distance_range, M):
    """
    Retorna el resultado del requerimiento 6
    """
    start = get_time()

    date_start, date_end = date_range
    min_dist, max_dist = distance_range


    def hours_to_minutes(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    def compute_delay_minutes(sched, actual):
        delta = actual - sched
        if delta <= -720:
            delta += 1440
        elif delta > 720:
            delta -= 1440
        return delta

    airlines = {}

    flights_arr = catalog["flights"]["elements"]["elements"]
    total_flights = pq.size(catalog["flights"])


    for i in range(1, total_flights + 1):

        flight = flights_arr[i]["value"]

        try:
            fdate = flight["date"]
            if not (date_start <= fdate <= date_end):
                continue
        except:
            continue

        try:
            dist = int(flight["distance"])
        except:
            continue

        if not (min_dist <= dist <= max_dist):
            continue

        try:
            sched = hours_to_minutes(flight["sched_dep_time"])
            actual = hours_to_minutes(flight["dep_time"])
        except:
            continue

        delay = compute_delay_minutes(sched, actual)
        carrier = flight["carrier"]

        if carrier not in airlines:
            airlines[carrier] = {
                "delays": [],
                "flights": [],
                "count": 0
            }

        airlines[carrier]["delays"].append(delay)
        airlines[carrier]["flights"].append(flight)
        airlines[carrier]["count"] += 1


    results = []

    for carrier, info in airlines.items():

        delays = info["delays"]
        n = len(delays)

        if n == 0:
            continue

        avg_delay = sum(delays) / n

        var = sum((d - avg_delay) ** 2 for d in delays) / n
        std_dev = math.sqrt(var)

        best_flight = None
        best_diff = float("inf")

        for flight in info["flights"]:
            d = compute_delay_minutes(
                hours_to_minutes(flight["sched_dep_time"]),
                hours_to_minutes(flight["dep_time"])
            )
            diff = abs(d - avg_delay)
            if diff < best_diff:
                best_diff = diff
                best_flight = flight

        result = {
            "carrier": carrier,
            "count": n,
            "avg_delay": avg_delay,
            "std_dev": std_dev,
            "closest_flight": {
                "id": best_flight["id"],
                "code": best_flight["flight"],
                "dep_datetime": (best_flight["date"], best_flight["dep_time"]),
                "origin": best_flight["origin"],
                "dest": best_flight["dest"]
            }
        }

        results.append(result)


    pq_results = pq.new_heap(is_min_pq=True)

    for item in results:
        key = (item["std_dev"], item["avg_delay"], item["carrier"])
        pq.insert(pq_results, key, item)

    final_list = []

    for _ in range(min(M, pq.size(pq_results))):
        extracted = pq.remove(pq_results)
        final_list.append(extracted)

    end = get_time()

    return {
        "time_ms": delta_time(start, end),
        "total_airlines": M,
        "airlines": final_list
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
