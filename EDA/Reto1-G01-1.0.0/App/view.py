import sys
import os
from DataStructures.List import array_list as lt
import App.logic as logic

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
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("0- Salir")

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
    passengers = int(input("Ingrese la cantidad de pasajeros a filtrar: "))
    result = logic.req_1(control, passengers)

    print("\n--- Requerimiento 1 ---")
    print(f"Tiempo ejecución: {result['tiempo']:.2f} ms")
    print(f"Total trayectos: {result['total_trayectos']}")
    print(f"Duración promedio (min): {result['avg_duracion']:.2f}")
    print(f"Costo total promedio ($): {result['avg_costo']:.2f}")
    print(f"Distancia promedio (millas): {result['avg_distancia']:.2f}")
    print(f"Costo peajes promedio ($): {result['avg_peajes']:.2f}")
    print(f"Medio de pago más usado: {result['pago_frecuente']}")
    print(f"Propina promedio ($): {result['avg_propina']:.2f}")
    print(f"Fecha más frecuente: {result['fecha_frecuente']}")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    metodo = input("Ingrese el método de pago a filtrar (CASH, CREDIT_CARD, etc.): ")
    result = logic.req_2(control, metodo)

    print("\n--- Requerimiento 2 ---")
    print(f"Tiempo ejecución: {result['tiempo_ejecucion']:.2f} ms")
    print(f"Total trayectos: {result['total_trayectos']}")
    print(f"Duración promedio (min): {result['avg_duracion']:.2f}")
    print(f"Costo total promedio ($): {result['avg_costo']:.2f}")
    print(f"Distancia promedio (millas): {result['avg_distancia']:.2f}")
    print(f"Costo peajes promedio ($): {result['avg_peajes']:.2f}")
    print(f"Cantidad de pasajeros más frecuente: {result['pasajeros_frecuente']}")
    print(f"Propina promedio ($): {result['avg_propina']:.2f}")
    print(f"Fecha más frecuente: {result['fecha_frecuente']}")



def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    print("Solo somos un grupo de 2 personas. Por lo tanto, este requerimiento no se puede ejecutar.")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    filtro = input("Ingrese filtro de costo (MAYOR/MENOR): ")
    fecha_ini = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha final (YYYY-MM-DD): ")

    result = logic.req_4(control, filtro, fecha_ini, fecha_fin)

    print("\n--- Requerimiento 4 ---")
    print(f"Tiempo ejecución: {result['tiempo']:.2f} ms")
    print(f"Filtro aplicado: {result['filtro']}")
    print(f"Total trayectos en rango: {result['total_trayectos']}")
    print("Combinación de barrios:")
    print(f" Origen: {result['origen']}")
    print(f" Destino: {result['destino']}")
    print(f" Distancia promedio (millas): {result['avg_distancia']:.2f}")
    print(f" Duración promedio (min): {result['avg_duracion']:.2f}")
    print(f" Costo total promedio ($): {result['avg_costo']:.2f}")


def print_req_5(control):
    
    filtro = input("Ingrese filtro de costo (MAYOR/MENOR): ")
    fecha_ini = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha final (YYYY-MM-DD): ")
    
    result = logic.req_5(control, filtro, fecha_ini, fecha_fin)
    print("\n--- Requerimiento 5 ---")
    print(f"Tiempo ejecución: {result['tiempo']:.2f} ms")
    print(f"Filtro aplicado: {result['filtro']}")
    print(f"Total trayectos en rango: {result['total_trayectos']}")
    print(f"Franja Horaria: {result['franja']}")
    print(f"Costo Promedio: {result['avg_cost']}")
    print(f"Cantidad de viajes en la franja: {result['num_trips']}")
    print(f"Duración promedio (min): {result['avg_duracion']:.2f}")
    print(f"Cantidad promedio de pasajeros: {result['avg_pasajeros']:.2f}")
    print(f"Viaje más costoso en la franja horaria: {result['max_trip']}")
    print(f"Viaje menos costoso en la franja horaria: {result['min_trip']}")

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    result = logic.req_6(
        control,
        barrio_inicio=input("Ingrese el barrio de inicio: "),
        fecha_inicio=input("Ingrese la fecha inicial (YYYY-MM-DD): "),
        fecha_fin=input("Ingrese la fecha final (YYYY-MM-DD): ")
    )

    # Caso sin resultados o cuando no hay vecindario
    if result.get("total_trayectos", 0) == 0:
        print("\n--- Requerimiento 6 ---")
        print(result.get("message", "No se encontraron trayectos."))
        print(f"Tiempo ejecución: {result['tiempo']:.2f} ms")
        return

    print("\n--- Requerimiento 6 ---")
    print(f"Tiempo de ejecución: {result['tiempo']:.2f} ms")
    print(f"Total de trayectos en rango de fechas: {result['total_trayectos_fecha']}") 
    print(f"Total de trayectos con barrio origen: {result['total_trayectos']}")
    print(f"Distancia promedio (millas): {result['avg_distancia']:.2f}")
    print(f"Duración promedio (minutos): {result['avg_duracion']:.2f}")
    print(f"Barrio más visitado: {result['barrio_mas_visitado']}")
    print("\nMétodos de pago:")

    # Encabezado
    print(f"{'Tipo':<12} {'#Trayectos':<12} {'Prom. Precio($)':<15} "
          f"{'Prom. Tiempo(min)':<18} {'Más usado':<10} {'Mayor recaudo':<15}")

    # Filas
    for pago in result["medios_pago"]:
        print(f"{pago['tipo']:<12} {pago['cantidad']:<12} "
              f"{pago['avg_precio']:<15.2f} {pago['avg_tiempo_min']:<18.2f} "
              f"{'Sí' if pago['es_mas_usado'] else 'No':<10} "
              f"{'Sí' if pago['es_mayor_recaudo'] else 'No':<15}")


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
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
