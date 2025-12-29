import sys
from App import logic as lg
import os
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Priority_queue import priority_queue  as pq
from tabulate import tabulate

def imprimir_lista_vertices(lista_vertices):
    n = lt.size(lista_vertices)
    for i in range(n):
        nodo = lt.get_element(lista_vertices, i)
        print(f"\nVértice {i+1}:")
        print(f"  ID: {nodo.get('id', 'Unknown')}")
        print(f"  Latitud: {nodo.get('lat', 'Unknown')}")
        print(f"  Longitud: {nodo.get('lon', 'Unknown')}")
        print(f"  Número de individuos: {nodo.get('num_individuos', 'Unknown')}")

        prim = nodo.get('tags_prim', [])
        ult = nodo.get('tags_ult', [])

        if isinstance(prim, list) and len(prim) > 0:
            print(f"  Primeros tags: {prim}")
        else:
            print("  Primeros tags: []")

        if isinstance(ult, list) and len(ult) > 0:
            print(f"  Últimos tags: {ult}")
        else:
            print("  Últimos tags: []")

        dnext = nodo.get('distancia_siguiente', None)
        if isinstance(dnext, (int, float)):
            print(f"  Distancia al siguiente vértice: {dnext:.3f} km")
        elif dnext is None:
            print("  Distancia al siguiente vértice: -- (último nodo)")
        else:
            print(f"  Distancia al siguiente vértice: {dnext}")

def imprimir_tabla_req_4(lista_puntos):
    # lista_puntos is an array_list of punto dicts (id, lat, lon, num_individuos, tags_prim, tags_ult, dist_to_root)
    headers = ["ID", "Posición (lat, lon)", "Individuos", "Primeros 3 tags", "Últimos 3 tags", "Dist. a raíz (km)"]
    tabla = []
    for i in range(lt.size(lista_puntos)):
        p = lt.get_element(lista_puntos, i)
        pos = f"({p.get('lat','Unknown')}, {p.get('lon','Unknown')})"
        tabla.append([
            p.get("id", "Unknown"),
            pos,
            p.get("num_individuos", "Unknown"),
            p.get("tags_prim", ["Unknown"]),
            p.get("tags_ult", ["Unknown"]),
            p.get("dist_to_root", "Unknown")
        ])
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

def imprimir_vertices_req2(lista_vertices):
    n = lt.size(lista_vertices)

    for i in range(n):
        nodo = lt.get_element(lista_vertices, i)

        print(f"\nVértice {i+1}:")
        print(f"  ID: {nodo['id']}")
        print(f"  Latitud: {nodo['lat']}")
        print(f"  Longitud: {nodo['lon']}")
        print(f"  Número de individuos: {lt.size(nodo['tags'])}")

        tags_total = lt.size(nodo["tags"])

        prim = []
        for k in range(min(3, tags_total)):
            prim.append(lt.get_element(nodo["tags"], k))

        ult = []
        for k in range(min(3, tags_total)):
            ult.append(lt.get_element(nodo["tags"], tags_total - 1 - k))
        ult = ult[::-1]

        print(f"  Primeros tags: {prim}")
        print(f"  Últimos tags: {ult}")


def new_logic():
    """
        Se crea una instancia del controlador
    """
    return lg.new_logic()


def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos con formato tipo figura usando tabulate
    """
    filename = input("Ingrese el nombre del archivo (ej: 1000_cranes_mongolia_small.csv): ")

    print("\n==============================")
    print(" CARGA DE DATOS ")
    print("==============================\n")

    (
        catalog,
        tiempo,
        total_tags,
        total_eventos,
        total_nodos,
        total_arcos_dist,
        total_arcos_water,
        primeros_5,
        ultimos_5
    ) = lg.load_data(control, filename)

    print(f"Total de grullas reconocidas: {total_tags}")
    print(f"Total de eventos cargados: {total_eventos}")
    print(f"Total de nodos del grafo: {total_nodos}")
    print(f"Total de arcos en el grafo (distancias): {total_arcos_dist}")
    print(f"Total de arcos en el grafo (agua): {total_arcos_water}")
    print(f"Tiempo de carga: {tiempo:.3f} ms\n")

    print("==============================")
    print(" DETALLE DE NODOS (VÉRTICES)")
    print("==============================\n")

    print("carga de datos de grafo de distancias geográficas y de fuentes hídricas")
    print(f"Archivo: '{filename}'\n")
    print("--- Primeros 5 Nodos ---")

    headers = [
        "Identificador único",
        "Posición (lat, lon)",
        "Fecha de creación",
        "Grullas (tags)",
        "Conteo de eventos",
        "Dist. Hídrica Prom (km)"
    ]

    tabla_prim = []
    for i in range(lt.size(primeros_5)):
        nodo = lt.get_element(primeros_5, i)

        fila = [
            nodo["id"],
            f"({nodo['lat']:.6f}, {nodo['lon']:.6f})",
            nodo["creation_timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
            [lt.get_element(nodo["tags"], j) for j in range(lt.size(nodo["tags"]))],
            nodo["events_count"],
            round(nodo["prom_distancia_agua"], 4)
        ]
        tabla_prim.append(fila)

    print(tabulate(tabla_prim, headers=headers, tablefmt="grid"))

    print("\n--- Últimos 5 Nodos ---")

    tabla_ult = []
    for i in range(lt.size(ultimos_5)):
        nodo = lt.get_element(ultimos_5, i)

        fila = [
            nodo["id"],
            f"({nodo['lat']:.6f}, {nodo['lon']:.6f})",
            nodo["creation_timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
            [lt.get_element(nodo["tags"], j) for j in range(lt.size(nodo["tags"]))],
            nodo["events_count"],
            round(nodo["prom_distancia_agua"], 4)
        ]
        tabla_ult.append(fila)

    print(tabulate(tabla_ult, headers=headers, tablefmt="grid"))

    print(f"Archivo: '{filename}'\n")
    print(f"Total de arcos hídricos: {total_arcos_water}")

    return catalog





def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    lat_origen = float(input("Ingrese latitud del punto de origen: "))
    lon_origen = float(input("Ingrese longitud del punto de origen: "))
    lat_destino = float(input("Ingrese latitud del punto de destino: "))
    lon_destino = float(input("Ingrese longitud del punto de destino: "))
    tag = int(input("Ingrese el identificador de la grulla: "))

    resultado = lg.req_1(control, lat_origen, lon_origen, lat_destino, lon_destino, tag)

    if "error" in resultado:
        print(resultado["error"])
        return

    print("\n==== RESULTADO REQUERIMIENTO 1 ====\n")

    print(f"Primer nodo donde aparece el individuo: {resultado['primer_nodo_individuo']}")
    print(f"Distancia total del recorrido: {resultado['distancia_total']:.3f} km")
    print(f"Total de puntos del camino: {resultado['num_vertices']}")
    print(f"Tiempo de ejecución: {resultado['tiempo']:.3f} ms\n")

    print("----- Primeros 5 vértices -----")
    imprimir_lista_vertices(resultado["primeros_5"])

    print("\n----- Últimos 5 vértices -----")
    imprimir_lista_vertices(resultado["ultimos_5"])


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    
    lat_origen = float(input("Ingrese la latitud del punto de origen: "))
    lon_origen = float(input("Ingrese la longitud del punto de origen: "))
    lat_destino = float(input("Ingrese la latitud del punto de destino: "))
    lon_destino = float(input("Ingrese la longitud del punto de destino: "))
    radio_km = float(input("Ingrese el radio en km: "))
    
    resultado = lg.req_2(control, lat_origen, lon_origen, lat_destino, lon_destino, radio_km)
    
    print("\n==== RESULTADO REQUERIMIENTO 2 ====\n")

    print(f"Duración de proceso del requerimiento: {resultado['tiempo']}")
    print(f"Último nodo dentro del área: {resultado['ultimo_en_radio']}")
    print(f"Distancia total del recorrido: {resultado['distancia_total']:.3f} km")
    print(f"Total de puntos en la ruta: {resultado['num_vertices']}\n")

    print("----- Primeros 5 puntos del camino -----")
    imprimir_vertices_req2(resultado["primeros_5"])

    print("\n----- Últimos 5 puntos del camino -----")
    imprimir_vertices_req2(resultado["ultimos_5"])

    
def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    
    print("Identificando ruta migratoria...")
    res = lg.req_3(control)
    
    ruta = res["ruta"]
    total_pts = lt.size(ruta)
    
    #prints
    print("\n==== RUTA MIGRATORIA ====")
    print(f"Tiempo: {res['tiempo']:.4f} ms")
    print(f"Puntos en la ruta: {total_pts}")
    print(f"Total de grullas en la ruta: {res['total_individuos']}")
    print("-" * 30)

    #Mostrar primeros 5
    print("\n--- INICIO DE RUTA (5) ---")
    limit = 5 if total_pts > 5 else total_pts
    for i in range(limit):
        n = lt.get_element(ruta, i)
        print(f"ID: {n['id']} | Pos: ({n['lat']:.3f}, {n['lon']:.3f}) | Indiv: {n['num_individuos']}")

    #Mostrar últimos 5 si la lista es larga
    if total_pts > 5:
        print("\n--- FIN DE RUTA (5) ---")
        start = total_pts - 5
        for i in range(start, total_pts):
            n = lt.get_element(ruta, i)
            print(f"ID: {n['id']} | Pos: ({n['lat']:.3f}, {n['lon']:.3f}) | Indiv: {n['num_individuos']}")


def print_req_4(control):
    lat = float(input("Ingrese latitud del punto de origen: "))
    lon = float(input("Ingrese longitud del punto de origen: "))

    result = lg.req_4(control, lat, lon)

    if result is None or "error" in result:
        print("\nNo corredor hídrico reconocido.\n")
        if result is not None and "error" in result:
            print("Error:", result["error"])
        return

    print("\n===== REQ 4 - Estimar corredores hídricos óptimos =====")
    print("\n--- Resultados del Requerimiento 4 ---\n")

    print(f"Total de puntos en el corredor: {result['total_points']}")
    print(f"Total de individuos en el corredor: {result['total_individuals']}")
    print(f"Distancia total del corredor (km): {round(result['total_distance'], 6)}\n")

    print("Primeros 5 puntos del corredor:\n")
    imprimir_tabla_req_4(result["primeros_5"])

    print("\nÚltimos 5 puntos del corredor:\n")
    imprimir_tabla_req_4(result["ultimos_5"])

    print(f"\nTiempo de ejecución: {round(result['tiempo'], 3)} ms\n")

def print_req_5(control):
    """
    Función que imprime la solución del Requerimiento 5 en consola
    """
    
    lat_origen = float(input("Ingrese la latitud del punto de origen: "))
    lon_origen = float(input("Ingrese la longitud del punto de origen: "))
    lat_destino = float(input("Ingrese la latitud del punto de destino: "))
    lon_destino = float(input("Ingrese la longitud del punto de destino: "))
    modo = int(input("Ingrese 1 para grafo de distancias, 2 para grafo de agua: "))
    
    resultado = lg.req_5(control, lat_origen, lon_origen, lat_destino, lon_destino, modo)
    
    print("\n==== RESULTADO REQUERIMIENTO 5 ====\n")

    if "error" in resultado:
        print("Error:", resultado["error"])
        return

    print(f"Duración del proceso: {resultado.get('tiempo', 'Unknown')} ms")

    costo = resultado.get('costo_total', None)
    if isinstance(costo, (int, float)):
        print(f"Costo total del recorrido: {costo:.3f} km")
    else:
        print(f"Costo total del recorrido: {costo}")

    print(f"Total de puntos (vértices): {resultado.get('num_vertices', 'Unknown')}")
    print(f"Total de segmentos (arcos): {resultado.get('num_arcos', 'Unknown')}\n")

    print("----- Primeros 5 vértices del camino -----")
    imprimir_lista_vertices(resultado.get("primeros_5", lt.new_list()))

    print("\n----- Últimos 5 vértices del camino -----")
    imprimir_lista_vertices(resultado.get("ultimos_5", lt.new_list()))



def print_req_6(control):
    """
    Función que imprime la solución del Requerimiento 6 en consola
    """
    print("Identificando grupos hídricos aislados...")
    res = lg.req_6(control)
    
    subredes = res["subredes"]
    total = lt.size(subredes)
    
    print("\n==== SUBREDES HÍDRICAS ====")
    print(f"Tiempo: {res['tiempo']:.4f} ms")
    print(f"Total subredes encontradas: {total}")
    print("\n----- TOP 5 SUBREDES MÁS GRANDES -----\n")

    #Mostrar máximo 5
    limit = 5 if total > 5 else total
    
    for i in range(limit):
        #logic.py devuelve un diccionario "info_subred" fácil de usar
        sub = lt.get_element(subredes, i) 
        
        cant = sub["cantidad_nodos"]
        lista_n = sub["nodos"]
        lat_r = sub["rango_lat"]
        lon_r = sub["rango_lon"]

        print(f"[{sub['id']}] Tamaño: {cant} nodos | Individuos Únicos: {sub['total_individuos']}")
        print(f"   Lat: [{lat_r[0]:.4f}, {lat_r[1]:.4f}] | Lon: [{lon_r[0]:.4f}, {lon_r[1]:.4f}]")

        #Imprimir breve muestra de nodos inicio y fin de la lista de la componente
        n_inicio = lt.get_element(lista_n, 0)
        n_fin = lt.get_element(lista_n, cant - 1)
        
        print(f"   Nodo Inicio (Muestra): {n_inicio['id']} ({n_inicio['lat']:.3f}, {n_inicio['lon']:.3f})")
        print(f"   Nodo Fin    (Muestra): {n_fin['id']}    ({n_fin['lat']:.3f}, {n_fin['lon']:.3f})")
        print("-" * 40)

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
