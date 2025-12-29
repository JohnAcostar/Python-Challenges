"""
Ejercicio nivel 3: Colombianos en Wikipedia.
Interfaz basada en consola para la interaccion con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos
@author: Cupi2
"""
import colombianos as c

def ejecutar_cargar_datos() -> dict:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de los jugadores.
    Retorno: dict
        El diccionario de ocupaciones con la información de los colombianos en el archivo
    """
    colombianos = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con los colombianos en Wikipedia: ")
    colombianos = c.cargar_datos(archivo)
    if len(colombianos) == 0:
        print("El archivo seleccionado no es valido. No se pudieron cargar los bloques.")
    else:
        print("Se cargaron los siguientes ocupaciones a partir del archivo.")
        for key in colombianos.keys():
            print(key)
    return colombianos


def ejecutar_mayor_lectores(colombianos: dict) -> None:
    """Ejecuta la opción de encontrar el colombiano con mayor número de lectores.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El colombiano con mayor número de lectores en Wikipedia es (nombre del colombiano)'
    """

    resultado = c.mayor_lectores(colombianos)
    print ("El colombiano con mayor numero de lectores de wikipedia es " + resultado)

def ejecutar_hay_3_colombianos(colombianos: dict) -> None:
    """Ejecuta la opción que busca si hay 3 colombianos que superen un número de lectores
       dada una ocupación, un género y un número de lectores a superar.  
    La consola debe mostrar un mensaje con el siguiente mensaje según el caso:
        'Sí existen 3 colombianos de este género y ocupación que superen este tope.'
        'No existen 3 colombianos de este género y ocupación que superen este tope.'
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado
    ocupacion = str(input("Ingrese la ocupacion que quiere buscar: "))
    genero = str(input("Ingrese el genero que quiere buscar: "))
    lectores = int(input("escriba el numero de lectores: "))
    resultado = c.hay_3_colombianos(colombianos, ocupacion, genero, lectores)
    
    if resultado:
        print("si existen 3 colombianos de este genero y ocupacion que superen este tope.")
    else:
        print("No existen 3 colombianos de este género y ocupación que superen este tope.")

def ejecutar_promedio_lectores(colombianos:dict)-> None:
    """Ejecuta la opción de calcular el promedio de lectores de las personas de una ocupación específica. 
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El número de lectores promedio de los colombianos con ocupación (ocupacion) es (número de lectores promedio).'
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado
    ocupacion = str(input("Ingrese la ocupacion que quiere buscar: "))
    resultado = c.promedio_lectores(colombianos, ocupacion)
    print ("El número de lectores promedio de los colombianos con ocupación " + str(ocupacion) + " es " + str(resultado)) 
    
    
    
def ejecutar_mayor_rating(colombianos: dict)->None:
    """Ejecuta la opción de encontrar la ocupación con mayor número de lectores promedio
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'La ocupación con mayor número de lectores promedio es (ocupación).'
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado
    rating = c.mayor_rating(colombianos)
    print("La ocupación con mayor número de lectores promedio es "+ rating)


def ejecutar_colombianos_rango(colombianos: dict) -> None:
    """Ejecuta la opción que consulta colombianos con una ocupación específica que hayan nacido en un rango de años
    Se debe mostrar al usuario solo los nombres de los colombianos que cumplen con la condición.
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado
    ocupacion = str(input("Ingrese la ocupacion que quiere buscar: "))
    superior = int(input("Ingrese un limite superior que quiere buscar: "))
    inferior = int(input("Ingrese un limite inferior que quiere buscar: "))
    resultado = c.colombianos_rango(colombianos, ocupacion, inferior, superior)
    for nombre in resultado:
        print(nombre["nombre"])

def ejecutar_nacionalidades(colombianos: dict) -> None:
    """Ejecuta la opción que cuenta cuantas personas hay de cada nacionalidad. 
    Se debe mostrar al usuario un mensaje que luzca así:
        '(nacionalidad) --> (número de personas con esa nacionalidad)'
    Ejemplo:
        Colombia - Peru --> 2
        Colombia - Mexico --> 7
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado
    resultado = c.nacionalidades(colombianos)
    for nacionalidad in resultado.keys():
        print(nacionalidad + " --> " + str(resultado[nacionalidad]))
        

def ejecutar_calcular_edad(colombianos: dict) -> None:
    """Ejecuta la opción de calcular la edad de cada persona.
    Se debe mostrar al usuario el diccionario de colombianos con la edad incluida
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado

    resultado = c.calcular_edad(colombianos)
    print (resultado)
    
def ejecutar_colombianos_fallecidos(colombianos: dict) -> None:
    """Ejecuta la opción que consulta qué colombianos han fallecido.
    Se debe mostrar al usuario los nombres de los colombianos que han fallecido.
    """
    
    resultado = c.colombianos_fallecidos(colombianos)
    for ocupacion in resultado.keys():
        for persona in resultado[ocupacion]:
            print (persona["nombre"])
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de colombianos.")
    print("2. Encontrar el colombiano con mayor número de lectores.")
    print("3. Encontrar si hay 3 colombianos que superen el tope de lectores.")
    print("4. Calcular el promedio de lectores de las personas de una ocupación específica.")
    print("5. Encontrar qué ocupación es la que tiene mayor número de lectores promedio.")
    print("6. Consultar colombianos con una ocupación específica que hayan nacido en un rango de años.")
    print("7. Contar cuantas personas hay de cada nacionalidad.")
    print("8. Calcular la edad de cada persona. ")
    print("9. Consultar qué colombianos han fallecido.")
    print("10. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    colombianos = {}
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            colombianos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_mayor_lectores(colombianos)
        elif opcion_seleccionada == 3:
            ejecutar_hay_3_colombianos(colombianos)
        elif opcion_seleccionada == 4:
            ejecutar_promedio_lectores(colombianos)
        elif opcion_seleccionada == 5:
            ejecutar_mayor_rating(colombianos)
        elif opcion_seleccionada == 6:
            ejecutar_colombianos_rango(colombianos)
        elif opcion_seleccionada == 7:
            ejecutar_nacionalidades(colombianos)
        elif opcion_seleccionada == 8:
            ejecutar_calcular_edad(colombianos)
        elif opcion_seleccionada == 9:
            ejecutar_colombianos_fallecidos(colombianos)
        elif opcion_seleccionada == 10:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()
