import time
import os
from DataStructures.List import array_list as lt
from DataStructures.Stack import stack as st
from DataStructures.Queue import queue as q
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Map import map_separate_chaining as sp
from DataStructures.List import single_linked_list as sl
import csv
import math 
from datetime import datetime

csv.field_size_limit(2147483647)



def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {}
    catalog["taxis"] = lt.new_list()
    catalog["neighborhoods"] = lt.new_list()
    
    return catalog



# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    inicial = get_time()   
    
    filename = "Data/" + filename
    
    archivo = csv.DictReader(open(filename, encoding='utf-8'))    

    for register in archivo:

        register["pickup_datetime"] = datetime.strptime(register["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        register["dropoff_datetime"] = datetime.strptime(register["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
        register["passenger_count"] = int(register["passenger_count"])
        register["trip_distance"] = float(register["trip_distance"])
        register["pickup_longitude"] = float(register["pickup_longitude"])
        register["pickup_latitude"] = float(register["pickup_latitude"])
        register["rate_code"] = int(register["rate_code"])
        register["dropoff_longitude"] = float(register["dropoff_longitude"])
        register["dropoff_latitude"] = float(register["dropoff_latitude"])
        register["payment_type"] = str(register["payment_type"])
        register["fare_amount"] = float(register["fare_amount"])
        register["extra"] = float(register["extra"])
        register["mta_tax"] = float(register["mta_tax"])
        register["tip_amount"] = float(register["tip_amount"])
        register["tolls_amount"] = float(register["tolls_amount"])
        register["improvement_surcharge"] = float(register["improvement_surcharge"])
        register["total_amount"] = float(register["total_amount"])
        
        lt.add_last(catalog["taxis"], register)
        
    filename_1 = os.path.join("Data", "nyc-neighborhoods.csv")
    
    archivo_1 = csv.DictReader(open(filename_1, encoding='utf-8'), delimiter=";")
    for register_1 in archivo_1:
        register_1["borough"] = str(register_1["borough"])
        register_1["neighborhood"] = str(register_1["neighborhood"])
        register_1["latitude"] = float(register_1["latitude"].replace(",", "."))
        register_1["longitude"] = float(register_1["longitude"].replace(",", "."))
        
        lt.add_last(catalog["neighborhoods"], register_1)
            
    
    tamano = catalog["taxis"]["size"]
    
    
    i = 0
    
    mini = lt.get_element(catalog["taxis"], 0)
    
    maxi = mini
    
    while mini["trip_distance"] <= 0.0:
        i +=1
        mini = lt.get_element(catalog["taxis"], i)
    
    for val in range(0, tamano):
        elem = lt.get_element(catalog["taxis"], val)
        if elem["trip_distance"] < mini["trip_distance"] and elem["trip_distance"] > 0.0:
            mini = elem
        elif elem["trip_distance"] > maxi["trip_distance"]:
            maxi = elem
    
    mas_corto = {"pickup": mini["pickup_datetime"], 
                 "distance": mini["trip_distance"], 
                 "total_amount":mini["total_amount"]}
    
    mas_largo = {"pickup": maxi["pickup_datetime"], 
                 "distance": maxi["trip_distance"], 
                 "total_amount": maxi["total_amount"]}
    
    primeros = []
    
    ultimos = []
    
    for num in range(0,5):
        
        elemento = lt.get_element(catalog["taxis"], num)
        
        resta = elemento["dropoff_datetime"] - elemento["pickup_datetime"]
        minutos = resta.total_seconds()/60
        
        elt = {"pickup": elemento["pickup_datetime"], 
               "dropoff": elemento["dropoff_datetime"], 
               "tiempo": minutos, 
               "distance": elemento["trip_distance"], 
               "total_amount": elemento["total_amount"]}
        primeros.append(elt)
        
        
        
    for num in range(tamano-5, tamano):
        elemento = lt.get_element(catalog["taxis"], num)
        
        resta = elemento["dropoff_datetime"] - elemento["pickup_datetime"]
        minutos = resta.total_seconds()/60
        
        elt = {"pickup": elemento["pickup_datetime"], 
               "dropoff": elemento["dropoff_datetime"], 
               "tiempo": minutos, 
               "distance": elemento["trip_distance"], 
               "total_amount": elemento["total_amount"]}
        ultimos.append(elt)

    
    final = get_time()
    total = delta_time(inicial, final)
    
    retorno = {"catalog": catalog, 
               "total": total, 
               "tamaño": tamano, 
               "mas_corto": mas_corto, 
               "mas_largo": mas_largo, 
               "primeros_5": primeros, 
               "ultimos_5": ultimos}
    
    return retorno


# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    try:
        return catalog["taxis"]["elements"][id]
    except IndexError:
        print("ID fuera de rango")
        return None


# Funciones de consulta sobre el catálogo


def req_1(catalog, hora_inicial, hora_final, muestra):
    
    inicial = get_time()
    
    hora_i = datetime.strptime(hora_inicial, "%Y-%m-%d %H:%M:%S")
    hora_f = datetime.strptime(hora_final, "%Y-%m-%d %H:%M:%S")
    viajes = catalog["taxis"]
    
    sub = lt.new_list()
    
    for n in range(lt.size(viajes)):
        elemento = lt.get_element(viajes, n)
        
        if elemento["pickup_datetime"] >= hora_i and elemento["pickup_datetime"] <= hora_f:
            lt.add_last(sub, elemento)
    

    def sort_criteria(element_1, element_2):
        return element_1["pickup_datetime"] < element_2["pickup_datetime"]
    
    ordenada = lt.quick_sort(sub, sort_criteria)
    
    primeros = lt.new_list()
    ultimos = lt.new_list()
    
    if muestra*2 < lt.size(ordenada):
        
        primeros_sub = lt.sub_list(ordenada, 0, muestra)
        ultimos_sub = lt.sub_list(ordenada, lt.size(ordenada) - muestra, muestra)
        
        for l in range(lt.size(primeros_sub)):
            
            viaje = lt.get_element(primeros_sub, l)
            
            ll = "[" + str(viaje["pickup_latitude"]) + ", " + str(viaje["pickup_longitude"]) + "]"
            ll2 = "[" + str(viaje["dropoff_latitude"]) + ", " + str(viaje["dropoff_longitude"]) + "]"
            
            info = {"pickup": viaje["pickup_datetime"],
                    "longitud_latitud": ll,
                    "dropoff": viaje["dropoff_datetime"],
                    "longitud_latitud_2": ll2,
                    "distancia": viaje["trip_distance"],
                    "costo": viaje["total_amount"]
                    }
            lt.add_last(primeros, info)
        
        for k in range(lt.size(ultimos_sub)):
            
            viaje = lt.get_element(ultimos_sub, k)
            
            ll3 = "[" + str(viaje["pickup_latitude"]) + ", " + str(viaje["pickup_longitude"]) + "]"
            ll4 = "[" + str(viaje["dropoff_latitude"]) + ", " + str(viaje["dropoff_longitude"]) + "]"
            
            info = {"pickup": viaje["pickup_datetime"],
                    "longitud_latitud": ll3,
                    "dropoff": viaje["dropoff_datetime"],
                    "longitud_latitud_2": ll4,
                    "distancia": viaje["trip_distance"],
                    "costo": viaje["total_amount"]
                    }
            lt.add_last(ultimos, info)
        
        final = get_time()
        delta = delta_time(inicial, final)
        factor = 0
        
        retorno ={"tiempo": delta,
                  "tamano": lt.size(ordenada),
                  "primeros": primeros,
                  "ultimos": ultimos,
                  "factor": factor}
    
        return retorno
            
    else:
        todos = lt.new_list()
        for y in range(lt.size(ordenada)):
            
            viaje = lt.get_element(ordenada, y)
            
            ll5 = "[" + str(viaje["pickup_latitude"]) + ", " + str(viaje["pickup_longitude"]) + "]"
            ll6 = "[" + str(viaje["dropoff_latitude"]) + ", " + str(viaje["dropoff_longitude"]) + "]"
            
            info = {"pickup": viaje["pickup_datetime"],
                    "longitud_latitud": ll5,
                    "dropoff": viaje["dropoff_datetime"],
                    "longitud_latitud_2": ll6,
                    "distancia": viaje["trip_distance"],
                    "costo": viaje["total_amount"]
                    }
            lt.add_last(todos, info)
        final = get_time()
        delta = delta_time(inicial, final)
        factor = 1
        
        retorno ={"tiempo": delta,
                  "tamano": lt.size(ordenada),
                  "todos": todos,
                  "factor": factor}
    
        return retorno


def req_2(catalog, lat_min, lat_max, sample_size):
    """
    Retorna el resultado del requerimiento 2
    """
    inicio = get_time()

    trips = catalog["taxis"]
    filtered = lt.new_list()

    for i in range(lt.size(trips)):
        trip = lt.get_element(trips, i)
        try:
            lat = float(trip["pickup_latitude"])
            lon = float(trip["pickup_longitude"])
        except Exception:
            continue
        if lat_min <= lat <= lat_max:
            lt.add_last(filtered, trip)

    total_filtered = lt.size(filtered)

    if total_filtered == 0:
        fin = get_time()
        return {
            "tiempo": delta_time(inicio, fin),
            "total_rutas": 0,
            "primeros": [],
            "ultimos": [],
            "message": "No se encontraron rutas en el rango de latitud especificado."
        }

    # Criterio de ordenamiento
    def sort_criteria(t1, t2):
        lat1, lon1 = float(t1["pickup_latitude"]), float(t1["pickup_longitude"])
        lat2, lon2 = float(t2["pickup_latitude"]), float(t2["pickup_longitude"])
        if lat1 > lat2:
            return True
        elif lat1 < lat2:
            return False
        else:
            return lon1 > lon2

    # Ordenar
    sorted_list = lt.merge_sort(filtered, sort_criteria)

    n = min(sample_size, total_filtered)
    n = min(sample_size, total_filtered)

    # Si el total de viajes es menor o igual a 2N, mostrar todos
    if total_filtered <= 2 * n:
        todos_fmt = []
        for t in sorted_list["elements"]:
            try:
                pickup_dt = datetime.strptime(t["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
                dropoff_dt = datetime.strptime(t["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
            except Exception:
                pickup_dt = t["pickup_datetime"]
                dropoff_dt = t["dropoff_datetime"]

            todos_fmt.append({
                "pickup_datetime": pickup_dt.strftime("%Y-%m-%d %H:%M:%S"),
                "pickup_coord": [float(t["pickup_latitude"]), float(t["pickup_longitude"])],
                "dropoff_datetime": dropoff_dt.strftime("%Y-%m-%d %H:%M:%S"),
                "dropoff_coord": [float(t["dropoff_latitude"]), float(t["dropoff_longitude"])],
                "trip_distance": float(t["trip_distance"]),
                "total_amount": float(t["total_amount"])
            })

        fin = get_time()
        return {
            "tiempo": delta_time(inicio, fin),
            "total_rutas": total_filtered,
            "factor": 1,
            "todos": todos_fmt
        }

    primeros = lt.sub_list(sorted_list, 0, n)["elements"]
    ultimos = lt.sub_list(sorted_list, max(0, total_filtered - n), n)["elements"]

    def format_trip(t):
        try:
            pickup_dt = datetime.strptime(t["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
            dropoff_dt = datetime.strptime(t["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
        except Exception:
            pickup_dt = t["pickup_datetime"]
            dropoff_dt = t["dropoff_datetime"]
        return {
            "pickup_datetime": pickup_dt.strftime("%Y-%m-%d %H:%M:%S"),
            "pickup_coord": [float(t["pickup_latitude"]), float(t["pickup_longitude"])],
            "dropoff_datetime": dropoff_dt.strftime("%Y-%m-%d %H:%M:%S"),
            "dropoff_coord": [float(t["dropoff_latitude"]), float(t["dropoff_longitude"])],
            "trip_distance": float(t["trip_distance"]),
            "total_amount": float(t["total_amount"])
        }

    primeros_fmt = [format_trip(t) for t in primeros]
    ultimos_fmt = [format_trip(t) for t in ultimos]

    fin = get_time()
    tiempo_total = delta_time(inicio, fin)

    return {
        "tiempo": tiempo_total,
        "total_rutas": total_filtered,
        "factor": 0,
        "primeros": primeros_fmt,
        "ultimos": ultimos_fmt
    }

def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    pass


def req_4(catalog, completion_date, time_filter, reference_time, n):
    """
    Retorna el resultado del requerimiento 4

    """
    inicio = get_time()

    trips = catalog["taxis"]

    # Crear tabla hash con fecha de terminación como llave
    trips_by_date = mp.new_map(20000, 0.5)

    for i in range(lt.size(trips)):
        trip = lt.get_element(trips, i)
        dropoff_dt = trip["dropoff_datetime"]
        date_key = dropoff_dt.strftime("%Y-%m-%d")

        if mp.contains(trips_by_date, date_key):
            date_list = mp.get(trips_by_date, date_key)
            lt.add_last(date_list, trip)
        else:
            new_list = lt.new_list()
            lt.add_last(new_list, trip)
            mp.put(trips_by_date, date_key, new_list)

    trips_for_date = mp.get(trips_by_date, completion_date)
    if trips_for_date is None or lt.size(trips_for_date) == 0:
        fin = get_time()
        return {
            "tiempo": delta_time(inicio, fin),
            "total_rutas": 0,
            "primeros": [],
            "ultimos": [],
            "message": "No trips found for that completion date."
        }

    ref_time = datetime.strptime(reference_time, "%H:%M:%S").time()
    filtered = lt.new_list()

    for i in range(lt.size(trips_for_date)):
        trip = lt.get_element(trips_for_date, i)
        dropoff_time = trip["dropoff_datetime"].time()

        if time_filter.upper() == "ANTES" and dropoff_time < ref_time:
            lt.add_last(filtered, trip)
        elif time_filter.upper() == "DESPUES" and dropoff_time > ref_time:
            lt.add_last(filtered, trip)

    total_filtered = lt.size(filtered)
    if total_filtered == 0:
        fin = get_time()
        return {
            "tiempo": delta_time(inicio, fin),
            "total_rutas": 0,
            "primeros": [],
            "ultimos": [],
            "message": "No trips matched the time filter."
        }

    # Ordenar de más reciente a más antiguo
    def sort_criteria(t1, t2):
        return t1["dropoff_datetime"] > t2["dropoff_datetime"]

    sorted_list = lt.merge_sort(filtered, sort_criteria)

    # Si hay menos de 2N, mostrar todos
    if total_filtered <= 2 * n:
        todos_fmt = [
            {
                "pickup_datetime": t["pickup_datetime"].strftime("%Y-%m-%d %H:%M:%S"),
                "pickup_coord": [float(t["pickup_latitude"]), float(t["pickup_longitude"])],
                "dropoff_datetime": t["dropoff_datetime"].strftime("%Y-%m-%d %H:%M:%S"),
                "dropoff_coord": [float(t["dropoff_latitude"]), float(t["dropoff_longitude"])],
                "trip_distance": float(t["trip_distance"]),
                "total_amount": float(t["total_amount"])
            }
            for t in sorted_list["elements"]
        ]
        fin = get_time()
        return {
            "tiempo": delta_time(inicio, fin),
            "total_rutas": total_filtered,
            "factor": 1,
            "todos": todos_fmt
        }

    primeros = lt.sub_list(sorted_list, 0, n)["elements"]
    ultimos = lt.sub_list(sorted_list, max(0, total_filtered - n), n)["elements"]

    def format_trip(t):
        return {
            "pickup_datetime": t["pickup_datetime"].strftime("%Y-%m-%d %H:%M:%S"),
            "pickup_coord": [float(t["pickup_latitude"]), float(t["pickup_longitude"])],
            "dropoff_datetime": t["dropoff_datetime"].strftime("%Y-%m-%d %H:%M:%S"),
            "dropoff_coord": [float(t["dropoff_latitude"]), float(t["dropoff_longitude"])],
            "trip_distance": float(t["trip_distance"]),
            "total_amount": float(t["total_amount"])
        }

    primeros_fmt = [format_trip(t) for t in primeros]
    ultimos_fmt = [format_trip(t) for t in ultimos]

    fin = get_time()
    tiempo_total = delta_time(inicio, fin)

    return {
        "tiempo": tiempo_total,
        "total_rutas": total_filtered,
        "factor": 0,
        "primeros": primeros_fmt,
        "ultimos": ultimos_fmt
    }


def req_5(catalog, fecha, muestra):
    """
    Retorna el resultado del requerimiento 5
    """
    inicial = get_time()
    
    fecha = datetime.strptime(fecha, "%Y-%m-%d %H")
    
    hash = mp.new_map(num_elements=1000, load_factor=0.5)
    
    viajes = catalog["taxis"]
    
    for i in range(lt.size(viajes)):
        viaje = lt.get_element(viajes, i)
        fecha_viaje = viaje["dropoff_datetime"].strftime("%Y-%m-%d %H")
        if mp.contains(hash, fecha_viaje):
            contenedor = mp.get(hash, fecha_viaje)
            lt.add_last(contenedor, viaje)
        else:
            lista_viaje = lt.new_list()
            lt.add_last(lista_viaje, viaje)
            mp.put(hash, fecha_viaje, lista_viaje)
    
    if mp.contains(hash, fecha.strftime("%Y-%m-%d %H")):    
        rango = mp.get(hash, fecha.strftime("%Y-%m-%d %H"))
    else:
        raise RuntimeError("No hay viajes en la fecha y hora especificada.")
    
    ordenada = lt.merge_sort(rango, lambda t1, t2: t1["dropoff_datetime"] < t2["dropoff_datetime"])
    
    if lt.size(ordenada) >= 2 * muestra:
        primeros = lt.new_list()
        ultimos = lt.new_list()

        primeros_sub = lt.sub_list(ordenada, 0, muestra)
        ultimos_sub = lt.sub_list(ordenada, lt.size(ordenada) - muestra, muestra)
        
        for l in range(lt.size(primeros_sub)):
            
            viaje = lt.get_element(primeros_sub, l)
            
            ll = "[" + str(viaje["pickup_latitude"]) + ", " + str(viaje["pickup_longitude"]) + "]"
            ll2 = "[" + str(viaje["dropoff_latitude"]) + ", " + str(viaje["dropoff_longitude"]) + "]"
            
            info = {"pickup": viaje["pickup_datetime"],
                    "longitud_latitud": ll,
                    "dropoff": viaje["dropoff_datetime"],
                    "longitud_latitud_2": ll2,
                    "distancia": viaje["trip_distance"],
                    "costo": viaje["total_amount"]
                    }
            lt.add_last(primeros, info)
        
        for k in range(lt.size(ultimos_sub)):
            
            viaje = lt.get_element(ultimos_sub, k)
            
            ll3 = "[" + str(viaje["pickup_latitude"]) + ", " + str(viaje["pickup_longitude"]) + "]"
            ll4 = "[" + str(viaje["dropoff_latitude"]) + ", " + str(viaje["dropoff_longitude"]) + "]"
            
            info = {"pickup": viaje["pickup_datetime"],
                    "longitud_latitud": ll3,
                    "dropoff": viaje["dropoff_datetime"],
                    "longitud_latitud_2": ll4,
                    "distancia": viaje["trip_distance"],
                    "costo": viaje["total_amount"]
                    }
            lt.add_last(ultimos, info)
        
        final = get_time()
        delta = delta_time(inicial, final)
        factor = 0
        
        retorno ={"tiempo": delta,
                  "tamano": lt.size(ordenada),
                  "primeros": primeros,
                  "ultimos": ultimos,
                  "factor": factor}
    
        return retorno
            
    else:
        todos = lt.new_list()
        for y in range(lt.size(ordenada)):
            
            viaje = lt.get_element(ordenada, y)
            
            ll5 = "[" + str(viaje["pickup_latitude"]) + ", " + str(viaje["pickup_longitude"]) + "]"
            ll6 = "[" + str(viaje["dropoff_latitude"]) + ", " + str(viaje["dropoff_longitude"]) + "]"
            
            info = {"pickup": viaje["pickup_datetime"],
                    "longitud_latitud": ll5,
                    "dropoff": viaje["dropoff_datetime"],
                    "longitud_latitud_2": ll6,
                    "distancia": viaje["trip_distance"],
                    "costo": viaje["total_amount"]
                    }
            lt.add_last(todos, info)
        final = get_time()
        delta = delta_time(inicial, final)
        factor = 1
        
        retorno ={"tiempo": delta,
                  "tamano": lt.size(ordenada),
                  "todos": todos,
                  "factor": factor}
    
        return retorno

def req_6(catalog, pickup_neighborhood, start_hour, end_hour, sample_size):
    """
    Retorna el resultado del requerimiento 6
    """

    # Inicio del conteo de tiempo
    start_time = float(time.perf_counter() * 1000)
    
    barrios_list = catalog["neighborhoods"]

    # Usar la funcion haversine en millas
    def haversine(lat1, lon1, lat2, lon2):
        R = 3959  
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        a = math.sin(dphi/2.0)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2.0)**2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return R * c

    # Funcion para encontrar el vecindario/barrio mas cercano
    def nearest_neighborhood(lat, lon):
        if lt.size(barrios_list) == 0:
            return None
        best = None
        best_dist = float("inf")
        for j in range(lt.size(barrios_list)):
            nb = lt.get_element(barrios_list, j)
            try:
                nb_lat = float(nb["latitude"])
                nb_lon = float(nb["longitude"])
            except Exception:
                continue
            d = haversine(lat, lon, nb_lat, nb_lon)
            if d < best_dist:
                best_dist = d
                best = nb.get("neighborhood")
        return best

    taxis = catalog.get("taxis")
    neighborhoods = catalog.get("neighborhoods")

    if taxis is None or neighborhoods is None:
        end_time = float(time.perf_counter() * 1000)
        return {
            "tiempo": end_time - start_time,
            "total_rutas": 0,
            "primeros": [],
            "ultimos": [],
            "message": "Catálogo incompleto."
        }

    # Validar formato de hora
    try:
        h_start = int(str(start_hour).zfill(2))
        h_end = int(str(end_hour).zfill(2))
    except ValueError:
        end_time = float(time.perf_counter() * 1000)
        return {
            "tiempo": end_time - start_time,
            "total_rutas": 0,
            "primeros": [],
            "ultimos": [],
            "message": "Formato de hora inválido. Use 'HH' (ej: '09')."
        }

    # Crear tabla hash de barrios 
    trips_by_neigh = mp.new_map(3000, 0.5)

    # Asignar cada viaje al barrio más cercano de pickup
    for i in range(lt.size(taxis)):
        trip = lt.get_element(taxis, i)

        try:
            plat = float(trip["pickup_latitude"])
            plon = float(trip["pickup_longitude"])
        except Exception:
            continue

        nearest_neigh = nearest_neighborhood(plat, plon)
        if nearest_neigh is None:
            continue

        existing = mp.get(trips_by_neigh, nearest_neigh)
        if existing is None:
            new_list = lt.new_list()
            lt.add_last(new_list, trip)
            mp.put(trips_by_neigh, nearest_neigh, new_list)
        else:
            lt.add_last(existing, trip)

    # Buscar el barrio 
    trips_for_neigh = mp.get(trips_by_neigh, pickup_neighborhood)
    if trips_for_neigh is None or lt.size(trips_for_neigh) == 0:
        end_time = float(time.perf_counter() * 1000)
        return {
            "tiempo": end_time - start_time,
            "total_rutas": 0,
            "primeros": [],
            "ultimos": [],
            "message": f"No se encontraron viajes para el barrio '{pickup_neighborhood}'."
        }

    # Filtrar por hora de pickup
    filtered = lt.new_list()
    for i in range(lt.size(trips_for_neigh)):
        trip = lt.get_element(trips_for_neigh, i)
        try:
            pdt = trip["pickup_datetime"]
            if isinstance(pdt, str):
                pdt = datetime.strptime(pdt, "%Y-%m-%d %H:%M:%S")
            hour = pdt.hour
        except Exception:
            continue

        if h_start <= hour <= h_end:
            lt.add_last(filtered, trip)

    total_filtered = lt.size(filtered)
    if total_filtered == 0:
        end_time = float(time.perf_counter() * 1000)
        return {
            "tiempo": end_time - start_time,
            "total_rutas": 0,
            "primeros": [],
            "ultimos": [],
            "message": "No se encontraron viajes que cumplan el filtro de hora."
        }

    # Ordenar por pickup_datetime 
    def sort_criteria(t1, t2):
        return t1["pickup_datetime"] < t2["pickup_datetime"]

    sorted_list = lt.merge_sort(filtered, sort_criteria)

    def format_trip(trip):
        try:
            pickup_dt = datetime.strptime(trip["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        except Exception:
            pickup_dt = trip["pickup_datetime"]
        try:
            dropoff_dt = datetime.strptime(trip["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
        except Exception:
            dropoff_dt = trip["dropoff_datetime"]
        return {
            "pickup_datetime": pickup_dt.strftime("%Y-%m-%d %H:%M:%S"),
            "pickup_coord": [float(trip["pickup_latitude"]), float(trip["pickup_longitude"])],
            "dropoff_datetime": dropoff_dt.strftime("%Y-%m-%d %H:%M:%S"),
            "dropoff_coord": [float(trip["dropoff_latitude"]), float(trip["dropoff_longitude"])],
            "trip_distance": float(trip["trip_distance"]),
            "total_amount": float(trip["total_amount"])
        }

    # Si hay menos de 2N resultados, mostrar todos
    if total_filtered < 2 * sample_size:
        all_fmt = [format_trip(lt.get_element(sorted_list, i)) for i in range(lt.size(sorted_list))]
        end_time = float(time.perf_counter() * 1000)
        return {
            "tiempo": end_time - start_time,
            "total_rutas": total_filtered,
            "primeros": all_fmt,
            "ultimos": [],
            "message": f"Solo se encontraron {total_filtered} viajes (< 2N)."
        }

    n = min(sample_size, total_filtered)
    primeros = lt.sub_list(sorted_list, 0, n)["elements"]
    ultimos = lt.sub_list(sorted_list, max(0, total_filtered - n), n)["elements"]

    primeros_fmt = [format_trip(t) for t in primeros]
    ultimos_fmt = [format_trip(t) for t in ultimos]

    end_time = float(time.perf_counter() * 1000)

    return {
        "tiempo": end_time - start_time,
        "total_rutas": total_filtered,
        "primeros": primeros_fmt,
        "ultimos": ultimos_fmt
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
