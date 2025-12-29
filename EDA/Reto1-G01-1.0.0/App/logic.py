import time
import os
from DataStructures.List import array_list as lt
from DataStructures.Stack import stack as st
from DataStructures.Queue import queue as q
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


def req_1(catalog, passenger_count):
    """
    Retorna el resultado del requerimiento 1
    """
    inicio = get_time()
    trips = catalog["taxis"]

    total_trips = 0
    total_duration = total_cost = total_distance = total_tolls = total_tips = 0
    payment_counter = {}
    date_counter = {}

    # Recorrer lista con lt
    for i in range(lt.size(trips)):
        trip = lt.get_element(trips, i)
        if trip["passenger_count"] == passenger_count:
            total_trips += 1

            # Duración en minutos
            duration = (trip["dropoff_datetime"] - trip["pickup_datetime"]).total_seconds() / 60
            total_duration += duration

            # Acumular valores
            total_cost += trip["total_amount"]
            total_distance += trip["trip_distance"]
            total_tolls += trip["tolls_amount"]
            total_tips += trip["tip_amount"]

            # Contar métodos de pago
            payment = trip["payment_type"]
            payment_counter[payment] = payment_counter.get(payment, 0) + 1

            # Contar fechas en YYYY-MM-DD
            date_str = trip["pickup_datetime"].strftime("%Y-%m-%d")
            date_counter[date_str] = date_counter.get(date_str, 0) + 1

    if total_trips == 0:
        return {"message": f"No hay trayectos con {passenger_count} pasajeros."}

    # Calcular promedios
    avg_duration = total_duration / total_trips
    avg_cost = total_cost / total_trips
    avg_distance = total_distance / total_trips
    avg_tolls = total_tolls / total_trips
    avg_tips = total_tips / total_trips

    # Tipo de pago más frecuente
    most_freq_payment = max(payment_counter, key=payment_counter.get)
    most_freq_payment_str = f"{most_freq_payment} - {payment_counter[most_freq_payment]}"

    # Fecha más frecuente
    most_freq_date = max(date_counter, key=date_counter.get)

    fin = get_time()
    exec_time = delta_time(inicio, fin)

    # Retorna un diccionario con las salidas del requerimiento
    return {
    "tiempo": exec_time,
    "total_trayectos": total_trips,
    "avg_duracion": avg_duration,
    "avg_costo": avg_cost,
    "avg_distancia": avg_distance,
    "avg_peajes": avg_tolls,
    "avg_propina": avg_tips,
    "pago_frecuente": most_freq_payment_str,
    "fecha_frecuente": most_freq_date
    }

def req_2(catalog, metodo):
    """
    Retorna el resultado del requerimiento 2
    """
    inicio = get_time()
    
    met = []
    
    for pos in range(0, catalog["taxis"]["size"]):
        elemento = lt.get_element(catalog["taxis"], pos)
        if elemento["payment_type"] == metodo:
            met.append(elemento)
        
            
    tiempos = 0
    
    fechas = {}
    
    costos = 0
    
    distancias = 0
    
    peajes = 0
    
    pasajeros = {}
    
    propinas = 0
    

    
    for pos in range(0, len(met)):
        
        # primero tiempos y fechas
        
        pickup = met[pos]["pickup_datetime"]
        dropoff = met[pos]["dropoff_datetime"]
        
        duracion = dropoff - pickup 
        minutos = duracion.total_seconds() / 60
        fecha = met[pos]["dropoff_datetime"].strftime("%Y-%m-%d")
        
        tiempos += minutos
        
        if fecha in fechas:
            fechas[fecha] += 1
        else:
            fechas[fecha] = 1
        
        # segundo costos
        
        costo = met[pos]["total_amount"]
        costos += costo
        
        # tercero distancias
        
        distancia = met[pos]["trip_distance"]
        distancias += distancia
        
        # cuarto peajes
        
        peaje = met[pos]["tolls_amount"]
        peajes += peaje
        
        # quinto pasajeros
        
        pasajero = met[pos]["passenger_count"]
        if pasajero in pasajeros:
            pasajeros[pasajero] += 1
        else:
            pasajeros[pasajero] = 1
        
        # sexto propinas
        
        propina = met[pos]["tip_amount"]
        propinas += propina
    
    # tiempo promedio
        
    tiempo_promedio = tiempos/len(met)
    
    # costo promedio
    
    costo_promedio = costos/len(met)
    
    # distancia promedio
    
    distancia_promedio = distancias/len(met)
    
    # peaje promedio
    
    peaje_promedio = peajes/len(met)

    # numero de cantidad de pasajeros
    
    canti = -1
    mas = None
    
    for llave in pasajeros:
        if pasajeros[llave] > canti:
            canti = pasajeros[llave]
            mas = llave
    
    numero_pasajeros = str(mas) + " - " + str(canti)
    
    
    
    # propinas promedio
    propina_promedio = propinas/len(met)
    
    # fechas
    cantidad = -1
    fecha_mas = None
    
    for llave in fechas:
        if fechas[llave] > cantidad:
            cantidad = fechas[llave]
            fecha_mas = llave
    
    fecha_mas_frecuente = fecha_mas
    

    
            
            
    final = get_time()
    total = delta_time(inicio, final)    
    
    
    retorno = {"tiempo_ejecucion": total, 
               "total_trayectos": len(met), 
               "avg_duracion": tiempo_promedio, 
               "avg_costo":costo_promedio, 
               "avg_distancia": distancia_promedio, 
               "avg_peajes": peaje_promedio, 
               "pasajeros_frecuente": numero_pasajeros, 
               "avg_propina": propina_promedio, 
               "fecha_frecuente": fecha_mas_frecuente}
    return retorno



def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    return None


def req_4(catalog, filtro_costo, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    inicio = get_time()
    trips = catalog["taxis"]

    # Observar si las fechas ingresadas estan en el formato correcto
    try:
        fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    except Exception as e:
        fin = get_time()
        return {
            "tiempo": delta_time(inicio, fin),
            "filtro": filtro_costo,
            "total_trayectos": 0,
            "origen": None,
            "destino": None,
            "avg_distancia": 0.0,
            "avg_duracion": 0.0,
            "avg_costo": 0.0,
            "message": f"Error en las fechas: {e}"
        }

    # Haversine (millas)
    def haversine(lat1, lon1, lat2, lon2):
        R = 3959  
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        a = math.sin(dphi/2.0)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2.0)**2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return R * c

    # encontrar el barrio más cercano a coordenadas
    def find_neighborhood(lat, lon):
        neigh = catalog["neighborhoods"]
        if lt.size(neigh) == 0:
            return None
        best = None
        best_dist = float("inf")
        for j in range(lt.size(neigh)):
            nb = lt.get_element(neigh, j)
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

    combos = {}  # las diferentes combinaciones entre distintos barrios(origen, destino) 
    total_trips = 0  

    for i in range(lt.size(trips)):
        trip = lt.get_element(trips, i)

        # asegurar fecha de la recogida del trayecto
        try:
            pickup_dt = trip["pickup_datetime"]
            if isinstance(pickup_dt, datetime):
                pickup_date = pickup_dt.date()
            else:
                pickup_date = datetime.strptime(str(pickup_dt), "%Y-%m-%d %H:%M:%S").date()
        except Exception:
            continue

        if not (fecha_inicio_dt <= pickup_date <= fecha_fin_dt):
            continue

        total_trips += 1

        # coordenadas
        try:
            plat = float(trip["pickup_latitude"])
            plon = float(trip["pickup_longitude"])
            dlat = float(trip["dropoff_latitude"])
            dlon = float(trip["dropoff_longitude"])
        except Exception:
            continue

        origen = find_neighborhood(plat, plon)
        destino = find_neighborhood(dlat, dlon)

        # para combinatorias solo consideramos viajes entre barrios distintos y válidos
        if origen is None or destino is None or origen == destino:
            continue

        # duración total en minutos del recorrido/trayecto
        try:
            dur = (trip["dropoff_datetime"] - trip["pickup_datetime"]).total_seconds() / 60.0
        except Exception:
            dur = 0.0

        dist_miles = float(trip.get("trip_distance", 0.0))
        total_amount = float(trip.get("total_amount", 0.0))

        key = (origen, destino)
        if key not in combos:
            combos[key] = [0.0, 0.0, 0.0, 0]
        combos[key][0] += total_amount
        combos[key][1] += dist_miles
        combos[key][2] += dur
        combos[key][3] += 1

    fin = get_time()

    if total_trips == 0 or len(combos) == 0:
        return {
            "tiempo": delta_time(inicio, fin),
            "filtro": filtro_costo,
            "origen": None,
            "destino": None,
            "avg_distancia": 0.0,
            "avg_duracion": 0.0,
            "avg_costo": 0.0,
            "message": "No se encontraron combinaciones de barrios en el rango dado."
        }

    # calcular promedios
    resultados = []
    for (origen, destino), (s_cost, s_dist, s_dur, cnt) in combos.items():
        resultados.append({
            "origen": origen,
            "destino": destino,
            "avg_costo": s_cost / cnt,
            "avg_distancia": s_dist / cnt,
            "avg_duracion": s_dur / cnt,
            "count": cnt
        })

    # seleccionar MAYOR o MENOR
    if str(filtro_costo).strip().upper() == "MAYOR":
        elegido = max(resultados, key=lambda x: x["avg_costo"])
    else:
        elegido = min(resultados, key=lambda x: x["avg_costo"])

    fin2 = get_time()
    exec_time = delta_time(inicio, fin2)

    return {
        "tiempo": exec_time,
        "filtro": filtro_costo,
        "total_trayectos": total_trips,          
        "origen": elegido["origen"],
        "destino": elegido["destino"],
        "avg_distancia": elegido["avg_distancia"],
        "avg_duracion": elegido["avg_duracion"],
        "avg_costo": elegido["avg_costo"],
    }


def req_5(catalog, filtro, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 5
    
    """
    
    inicial = get_time()

    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()

    horas = {}
    
    trayectos_filtrados = 0

    for viaje in catalog["taxis"]["elements"]:
        pickup = viaje["pickup_datetime"].date()
        hora = viaje["pickup_datetime"].hour

        if pickup >= fecha_inicio and pickup <= fecha_fin:
            
            trayectos_filtrados += 1
            
            cost = viaje["total_amount"]
            dura = (viaje["dropoff_datetime"] - viaje["pickup_datetime"]).total_seconds() / 60
            pasa = viaje["passenger_count"]
            
            
            if hora not in horas:
                horas[hora] = {"sum_cost": 0, 
                                "sum_duracion": 0, 
                                "sum_pasajeros": 0, 
                                "count": 0,
                                "max_trip": None,
                                "min_trip": None}
                
            horas[hora]["sum_cost"] += cost
            horas[hora]["sum_duracion"] += dura
            horas[hora]["sum_pasajeros"] += pasa
            horas[hora]["count"] += 1
            
            max_trip = horas[hora]["max_trip"]
            if (max_trip is None or cost > max_trip["total_amount"] or (cost == max_trip["total_amount"] and viaje["dropoff_datetime"] > max_trip["dropoff_datetime"])):
                horas[hora]["max_trip"] = viaje


            min_trip = horas[hora]["min_trip"]
            if (min_trip is None or cost < min_trip["total_amount"] or (cost == min_trip["total_amount"] and viaje["dropoff_datetime"] > min_trip["dropoff_datetime"])):
                horas[hora]["min_trip"] = viaje
            
            
    for hora in horas:
            horas[hora]["avg_cost"] = horas[hora]["sum_cost"] / horas[hora]["count"]
            horas[hora]["avg_duracion"] = horas[hora]["sum_duracion"] / horas[hora]["count"]
            horas[hora]["avg_pasajeros"] = horas[hora]["sum_pasajeros"] / horas[hora]["count"]
            
    if filtro.upper() == "MAYOR":
        hora_seleccionada = max(horas.items(), key=lambda x: x[1]["avg_cost"])
    else:
        hora_seleccionada = min(horas.items(), key=lambda x: x[1]["avg_cost"])
    
    franja, datos = hora_seleccionada

    hora_inicio = int(franja)
    hora_fin = (hora_inicio + 1) % 24
    franja = f"[{hora_inicio:02d} - {hora_fin:02d})"

       
    final = get_time()
    total = delta_time(inicial, final)     
    
    retorno = {"tiempo": total,
            "filtro": filtro,
            "total_trayectos": trayectos_filtrados,
            "franja": franja,
            "avg_cost": datos["avg_cost"],    
            "num_trips": datos["count"],
            "avg_duracion": datos["avg_duracion"],
            "avg_pasajeros": datos["avg_pasajeros"],
            "max_trip": datos["max_trip"]["total_amount"],
            "min_trip": datos["min_trip"]["total_amount"]}
            
    
    
    return retorno

def req_6(catalog, barrio_inicio, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 6
    """
    inicio = get_time()

    # Establececer las fechas de inicio y final
    try:
        dt_start = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        dt_end = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    except Exception as e:
        fin = get_time()
        return {
            "tiempo": delta_time(inicio, fin),
            "total_trayectos": 0,
            "avg_distancia": 0.0,
            "avg_duracion": 0.0,
            "barrio_mas_visitado": None,
            "medios_pago": [],
            "message": f"Error al parsear fechas: {e}"
        }

    barrios_list = catalog["neighborhoods"]
    
    #  Usar la funcion harvesine en millas
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

    trips = catalog["taxis"]
    barrio_inicio_norm = str(barrio_inicio).strip().lower()

    # Contadores
    total_trips_fecha = 0       # viajes solo con filtro de fechas
    total_trips_barrio = 0      # viajes con filtro fecha + barrio inicio
    sum_distance = 0.0
    sum_duration = 0.0

    dest_counter = {}           # conteo de destinos
    payments = {}               # metodos de pago

    for i in range(lt.size(trips)):
        trip = lt.get_element(trips, i)

        # Fecha de inicio
        try:
            pickup_dt = trip["pickup_datetime"]
            if isinstance(pickup_dt, datetime):
                pickup_date = pickup_dt.date()
            else:
                pickup_date = datetime.strptime(str(pickup_dt), "%Y-%m-%d %H:%M:%S").date()
        except Exception:
            continue

        if not (dt_start <= pickup_date <= dt_end):
            continue

        total_trips_fecha += 1  # contar viajes en el rango de fechas

        # coordenadas
        try:
            p_lat = float(trip["pickup_latitude"])
            p_lon = float(trip["pickup_longitude"])
            d_lat = float(trip["dropoff_latitude"])
            d_lon = float(trip["dropoff_longitude"])
        except Exception:
            continue

        origin_nb = nearest_neighborhood(p_lat, p_lon)
        dest_nb = nearest_neighborhood(d_lat, d_lon)

        if origin_nb is None or dest_nb is None:
            continue

        if str(origin_nb).strip().lower() != barrio_inicio_norm:
            continue

        total_trips_barrio += 1

        # duración en minutos
        try:
            duration_min = (trip["dropoff_datetime"] - trip["pickup_datetime"]).total_seconds() / 60.0
        except Exception:
            try:
                dd = datetime.strptime(str(trip["dropoff_datetime"]), "%Y-%m-%d %H:%M:%S")
                dp = datetime.strptime(str(trip["pickup_datetime"]), "%Y-%m-%d %H:%M:%S")
                duration_min = (dd - dp).total_seconds() / 60.0
            except Exception:
                duration_min = 0.0

        try:
            dist_miles = float(trip.get("trip_distance", 0.0))
        except Exception:
            dist_miles = 0.0

        try:
            total_amount = float(trip.get("total_amount", 0.0))
        except Exception:
            total_amount = 0.0

        sum_distance += dist_miles
        sum_duration += duration_min

        # Destino más visitado
        dest_counter[dest_nb] = dest_counter.get(dest_nb, 0) + 1

        # Métodos de pago
        pay = str(trip.get("payment_type", "UNKNOWN")).strip()
        rec = payments.get(pay)

        try:
            drop_dt = trip["dropoff_datetime"]
            if not isinstance(drop_dt, datetime):
                drop_dt = datetime.strptime(str(drop_dt), "%Y-%m-%d %H:%M:%S")
        except Exception:
            drop_dt = None

        if rec is None:
            payments[pay] = {
                "count": 1,
                "sum_recaudo": total_amount,
                "sum_duration": duration_min,
                "latest_dropoff": drop_dt
            }
        else:
            rec["count"] += 1
            rec["sum_recaudo"] += total_amount
            rec["sum_duration"] += duration_min
            if drop_dt is not None:
                if rec["latest_dropoff"] is None or drop_dt > rec["latest_dropoff"]:
                    rec["latest_dropoff"] = drop_dt

    fin = get_time()
    tiempo_exec = delta_time(inicio, fin)

    # Si no hay viajes del barrio en ese rango
    if total_trips_barrio == 0:
        return {
            "tiempo": tiempo_exec,
            "total_trayectos": total_trips_fecha,  
            "avg_distancia": 0.0,
            "avg_duracion": 0.0,
            "barrio_mas_visitado": None,
            "medios_pago": [],
            "message": "No se encontraron trayectos que salieran del barrio indicado en el rango de fechas dado."
        }

    avg_distancia = sum_distance / total_trips_barrio
    avg_duracion = sum_duration / total_trips_barrio

    barrio_mas_visitado = max(dest_counter, key=dest_counter.get) if dest_counter else None

    # Procesar medios de pago
    pagos_list = []
    most_used_tipo = max(payments.items(), key=lambda x: x[1]["count"])[0] if payments else None

    most_recaudo_tipo = None
    most_recaudo_amount = -1.0
    most_recaudo_latest = None
    for tipo, agg in payments.items():
        amt = agg["sum_recaudo"]
        if amt > most_recaudo_amount:
            most_recaudo_amount = amt
            most_recaudo_tipo = tipo
            most_recaudo_latest = agg.get("latest_dropoff")
        elif amt == most_recaudo_amount:
            cand_latest = agg.get("latest_dropoff")
            if cand_latest is not None and (most_recaudo_latest is None or cand_latest > most_recaudo_latest):
                most_recaudo_tipo = tipo
                most_recaudo_latest = cand_latest

    for tipo, agg in payments.items():
        cantidad = agg["count"]
        avg_precio = agg["sum_recaudo"] / cantidad if cantidad > 0 else 0.0
        avg_tiempo = agg["sum_duration"] / cantidad if cantidad > 0 else 0.0
        pagos_list.append({
            "tipo": tipo,
            "cantidad": cantidad,
            "avg_precio": avg_precio,
            "es_mas_usado": tipo == most_used_tipo,
            "es_mayor_recaudo": tipo == most_recaudo_tipo,
            "avg_tiempo_min": avg_tiempo
        })

    pagos_list.sort(key=lambda x: x["cantidad"], reverse=True)

    return {
        "tiempo": tiempo_exec,
        "total_trayectos_fecha": total_trips_fecha,   
        "total_trayectos": total_trips_barrio,    
        "avg_distancia": avg_distancia,
        "avg_duracion": avg_duracion,
        "barrio_mas_visitado": barrio_mas_visitado,
        "medios_pago": pagos_list
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
