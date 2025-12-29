import sys
import os
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Priority_queue import priority_queue  as pq
import App.logic as logic
from tabulate import tabulate

default_limit = 1000
sys.setrecursionlimit(default_limit * 10)

def new_logic():
    """
    Se crea una instancia del controlador
    """
    catalog = logic.new_logic()
    return catalog

def print_flight_table(flights):
    """
    Muestra una lista de vuelos en formato de tabla
    """
    if not flights:
        print("No hay vuelos para mostrar.")
        return

    table = []
    headers = [ "Fecha", "Salida (real)", 
               "Llegada (real)", "Aerolínea", 
               "N° Vuelo", "Aeronave", "Origen", "Destino",
               "Duración (min)", "Distancia (millas)" ] 
    for flight in flights: 
        f = flight.get("value", flight) 
        date = f.get("date", "") 
        dep_time = f.get("dep_time", "") 
        arr_time = f.get("arr_time", "") 
        carrier = f.get("carrier", "") 
        name = f.get("name", "") 
        flight_no = f.get("flight", "") 
        tailnum = f.get("tailnum", "") 
        origin = f.get("origin", "") 
        dest = f.get("dest", "") 
        air_time = f.get("air_time", "") 
        distance = f.get("distance", "")
        
        table.append([ date, 
                      dep_time, 
                      arr_time, 
                      f"{carrier} - {name}", 
                      flight_no, tailnum, 
                      origin, 
                      dest, 
                      air_time, 
                      distance ]) 
    print(tabulate(table, headers=headers, tablefmt="grid"))

def print_menu():
    print("\nBienvenido")
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
    Carga los datos
    """
    filename = input("Ingrese el nombre del archivo de vuelos (ej: flights_small.csv): ")
    result = logic.load_data(control, filename)

    print("\n Datos cargados correctamente")
    print(f"Tiempo de carga: {result['time_ms']:.2f} ms")
    print(f"Total de vuelos cargados: {result['total_flights']}")

    print("\n Primeros 5 vuelos (por salida programada):")
    print_flight_table(result["first_5"])

    print("\n Últimos 5 vuelos:")
    print_flight_table(result["last_5"])


def print_data(control, id):
    """
    Función que imprime un dato dado su ID
    """
    try:
        # Buscar el vuelo por su posición en la lista
        flight = control["flights"]["elements"][id]
        
        # Mostrar los detalles del vuelo
        print("\n=== Información del vuelo ===")
        print(f"ID: {flight.get('id', 'Unknown')}")
        print(f"Fecha: {flight.get('date', 'Unknown')}")
        print(f"Hora de salida real: {flight.get('dep_time', 'Unknown')}")
        print(f"Hora de llegada real: {flight.get('arr_time', 'Unknown')}")
        print(f"Aerolínea: {flight.get('carrier', 'Unknown')} - {flight.get('name', 'Unknown')}")
        print(f"Aeronave: {flight.get('tailnum', 'Unknown')}")
        print(f"Origen: {flight.get('origin', 'Unknown')}")
        print(f"Destino: {flight.get('dest', 'Unknown')}")
        print(f"Duración: {flight.get('air_time', 'Unknown')} min")
        print(f"Distancia: {flight.get('distance', 'Unknown')} millas")

    except IndexError:
        print("\n ID fuera de rango. Intente con otro número.")
    except KeyError:
        print("\n El formato de los datos no es válido.")

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    if pq.is_empty(control["flights"]):
        print("\nERROR: No hay datos cargados. Por favor, use la opción 0 para cargar un archivo primero.")
        return

    carrier_code = input("Ingrese el código de la aerolínea a analizar (ej: UA): ").upper()
    delay_range_str = input("Ingrese el rango de minutos de retraso [min,max] (ej: 10,30): ")

    if "," not in delay_range_str:
        print("\nERROR: Formato de rango inválido. Debe ser 'min,max'.")
        return
        
    parts = delay_range_str.split(',')
    min_part = parts[0].strip()
    max_part = parts[1].strip()
    min_delay = int(min_part)
    max_delay = int(max_part)
    delay_range = [min_delay, max_delay]

    print("\nProcesando...")
    result = logic.req_1(control, carrier_code, delay_range)
    
    print(f"\n--- Resultados para la aerolínea '{carrier_code}' con retraso entre {min_delay} y {max_delay} minutos ---")
    print(f"Tiempo de ejecución: {result['tiempo_ejecucion_ms']:.4f} ms")
    print(f"Total de vuelos encontrados que cumplen el filtro: {result['total_vuelos']}")

    flights = result.get('vuelos', [])
    
    if not flights:
        print("\nNo se encontraron vuelos que coincidan con los criterios de búsqueda.")
    else:
        headers = flights[0].keys()
        table_data = [list(flight.values()) for flight in flights]
        
        print("\nListado de Vuelos:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        if result['total_vuelos'] > 10:
            print("\nNota: Se muestran los primeros 5 y los últimos 5 vuelos del total encontrado.")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    cod = input("Ingrese el codigo del aeropuerto: ")
    rango = input("Ingrese el rango: ")
    retorno = logic.req_2(control, cod, rango)
    tiempo = retorno["delta"]
    tam = retorno["canti"]
    data = retorno["datos"]
    print("El tiempo total de este requerimiento es: " + str(tiempo))
    print("La cantidad total de vuelos que pasaron los filtros es: " + str(tam))
    for i in range(0, lt.size(data)):
        elem = lt.get_element(data, i)

        print("----------------------------------------------------")
        print(f"Id: {elem['id']}")
        print(f"Codigo del vuelo:        {elem['codigo']}")
        print(f"Fecha:        {elem['fecha']}")
        print(f"Aerolinea:        {elem['aerolinea']}")
        print(f"Codigo de aerolinea:        {elem['ac']}")
        print(f"Origen:        {elem['origen']}")
        print(f"Destino:        {elem['dest']}")
        print(f"Minutos de anticipación:        {elem['dif']}")
        

        print("----------------------------------------------------\n")



def print_req_3(control):
    """
    Función que imprime la solución del Requerimiento 3 en consola
    """
    if pq.is_empty(control["flights"]):
        print("\nERROR: No hay datos cargados. Por favor, use la opción 0 para cargar un archivo primero.")
        return

    carrier_code = input("Ingrese el código de la aerolínea (ej: AA): ").strip().upper()
    dest_code = input("Ingrese el código del aeropuerto destino (ej: JFK): ").strip().upper()
    distance_range_str = input("Ingrese el rango de distancia en millas [min,max] (ej: 500,1500): ").strip()

    if "," not in distance_range_str:
        print("\nERROR: Formato inválido. Debe ser 'min,max'.")
        return

    try:
        parts = distance_range_str.replace("[", "").replace("]", "").split(",")
        min_d = int(parts[0].strip())
        max_d = int(parts[1].strip())
    except Exception:
        print("\nERROR: Valores de distancia no válidos. Use números enteros.")
        return

    print("\nProcesando...")
    retorno = logic.req_3(control, carrier_code, dest_code, (min_d, max_d))

    tiempo = retorno.get("time_ms", 0.0)
    total = retorno.get("total_flights", 0)
    vuelos = retorno.get("flights", lt.new_list())

    print("\n--- Resultados del Requerimiento 3 ---")
    print(f"Tiempo de ejecución (ms): {tiempo:.4f}")
    print(f"Total de vuelos encontrados: {total}\n")

    if lt.size(vuelos) == 0:
        print("No se encontraron vuelos que cumplan con los criterios especificados.\n")
        return

    if total > 10:
        print("Nota: hay más de 10 vuelos; se muestran los primeros 5 y los últimos 5 del resultado ordenado.\n")
        print("Primeros 5 vuelos:\n")
        for i in range(0, 5):
            elem = lt.get_element(vuelos, i)
            print("----------------------------------------------------")
            print(f"ID del vuelo:          {elem.get('id')}")
            print(f"Código del vuelo:      {elem.get('code')}")
            print(f"Fecha:                 {elem.get('date')}")
            print(f"Nombre Aerolínea:      {elem.get('airline_name')}")
            print(f"Código Aerolínea:      {elem.get('carrier')}")
            print(f"Aeropuerto Origen:     {elem.get('origin')}")
            print(f"Aeropuerto Destino:    {elem.get('dest')}")
            print(f"Distancia (millas):    {elem.get('distance')}")
            print("----------------------------------------------------\n")
        print("Últimos 5 vuelos:\n")
        for i in range(lt.size(vuelos) - 5, lt.size(vuelos)):
            elem = lt.get_element(vuelos, i)
            print("----------------------------------------------------")
            print(f"ID del vuelo:          {elem.get('id')}")
            print(f"Código del vuelo:      {elem.get('code')}")
            print(f"Fecha:                 {elem.get('date')}")
            print(f"Nombre Aerolínea:      {elem.get('airline_name')}")
            print(f"Código Aerolínea:      {elem.get('carrier')}")
            print(f"Aeropuerto Origen:     {elem.get('origin')}")
            print(f"Aeropuerto Destino:    {elem.get('dest')}")
            print(f"Distancia (millas):    {elem.get('distance')}")
            print("----------------------------------------------------\n")
    else:
        print("Vuelos encontrados:\n")
        for i in range(0, lt.size(vuelos)):
            elem = lt.get_element(vuelos, i)
            print("----------------------------------------------------")
            print(f"ID del vuelo:          {elem.get('id')}")
            print(f"Código del vuelo:      {elem.get('code')}")
            print(f"Fecha:                 {elem.get('date')}")
            print(f"Nombre Aerolínea:      {elem.get('airline_name')}")
            print(f"Código Aerolínea:      {elem.get('carrier')}")
            print(f"Aeropuerto Origen:     {elem.get('origin')}")
            print(f"Aeropuerto Destino:    {elem.get('dest')}")
            print(f"Distancia (millas):    {elem.get('distance')}")
            print("----------------------------------------------------\n")
        

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    if pq.is_empty(control["flights"]):
        print("\nERROR: No hay datos cargados. Por favor, use la opción 0 para cargar un archivo primero.")
        return

    start_date = input("Ingrese la fecha de inicio (formato AAAA-MM-DD): ")
    end_date = input("Ingrese la fecha de fin (formato AAAA-MM-DD): ")
    time_range = input("Ingrese la franja horaria de salida (formato HH:mm-HH:mm, ej: 06:00-07:00): ")
    n_str = input("Ingrese la cantidad N de aerolíneas a mostrar: ")

    if len(start_date) != 10 or len(end_date) != 10 or start_date > end_date or '-' not in time_range or not n_str.isdigit() or int(n_str) <= 0:
        print("\nERROR: Verifique el formato de fechas, la franja horaria o que N sea un número positivo.")
        return

    print("\nProcesando...")
    result = logic.req_4(control, [start_date, end_date], time_range, int(n_str))
    
    print(f"\n--- Resultados ---\nTiempo de ejecución: {result.get('tiempo_ejecucion_ms', 0):.4f} ms")
    
    top_airlines = result.get('aerolineas', [])
    if not top_airlines:
        print("\nNo se encontraron aerolíneas que cumplan con los criterios especificados.")
        return

    print(f"\nMostrando las {len(top_airlines)} aerolíneas con más vuelos programados:")
    
    #Se itera sobre los resultados para mostrar la información de cada aerolínea
    for i, data in enumerate(top_airlines):
        print("\n" + "="*50 + f"\n{i+1}. Aerolínea: {data.get('Código de la aerolínea', 'N/A')}\n" + "-"*50)
        print(f"   - Vuelos en el rango: {data.get('Número total de vuelos', 'N/A')}")
        print(f"   - Duración promedio: {data.get('Duración promedio (min)', 'N/A')} min")
        print(f"   - Distancia promedio: {data.get('Distancia promedio (millas)', 'N/A')} millas")
        
        flight = data.get("Vuelo con menor duración")
        if flight:
            print("   - Vuelo de menor duración:")
            print(f"     > ID: {flight.get('id', 'N/A')}, Código: {flight.get('code', 'N/A')}")
            print(f"     > Salida: {flight.get('sched_datetime', 'N/A')}")
            print(f"     > Ruta: {flight.get('origin', 'N/A')} -> {flight.get('destination', 'N/A')}")
            print(f"     > Duración: {flight.get('duration', 'N/A')} minutos")
        else:
            print("   - No se encontró información del vuelo de menor duración.")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    rango = input("Ingrese el rango de fechas: ")
    aero = input("Ingrese el aeropuerto: ")
    canti = int(input("Ingrese la cantidad de aerolineas a considerar: "))
    tiempo, cantidad, data = logic.req_5(control,rango, aero, canti)
    
    print("El tiempo total es: " + str(tiempo))
    print("La cantidad de aerolineas consideradas despues de los filtros es: " + str(cantidad))
    for i in range(0, lt.size(data)):
        elem = lt.get_element(data, i)
        vuelo_largo = elem["vuelo_largo"]

        print("----------------------------------------------------")
        print(f"Identificador de la aerolínea: {elem['identificador']}")
        print(f"Número total de vuelos:        {elem['vuelos']}")
        print(f"Duración promedio:             {round(elem['duracion'], 2)}")
        print(f"Distancia promedio:            {round(elem['distancia'], 2)}")

        print("\n Información del vuelo con la mayor distancia recorrida:")
        print(f"   ID del vuelo:               {vuelo_largo['id']}")
        print(f"   Código del vuelo:           {vuelo_largo['codigo']}")
        print(f"   Fecha-Hora de llegada:      {vuelo_largo['fecha_llega']}")
        print(f"   Aeropuerto de origen:       {vuelo_largo['origen']}")
        print(f"   Aeropuerto de destino:      {vuelo_largo['dest']}")
        print(f"   Duración del vuelo:         {vuelo_largo['dura']} minutos")
        print("----------------------------------------------------\n")



def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    if pq.is_empty(control["flights"]):
        print("\nERROR: No hay datos cargados. Por favor, use la opción 0 para cargar un archivo primero.")
        return

    print("\n--- Requerimiento 6 ---")
    rango_fechas = input("Ingrese el rango de fechas [AAAA-MM-DD,AAAA-MM-DD]: ").strip()
    rango_dist = input("Ingrese el rango de distancias [min,max]: ").strip()
    m_str = input("Ingrese la cantidad M de aerolíneas a mostrar: ").strip()

    if "," not in rango_fechas or "," not in rango_dist:
        print("\nERROR: Los rangos deben ser 'x,y'.")
        return

    try:
        f1, f2 = [p.strip() for p in rango_fechas.split(",")]
        d1, d2 = [int(p.strip()) for p in rango_dist.split(",")]
        M = int(m_str)
        if M <= 0:
            print("\nERROR: M debe ser un entero positivo.")
            return
    except:
        print("\nERROR: Formato inválido. Verifique valores.")
        return

    print("\nProcesando...")
    result = logic.req_6(control, [f1, f2], [d1, d2], M)

    tiempo = result.get("time_ms", 0)
    total = result.get("total_airlines", 0)
    lista = result.get("airlines", [])

    print("\n--- Resultados del Requerimiento 6 ---")
    print(f"Rango de fechas analizado: {f1}  →  {f2}")
    print(f"Rango de distancias: {d1} - {d2} millas")
    print(f"Tiempo de ejecución: {tiempo:.4f} ms")
    print(f"Aerolíneas mostradas: {len(lista)} (solicitado: {M})")

    if not lista:
        print("\nNo se encontraron aerolíneas que cumplan con los filtros.")
        return

    for i, entry in enumerate(lista, start=1):
        data = entry["value"] if "value" in entry else entry

        carrier = data["carrier"]
        count = data["count"]
        avg = data["avg_delay"]
        std = data["std_dev"]
        fl = data["closest_flight"]

        print("\n" + "="*60)
        print(f"{i}. Aerolínea: {carrier}")
        print("="*60)
        print(f"  • Total de vuelos analizados:       {count}")
        print(f"  • Retraso promedio (min):           {avg:.2f}")
        print(f"  • Estabilidad (desv. estándar min): {std:.2f}")

        print("\n  >> Vuelo con retraso más cercano al promedio:")
        print(f"     - ID del vuelo:         {fl['id']}")
        print(f"     - Código del vuelo:     {fl['code']}")
        print(f"     - Fecha/Hora salida:    {fl['dep_datetime'][0]} {fl['dep_datetime'][1]}")
        print(f"     - Aeropuerto origen:    {fl['origin']}")
        print(f"     - Aeropuerto destino:   {fl['dest']}")
        print("="*60 + "\n")

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
