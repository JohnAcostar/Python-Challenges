"""
Ejercicio nivel 2: Videojuegos
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

@author: Cupi2

"""

import math
def crear_videojuego(titulo: str, anio_de_lanzamiento: int, generos: str, rating: float,
                     es_multijugador: bool, clasificacion_edad: str, duracion: int) -> dict:
    """
    Función para crear un videojuego en la plataforma.

    Parámetros
    ----------

    titulo : str
        Título del videojuego.
    anio_de_lanzamiento : int
        Año de lanzamiento del videojuego.
    generos : str
        Géneros del videojuego separados por coma
    rating : float
        Rating IGN del videojuego, en el rango [0.0, 10.0].
    es_multijugador : bool
        Indica si el videojuego tiene algún modo multijugador.
    clasificacion_edad : str
        Clasificación de edad del videojuego según la ESRB.
    duracion : int
        Duración del videojuego según el sitio HowLongToBeat.
        El formato es XY, con X como las horas y Y como los minutos, ejemplo: 3221.

    Retorno
    -------
    dict
        Diccionario del videojuego con su información.

    """
    
    juego={"titulo":titulo,
            "anio_de_lanzamiento":anio_de_lanzamiento,
            "generos":generos,
            "rating":rating,
            "es_multijugador":es_multijugador,
            "clasificacion_edad":clasificacion_edad,
            "duracion":duracion}
    
    # TODO: completar y retornar el valor adecuado
    return juego


def buscar_videojuego_por_titulo(j1: dict, j2: dict, j3: dict, j4: dict, titulo: str) -> dict:
    """
    Busca un videojuego en particular por su título.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.
    titulo : str
        Título del videojuego que se desea buscar.

    Retorno
    -------
    dict
        Diccionario que contiene la información del videojuego encontrado. Si no se encuentra el videojuego,
        retorna None.

    """
    
    if titulo == j1["titulo"]:
        titulos = j1
        
    elif titulo==j2["titulo"]:
        titulos=j2
        
    elif titulo==j3["titulo"]:
        titulos=j3
        
    elif titulo==j4["titulo"]:
        titulos=j4
    else:
        titulos= None
        
    return titulos
    # TODO: completar y retornar el valor adecuado
    


def buscar_videojuego_mas_corto(j1: dict, j2: dict, j3: dict, j4: dict) -> dict:
    """
    Busca el videojuego más corto de un grupo de videojuegos.
    En caso de que dos o más videojuegos tengan la misma duración, retorne el primero que encuentre.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.

    Retorno
    -------
    dict
        Diccionario que contiene la información del videojuego más corto.

    """
    jmenor = 0
    if j1["duracion"] <= j2["duracion"] and j1["duracion"] <= j3["duracion"] and j1["duracion"] <= j4["duracion"]:
        jmenor= j1
            
    elif j2["duracion"] < j1["duracion"] and j2["duracion"] <= j3["duracion"] and j2["duracion"] <= j4["duracion"]:
        jmenor= j2
            
    elif j3["duracion"] < j2["duracion"] and j3["duracion"] < j1["duracion"] and j3["duracion"] <= j4["duracion"]:
        jmenor= j3
        
        
    if j4["duracion"] < j2["duracion"] and j4["duracion"] < j3["duracion"] and j4["duracion"] < j1["duracion"]:
        jmenor= j4
    
    # TODO: completar y retornar el valor adecuado
    return jmenor


def calcular_dias_necesarios_para_terminar_videojuego(juego: dict, horas_disponibilidad: int) -> int:
    """
    Calcula los días necesarios para terminar un videojuego.

    Parámetros
    ----------
    juego : dict
        Diccionario que contiene la información del videojuego.
    horas_disponibilidad : int
        Horas disponibles por día para jugar.

    Retorno
    -------
    int
        Número de días necesarios para terminar el videojuego.

    """
    dias = 0
    tiempo = juego["duracion"]
    horas = tiempo / 100
    
    
    dias= horas/horas_disponibilidad
    
    
    # TODO: completar y retornar el valor adecuado
    return math.ceil(dias)


def mostrar_videojuegos_aptos_para_cierta_edad(j1: dict, j2: dict, j3: dict, j4: dict, edad: int) -> str:
    """
    Retorna una cadena con los títulos de los videojuegos aptos para una cierta edad.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.
    edad : int
        Edad a la que se desea verificar la aptitud de los videojuegos.

    Retorno
    -------
    str
        Cadena con los títulos de los videojuegos aptos para la edad especificada. 
        Si hay más de un juego apto, el formato será "X, Y, Z", con X, Y y Z siendo 
        los nombres de los juegos; En caso de haber un único resultado, el formato 
        será el nombre del juego "X". Además, en caso de no existir ningún juego apto,
        se debe responder con el siguiente mensaje "No hay ningún juego apto para 
        personas de X años”, donde X es la edad.

    """
    nom_1 = 0
    nom_2 = 0
    nom_3 = 0
    nom_4 = 0 
    x = ""
    
    if j1["clasificacion_edad"] == "E" or (j1["clasificacion_edad"] == "E10+" and edad >= 10) or (j1["clasificacion_edad"] == "T" and edad >= 13) or (j1["clasificacion_edad"] == "M" and edad >= 17):
        nom_1 = j1["titulo"]

    if j2["clasificacion_edad"] == "E" or (j2["clasificacion_edad"] == "E10+" and edad >= 10) or (j2["clasificacion_edad"] == "T" and edad >= 13) or (j2["clasificacion_edad"] == "M" and edad >= 17):
        nom_2 = j2["titulo"]

    if j3["clasificacion_edad"] == "E" or (j3["clasificacion_edad"] == "E10+" and edad >= 10) or (j3["clasificacion_edad"] == "T" and edad >= 13) or (j3["clasificacion_edad"] == "M" and edad >= 17):
        nom_3 = j3["titulo"]
    
    if j4["clasificacion_edad"] == "E" or (j4["clasificacion_edad"] == "E10+" and edad >= 10) or (j4["clasificacion_edad"] == "T" and edad >= 13) or (j4["clasificacion_edad"] == "M" and edad >= 17):
        nom_4 = j4["titulo"]

    if nom_1 == 0 and nom_2 == 0 and nom_3 == 0 and nom_4 == 0 :
        x = "No hay ningún juego apto para personas de " + str(edad) + " años"
        
    elif not nom_1 == 0:
        if not nom_2 == 0:
            if not nom_3 == 0:
                if not nom_4 == 0:
                    x = nom_1 + "," + nom_2 + "," + nom_3 + "," + nom_4 
                else:
                    x = nom_1 + "," + nom_2 + "," + nom_3 
            elif not nom_4 == 0 :
                x = nom_1 + "," + nom_2 + "," + nom_4
            else:
                x = nom_1 + "," + nom_2
        elif not nom_3 == 0:
            if not nom_4 == 0:
                x = nom_1 + "," + nom_3 + "," + nom_4 
            else:       
                x = nom_1 + "," + nom_3
        elif not nom_4 == 0:
            x = nom_1 + "," + nom_4
        else:
            x = nom_1
            
    elif not nom_2 == 0:
        if not nom_3 == 0:
            if not nom_4 == 0:
                x = nom_2 + "," + nom_3 + "," + nom_4 
            else:
                x = + nom_2 + "," + nom_3  
        elif not nom_4 == 0:
            x = nom_2 + "," + nom_4
        else:
            x = nom_2
    
    elif not nom_3 == 0:
        if not nom_4 == 0:
            x = nom_3 + "," + nom_4 
        else:
            x = nom_3 
            
    elif not nom_4 == 0:
        x = nom_4
    
    return x
    
       
    # TODO: completar y retornar el valor adecuado


def determinar_puntaje_de_un_videojuego(juego: dict) -> float:
    """
    Calcula el puntaje de un videojuego en base a sus características.

    Parámetros:
    - juego (dict): Diccionario que contiene la información del videojuego.

    Retorna:
    - float: Puntaje del videojuego.

    puntos por:

    anio_de_lanzamiento -> mas reciente es mejor | 2020s -> 4 | 2010s -> 3 | 2000s -> 2 | 1990s -> 1 | 1980s -> 0
    generos -> solo suma el mejor genero | carreras o simulacion -> 4 | deportes -> 3 | accion, aventura o plataformas -> 2 | rol o estrategia -> 1
    rating -> mas rating mejor | divida el rating en 2 y restarle 1
    es_multijugador -> si es multijugador sume 5 puntos
    clasificacion_edad -> mas inclusivo mejor | E -> 4 | E10+ -> 3 | T -> 2 | M -> 1
    duracion -> quiero que dure lo justo | entre 1 y 3 hr -> 2 | entre 3 y 10 hr -> 4 | mas de 10 hr -> 2

    """
    # TODO: completar y retornar el valor adecuado
    car = "carreras"
    sim = "simulación"
    dep = "deportes"
    acc = "acción"
    ave = "aventura"
    pla = "plataforma"
    rol = "rol"
    est = "estrategia"
    
    genero = juego["generos"]
    ratio = juego["rating"]
    edad = juego["clasificacion_edad"]
    puntos = 0
    duracion = juego["duracion"]
    if juego["anio_de_lanzamiento"] >= 2020:
        puntos += 4
    elif juego["anio_de_lanzamiento"] >= 2010 and juego["anio_de_lanzamiento"] < 2020:
        puntos += 3
    elif juego["anio_de_lanzamiento"] >= 2000 and juego["anio_de_lanzamiento"] < 2010:
        puntos += 2
    elif juego["anio_de_lanzamiento"] < 2000:
        puntos += 1
        
    if genero.count(car) or genero.count(sim):
        puntos += 4
    
    elif genero.count(dep):
        puntos += 3
    
    elif genero.count(acc) or genero.count(ave) or genero.count(pla):
        puntos += 2 
        
    elif genero.count(rol) or genero.count(est):
        puntos += 1
        
    puntos = puntos + ((ratio/2)-1)
    
    if juego["es_multijugador"] == True:
        puntos += 5
    
    if edad == "E":
        puntos += 4
        
    elif edad == "E10+":
        puntos += 3

    elif edad == "T":
        puntos += 2

    elif edad == "M":
        puntos += 1
        
    if duracion > 100 and duracion < 300:
        puntos +=2
    elif duracion > 300 and duracion <= 1000:
        puntos +=4
        
    elif duracion > 1000:
        puntos +=2  
        
    return round(puntos,2)


def contar_cantidad_de_juegos_de_un_genero(j1: dict, j2: dict, j3: dict, j4: dict, genero: str) -> int:
    """
    Cuenta la cantidad de juegos de un género específico.

    Parámetros:
    - j1 (dict): Diccionario que contiene la información del primer videojuego.
    - j2 (dict): Diccionario que contiene la información del segundo videojuego.
    - j3 (dict): Diccionario que contiene la información del tercer videojuego.
    - j4 (dict): Diccionario que contiene la información del cuarto videojuego.
    - genero (str): Género de los videojuegos a contar.

    Retorna:
    - int: Cantidad de videojuegos del género especificado.

    """
    genero1 = j1["generos"]
    genero2 = j2["generos"]
    genero3 = j3["generos"]
    genero4 = j4["generos"]
    
    cantidad = 0
    if genero1.count(genero):
        cantidad += 1
    if genero2.count(genero):
        cantidad += 1
    if genero3.count(genero):
        cantidad += 1
    if genero4.count(genero):
        cantidad += 1
    # TODO: completar y retornar el valor adecuado
    return cantidad


def calcular_promedio_de_rating_de_los_videojuegos_de_un_genero(j1: dict, j2: dict, j3: dict, j4: dict, genero: str) -> float:
    """
    Calcula el promedio de rating de los videojuegos de un género específico.

    Parámetros:
    - j1 (dict): Diccionario que contiene la información del primer videojuego.
    - j2 (dict): Diccionario que contiene la información del segundo videojuego.
    - j3 (dict): Diccionario que contiene la información del tercer videojuego.
    - j4 (dict): Diccionario que contiene la información del cuarto videojuego.
    - genero (str): Género de los videojuegos a contar.

    Retorna:
    - float: Promedio de rating de los videojuegos del género especificado. Si no hay videojuegos del género,
    retorna -1.

    """
    genero1 = j1["generos"]
    genero2 = j2["generos"]
    genero3 = j3["generos"]
    genero4 = j4["generos"]
    
    num = contar_cantidad_de_juegos_de_un_genero(j1, j2, j3, j4, genero)
    rat_prom = 0
    
    if genero1.count(genero):
        rat_prom += j1["rating"]
    if genero2.count(genero):
        rat_prom += j2["rating"]
    if genero3.count(genero):
        rat_prom += j3["rating"]
    if genero4.count(genero):
        rat_prom += j4["rating"]
        
    rat_prom = rat_prom / num
    
    # TODO: completar y retornar el valor adecuado
    return round(rat_prom,2)

