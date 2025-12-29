import sys
import os
from DataStructures.List import array_list as lt
import App.logic as logic
from tabulate import tabulate

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


def new_logic():
    """
        Se crea una instancia del controlador
    """
    catalog = {}
    catalog["taxis"] = lt.new_list()
    catalog["neighborhoods"] = lt.new_list()
    return catalog

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
    Carga los datos
    """
    filename = input("Ingrese el nombre del archivo de taxis (ej: taxis-small.csv): ")
    data = logic.load_data(control, filename)
    print(f"\nTiempo carga: {data['total']:.2f} ms")
    print(f"Total trayectos cargados: {data['tamaño']}")
    print("Trayecto más corto:", data["mas_corto"])
    print("Trayecto más largo:", data["mas_largo"])
    print("Primeros viajes en el rango:")
    for i, trip in enumerate(data["primeros_5"], start=1):
        print(f"{i}. Pickup: {trip['pickup']} | "
              f"Dropoff: {trip['dropoff']} | "
              f"Tiempo de duración del trayecto: {trip['tiempo']} | "
              f"Distancia: {trip['distance']:.2f} mi | "
              f"Total: ${trip['total_amount']:.2f}") 

        # Mostrar los últimos N registros
    print("\n Últimos viajes en el rango:")
    for i, trip in enumerate(data["ultimos_5"], start=1):
        print(f"{i}. Pickup: {trip['pickup']} | "
              f"Dropoff: {trip['dropoff']} | "
              f"Tiempo de duración del trayecto: {trip['tiempo']} | "
              f"Distancia: {trip['distance']:.2f} mi | "
              f"Total: ${trip['total_amount']:.2f}")  
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    try:
        return control["taxis"]["elements"][id]
    except IndexError:
        print("ID fuera de rango")
        return None
    
    
def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    hora_1 = input("Ingrese la hora inicial: ")
    hora_2 = input("Ingrese la hora final: ")
    muestra = int(input("Ingrese el tamaño de la muestra: "))
    
    retorno = logic.req_1(control, hora_1, hora_2, muestra)
    
    #Imrpimimos

    print("\n" + "=" * 100)
    print(f"Tiempo de ejecución: {retorno['tiempo']:.2f} ms")
    print(f"Total de viajes en el rango: {retorno['tamano']}")
    print("=" * 100 + "\n")
    
    cabs = ["Pickup", "Longitud y Latitud", "Dropoff", "Longitud y Latitud", "Distancia", "Total"]
    
    if retorno["factor"] == 0:
        primeros = [
            [v["pickup"], v["longitud_latitud"],v["dropoff"], v["longitud_latitud_2"], f"{v['distancia']:.2f}", f"${v['costo']:.2f}"]
            for v in retorno["primeros"]["elements"]
        ]
        
        ultimos = [
            [v["pickup"], v["longitud_latitud"], v["dropoff"], v["longitud_latitud_2"], f"{v['distancia']:.2f}", f"${v['costo']:.2f}"]
            for v in retorno["ultimos"]["elements"]
        ]
        print("Primeros viajes en el rango:\n")
        print(tabulate(primeros, headers = cabs, tablefmt="fancy_grid"))

        print("\nÚltimos viajes en el rango:\n")
        print(tabulate(ultimos, headers = cabs, tablefmt="fancy_grid"))
        
    else:
        todos = [
            [v["pickup"], v["longitud_latitud"],v["dropoff"], v["longitud_latitud_2"], f"{v['distancia']:.2f}", f"${v['costo']:.2f}"]
            for v in retorno["todos"]["elements"]
        ]
        
        print("Viajes en el rango:\n")
        print(tabulate(todos, headers = cabs, tablefmt="fancy_grid"))



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    try:
        # Entradas del usuario
        lat_min = float(input("Ingrese la latitud inicial del rango: "))
        lat_max = float(input("Ingrese la latitud final del rango: "))
        n = int(input("Ingrese el tamaño de la muestra N: "))

        print("\nProcesando la solicitud...\n")

        result = logic.req_2(control, lat_min, lat_max, n)

        # Si no hay resultados
        if not result or result["total_rutas"] == 0:
            print("\nNo se encontraron rutas que cumplan el filtro de latitud.")
            print(f"Tiempo de ejecución: {result.get('tiempo', 0):.2f} ms\n")
            return

        print("=" * 80)
        print(f"Tiempo de ejecución: {result['tiempo']:.2f} ms")
        print(f"Total de viajes encontrados: {result['total_rutas']}")
        print("=" * 80 + "\n")

        cabs = [
            "pickup_datetime", "pickup_coord",
            "dropoff_datetime", "dropoff_coord",
            "trip_distance", "total_amount"
        ]

        # Si hay menos o igual a 2N viajes, mostrar todos
        if result.get("factor", 0) == 1 or result["total_rutas"] <= 2 * n:
            print("Viajes en el rango de latitud:\n")
            todos = [
                [
                    v["pickup_datetime"],
                    v["pickup_coord"],
                    v["dropoff_datetime"],
                    v["dropoff_coord"],
                    f"{v['trip_distance']:.2f}",
                    f"${v['total_amount']:.2f}"
                ]
                for v in result["todos"]
            ]
            print(tabulate(todos, headers=cabs, tablefmt="fancy_grid", floatfmt=".4f"))

        else:
            # Mostrar primeros N viajes
            print(f"Primeros {len(result['primeros'])} viajes:\n")
            primeros = [
                [
                    v["pickup_datetime"],
                    v["pickup_coord"],
                    v["dropoff_datetime"],
                    v["dropoff_coord"],
                    f"{v['trip_distance']:.2f}",
                    f"${v['total_amount']:.2f}"
                ]
                for v in result["primeros"]
            ]
            print(tabulate(primeros, headers=cabs, tablefmt="fancy_grid", floatfmt=".4f"))

            # Mostrar últimos N viajes
            print(f"\nÚltimos {len(result['ultimos'])} viajes:\n")
            ultimos = [
                [
                    v["pickup_datetime"],
                    v["pickup_coord"],
                    v["dropoff_datetime"],
                    v["dropoff_coord"],
                    f"{v['trip_distance']:.2f}",
                    f"${v['total_amount']:.2f}"
                ]
                for v in result["ultimos"]
            ]
            print(tabulate(ultimos, headers=cabs, tablefmt="fancy_grid", floatfmt=".4f"))

        print("\n")

    except ValueError:
        print("\nError: asegúrese de ingresar valores numéricos válidos para las coordenadas y N.\n")
    except KeyError:
        print("\nError: el resultado devuelto por logic.req_2 no tiene el formato esperado.\n")
    except Exception as e:
        print(f"\nSe produjo un error inesperado: {str(e)}\n")


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    print("Solo somos un grupo de 2 personas. Por lo tanto, este requerimiento no se puede ejecutar.")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    try:
        # Solicitar datos al usuario
        completion_date = input("Ingrese la fecha de terminación (YYYY-MM-DD): ").strip()
        time_filter = input("Ingrese el filtro de tiempo (ANTES o DESPUES): ").strip().upper()
        reference_time = input("Ingrese la hora de referencia (HH:MM:SS): ").strip()
        n = int(input("Ingrese el tamaño de la muestra N: "))

        print("\nProcesando la solicitud...\n")

        result = logic.req_4(control, completion_date, time_filter, reference_time, n)

        print("========================================")
        print(f"Tiempo de ejecución: {result['tiempo']:.2f} ms")
        print(f"Total de viajes encontrados: {result['total_rutas']}")
        print("========================================\n")

        if result["total_rutas"] == 0:
            print(result.get("message", "No se encontraron viajes con los filtros especificados."))
            return

        cabs = [
            "pickup_datetime", "pickup_coord",
            "dropoff_datetime", "dropoff_coord",
            "trip_distance", "total_amount"
        ]

        # Si hay menos de 2N viajes, mostrar todos juntos
        if result.get("factor", 0) == 1 or result["total_rutas"] <= 2 * n:
            print("Viajes en el rango:\n")
            todos = [
                [
                    v["pickup_datetime"],
                    v["pickup_coord"],
                    v["dropoff_datetime"],
                    v["dropoff_coord"],
                    f"{v['trip_distance']:.2f}",
                    f"${v['total_amount']:.2f}"
                ]
                for v in result["todos"]
            ]
            print(tabulate(todos, headers=cabs, tablefmt="fancy_grid", floatfmt=".4f"))

        else:
            # Mostrar primeros N viajes
            print(f"Primeros {len(result['primeros'])} viajes:\n")
            primeros = [
                [
                    v["pickup_datetime"],
                    v["pickup_coord"],
                    v["dropoff_datetime"],
                    v["dropoff_coord"],
                    f"{v['trip_distance']:.2f}",
                    f"${v['total_amount']:.2f}"
                ]
                for v in result["primeros"]
            ]
            print(tabulate(primeros, headers=cabs, tablefmt="fancy_grid", floatfmt=".4f"))

            # Mostrar últimos N viajes
            print(f"\nÚltimos {len(result['ultimos'])} viajes:\n")
            ultimos = [
                [
                    v["pickup_datetime"],
                    v["pickup_coord"],
                    v["dropoff_datetime"],
                    v["dropoff_coord"],
                    f"{v['trip_distance']:.2f}",
                    f"${v['total_amount']:.2f}"
                ]
                for v in result["ultimos"]
            ]
            print(tabulate(ultimos, headers=cabs, tablefmt="fancy_grid", floatfmt=".4f"))

        print("\n")

    except ValueError:
        print("\nError: asegúrese de ingresar valores válidos para la fecha, hora o tamaño de muestra.\n")
    except KeyError:
        print("\nError: el resultado devuelto por logic.req_4 no tiene el formato esperado.\n")
    except Exception as e:
        print(f"\nSe produjo un error inesperado: {str(e)}\n")

def print_req_5(control):
    hora_1 = input("Ingrese la fecha: ")
    muestra = int(input("Ingrese el tamaño de la muestra: "))
    
    retorno = logic.req_5(control, hora_1, muestra)
    
    #Imrpimimos

    print("\n" + "=" * 100)
    print(f"Tiempo de ejecución: {retorno['tiempo']:.2f} ms")
    print(f"Total de viajes en la fecha: {retorno['tamano']}")
    print("=" * 100 + "\n")
    
    cabs = ["Pickup", "Longitud y Latitud", "Dropoff", "Longitud y Latitud", "Distancia", "Total"]
    
    if retorno["factor"] == 0:
        primeros = [
            [v["pickup"], v["longitud_latitud"],v["dropoff"], v["longitud_latitud_2"], f"{v['distancia']:.2f}", f"${v['costo']:.2f}"]
            for v in retorno["primeros"]["elements"]
        ]
        
        ultimos = [
            [v["pickup"], v["longitud_latitud"], v["dropoff"], v["longitud_latitud_2"], f"{v['distancia']:.2f}", f"${v['costo']:.2f}"]
            for v in retorno["ultimos"]["elements"]
        ]
        print("Primeros viajes en la fecha :\n")
        print(tabulate(primeros, headers = cabs, tablefmt="fancy_grid"))

        print("\nÚltimos viajes en la fecha:\n")
        print(tabulate(ultimos, headers = cabs, tablefmt="fancy_grid"))
        
    else:
        todos = [
            [v["pickup"], v["longitud_latitud"],v["dropoff"], v["longitud_latitud_2"], f"{v['distancia']:.2f}", f"${v['costo']:.2f}"]
            for v in retorno["todos"]["elements"]
        ]
        
        print("Viajes en el rango:\n")
        print(tabulate(todos, headers = cabs, tablefmt="fancy_grid"))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    pickup_neigh = input("Ingrese el nombre del barrio de recogida: ").strip()
    start_hour = input("Ingrese la hora inicial del rango (HH): ").strip()
    end_hour = input("Ingrese la hora final del rango (HH): ").strip()
    n = int(input("Ingrese el tamaño de la muestra N: "))

    print("\nProcesando la solicitud...\n")

    result = logic.req_6(control, pickup_neigh, start_hour, end_hour, n)

    print("========================================")
    print(f"Tiempo de ejecución: {result['tiempo']:.2f} ms")
    print(f"Total de viajes encontrados: {result['total_rutas']}")
    print("========================================\n")

    if result["total_rutas"] == 0:
        print(result.get("message", "No se encontraron viajes con los filtros especificados."))
        return

    # Si el total < 2N, mostrar todos los viajes
    if result.get("message", "").startswith("Solo se encontraron"):
        print(result["message"])
        print(tabulate(result["primeros"], headers="keys", tablefmt="grid", floatfmt=".4f"))
        return

    print(f"Primeros {len(result['primeros'])} viajes:\n")
    print(tabulate(result["primeros"], headers="keys", tablefmt="grid", floatfmt=".4f"))
    print("\n")

    print(f"Últimos {len(result['ultimos'])} viajes:\n")
    print(tabulate(result["ultimos"], headers="keys", tablefmt="grid", floatfmt=".4f"))
    print("\n")
    
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
