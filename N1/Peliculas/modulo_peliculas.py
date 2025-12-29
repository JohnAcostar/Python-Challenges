"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    dictionary = {}
    
    dictionary["nombre"] = nombre
    dictionary["genero"] = genero
    dictionary["duracion"] = duracion
    dictionary["anio"] = anio
    dictionary["clasificacion"] = clasificacion
    dictionary["hora"] = hora
    dictionary["dia"] = dia
    
    return dictionary

print(crear_pelicula("Sherk", "familiar", 120, 2000, "todos", 1625, "Lunes"))

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    
    retorno = ""
    
    if nombre_pelicula == p1["nombre"]:
        retorno = p1
        
    elif nombre_pelicula == p2["nombre"]:
        retorno = p2    
    
    elif nombre_pelicula == p3["nombre"]:
        retorno = p3
    
    elif nombre_pelicula == p4["nombre"]:
        retorno = p4
    
    elif nombre_pelicula == p5["nombre"]:
        retorno = p5
    
    else:
        retorno = None
    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return retorno

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    
    retorno = 0
    
    d1 = p1["duracion"]
    d2 = p2["duracion"]
    d3 = p3["duracion"]
    d4 = p4["duracion"]
    d5 = p5["duracion"]
    
    if d1 > d2 and d1 >d3 and d1 > d4 and d1 > d5:
        retorno = p1
    
    elif d2 > d1 and d2 > d3 and d2 >d4 and d2 > d5:
        retorno = p2
    
    elif d3 > d1 and d3 > d2 and d3 >d4 and d3 > d5:
        retorno = p3
    
    elif d4 > d1 and d4 > d3 and d4 >d1 and d4 > d5:
        retorno = p4
    
    elif d5 > d1 and d5 > d3 and d5 >d4 and d5 > d1:
        retorno = p5
    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return retorno

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    retorno = 0
    
    d1 = p1["duracion"]
    d2 = p2["duracion"]
    d3 = p3["duracion"]
    d4 = p4["duracion"]
    d5 = p5["duracion"]
    
    x = d1 + d2 + d3 + d4 + d5
    
    y = 0
    
    if d1 > 0:
        y += 1
    
    if d2 > 0:
        y += 1
    
    if d3 > 0:
        y += 1
    
    if d4 > 0:
        y += 1
    
    if d5 > 0:
        y += 1
    
    
    retorno = x/y

    retorno_h = int(retorno // 60)
    retorno_m = int(retorno % 60)
    
    return str(retorno_h) +":"+ str(retorno_m)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    retorno = ""
    retorno_1 = ""
    retorno_2 = ""
    retorno_3 = ""
    retorno_4 = ""
    retorno_5 = ""
    
    
    d1 = p1["anio"]
    d2 = p2["anio"]
    d3 = p3["anio"]
    d4 = p4["anio"]
    d5 = p5["anio"]
    
    if d1 > anio:
        retorno_1 = p1["nombre"]
    
    if d2 > anio:
        retorno_2  = p2["nombre"]
    
    if d3 > anio:
        retorno_3 = p3["nombre"]
        
    if d4 > anio:
        retorno_4 = p4["nombre"]    
        
    if d5 > anio:
        retorno_5 = p5["nombre"]
    
    if retorno_1 !="":
        if retorno_2 !="":
            if retorno_3 !="":
                if retorno_4 !="":
                    if retorno_5 !="":
                        
                        retorno = retorno_1 + ","+ retorno_2 + "," + retorno_3 + "," + retorno_4 + "," + retorno_5
                    else:
                        retorno = retorno_1 + ","+ retorno_2 + "," + retorno_3 + "," + retorno_4
                
                else:
                    if retorno_5 !="":
                        
                        retorno = retorno_1 + ","+ retorno_2 + "," + retorno_3 + "," + retorno_5
                    else:    
                        retorno = retorno_1 + ","+ retorno_2 + "," + retorno_3 
            
            else: 
                if retorno_4 !="":
                    if retorno_5 !="":
                        
                        retorno = retorno_1 + ","+ retorno_2 + ","  + retorno_4 + "," + retorno_5
                    else:
                        retorno = retorno_1 + ","+ retorno_2 + ","  + retorno_4
                
                else:
                    if retorno_5 !="":
                        
                        retorno = retorno_1 + ","+ retorno_2 + "," + retorno_5
                    else:    
                        retorno = retorno_1 + ","+ retorno_2 
        else:
            if retorno_3 !="":
                if retorno_4 !="":
                    if retorno_5 !="":
                        
                        retorno = retorno_1 + ","+ retorno_3 + "," + retorno_4 + "," + retorno_5
                    else:
                        retorno = retorno_1 + ","+ retorno_3 + "," + retorno_4 
                
                else: 
                    if retorno_5 !="":
                        
                        retorno = retorno_1 + ","+ retorno_3 + "," + retorno_5
                    else:    
                        retorno = retorno_1 + ","+ retorno_3
            
            else:
                if retorno_4 !="":
                    if retorno_5 !="":
                        
                        retorno = retorno_1 + "," + retorno_4 + "," + retorno_5
                    else:
                        retorno = retorno_1 + "," + retorno_4
                
                else:
                    if retorno_5 !="":
                        
                        retorno = retorno_1 + "," + retorno_5
                    else:    
                        retorno = retorno_1 
    else:
        if retorno_2 !="":
            if retorno_3 !="":
                if retorno_4 !="":
                    if retorno_5 !="":
                        
                        retorno = retorno_2 + "," + retorno_3 + "," + retorno_4 + "," + retorno_5
                    else:
                        retorno = retorno_2 + "," + retorno_3 + "," + retorno_4
                
                else:
                    if retorno_5 !="":
                        
                        retorno = retorno_2 + "," + retorno_3 + "," + retorno_5
                    else:    
                        retorno =  retorno_2 + "," + retorno_3 
            
            else: 
                if retorno_4 !="":
                    if retorno_5 !="":
                        
                        retorno = retorno_2 + "," + retorno_4 + "," + retorno_5
                    else:
                        retorno = retorno_2 + ","  + retorno_4
                
                else:
                    if retorno_5 !="":
                        
                        retorno =  retorno_2 + "," + retorno_5
                    else:    
                        retorno =  retorno_2 
        else:
            if retorno_3 !="":
                if retorno_4 !="":
                    if retorno_5 !="":
                        
                        retorno = retorno_3 + "," + retorno_4 + "," + retorno_5
                    else:
                        retorno = retorno_3 + "," + retorno_4 
                
                else: 
                    if retorno_5 !="":
                        
                        retorno = retorno_3 + "," + retorno_5
                    else:    
                        retorno = retorno_3
            
            else:
                if retorno_4 !="":
                    if retorno_5 !="":
                        
                        retorno = retorno_4 + "," + retorno_5
                    else:
                        retorno = retorno_4
                
                else:
                    if retorno_5 !="":
                        
                        retorno = retorno_5
                    else:    
                        retorno = "Ninguna"
        
    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return retorno

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """

    
    d1 = p1["clasificacion"]
    d2 = p2["clasificacion"]
    d3 = p3["clasificacion"]
    d4 = p4["clasificacion"]
    d5 = p5["clasificacion"]
    
    
    y = 0
    
    if d1 == "18+":
        y += 1
    
    if d2 == "18+":
        y += 1
    
    if d3 == "18+":
        y += 1
    
    if d4 == "18+":
        y += 1
    
    if d5 == "18+":
        y += 1 
    return y


def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    retorno = 0
    
    g1 = peli["genero"]
    doc = "Documental"
    dra = "Drama"
    
    h1 = p1["hora"]
    h2 = p2["hora"]
    h3 = p3["hora"]
    h4 = p4["hora"]
    h5 = p5["hora"]
    
    d1 = p1["dia"]
    d2 = p2["dia"]
    d3 = p3["dia"]
    d4 = p4["dia"]
    d5 = p5["dia"]
    
    
    Preh_1 = int((p1["duracion"] // 60)*100)
    prem_1 = int(p1["duracion"] % 60)
    
    Preh_2 = int((p2["duracion"] // 60)*100)
    prem_2 = int(p2["duracion"] % 60)
    
    Preh_3 = int((p3["duracion"] // 60)*100)
    prem_3 = int(p3["duracion"] % 60)
    
    Preh_4 = int((p4["duracion"] // 60)*100)
    prem_4 = int(p4["duracion"] % 60)
    
    Preh_5 = int((p5["duracion"] // 60)*100)
    prem_5 = int(p5["duracion"] % 60)
    
    Preh_6 = int((peli["duracion"] // 60)*100)
    prem_6 = int(peli["duracion"] % 60)
    
    f1 = p1["hora"] + Preh_1 + prem_1
    f2 = p2["hora"] + Preh_2 + prem_2
    f3 = p3["hora"] + Preh_3 + prem_3
    f4 = p4["hora"] + Preh_4 + prem_4
    f5 = p5["hora"] + Preh_5 + prem_5
    f6 = nueva_hora + Preh_6 + prem_6
    
    if control_horario == False:
        if nuevo_dia == d1:
            if nueva_hora >= h1 and nueva_hora < f1 or nueva_hora < h1 and f6 > h1:
                retorno = False
            else:
                retorno = True
                
        elif nuevo_dia == d2:
            if nueva_hora >= h2 and nueva_hora < f2 or nueva_hora < h2 and f6 > h2:
                retorno = False
            else:
                retorno = True
                
        elif nuevo_dia == d3:
            if nueva_hora >= h3 and nueva_hora < f3 or nueva_hora < h3 and f6 > h3:
                retorno = False
            else:
                retorno = True
                
        elif nuevo_dia == d4:
            if nueva_hora >= h4 and nueva_hora < f4 or nueva_hora < h4 and f6 > h4:
                retorno = False
            else:
                retorno = True
                
        elif nuevo_dia == d5:
            if nueva_hora >= h5 and nueva_hora < f5 or nueva_hora < h5 and f6 > h5:
                retorno = False
            else:
                retorno = True
        elif nuevo_dia != d1 and nuevo_dia != d2 and nuevo_dia != d3 and nuevo_dia != d4 and nuevo_dia != d5:
            retorno = True
    
    if control_horario == True:
        if nuevo_dia == d1:
            if nueva_hora >= h1 and nueva_hora < f1 or nueva_hora < h1 and f6 > h1:
                retorno = False
            else:
                retorno = True
                
        elif nuevo_dia == d2:
            if nueva_hora >= h2 and nueva_hora < f2 or nueva_hora < h2 and f6 > h2:
                retorno = False
            else:
                retorno = True
                
        elif nuevo_dia == d3:
            if nueva_hora >= h3 and nueva_hora < f3 or nueva_hora < h3 and f6 > h3:
                retorno = False
            else:
                retorno = True
                
        elif nuevo_dia == d4:
            if nueva_hora >= h4 and nueva_hora < f4 or nueva_hora < h4 and f6 > h4:
                retorno = False
            else:
                retorno = True
                
        elif nuevo_dia == d5:
            if nueva_hora >= h5 and nueva_hora < f5 or nueva_hora < h5 and f6 > h5:
                retorno = False
            else:
                retorno = True
                
        if doc in g1:
            if dra in g1:
                if nuevo_dia == "Lunes" or nuevo_dia == "Martes" or nuevo_dia == "Miércoles" or nuevo_dia == "Jueves" or nuevo_dia == "Viernes":
                    if nueva_hora >= 2300 or nueva_hora < 600:
                        retorno = False
                    if nueva_hora >= 2200:
                        retorno = False
                    else:
                        retorno = True
                if nuevo_dia == "Viernes":
                    retorno = False
                else:
                    if nuevo_dia == d1:
                        if nueva_hora >= h1 and nueva_hora < f1 or nueva_hora < h1 and f6 > h1:
                            retorno = False
                        else:
                            retorno = True
                            
                    elif nuevo_dia == d2:
                        if nueva_hora >= h2 and nueva_hora < f2 or nueva_hora < h2 and f6 > h2:
                            retorno = False
                        else:
                            retorno = True
                            
                    elif nuevo_dia == d3:
                        if nueva_hora >= h3 and nueva_hora < f3 or nueva_hora < h3 and f6 > h3:
                            retorno = False
                        else:
                            retorno = True
                            
                    elif nuevo_dia == d4:
                        if nueva_hora >= h4 and nueva_hora < f4 or nueva_hora < h4 and f6 > h4:
                            retorno = False
                        else:
                            retorno = True
                            
                    elif nuevo_dia == d5:
                        if nueva_hora >= h5 and nueva_hora < f5 or nueva_hora < h5 and f6 > h5:
                            retorno = False
                        else:
                            retorno = True
            elif nuevo_dia == "Lunes" or nuevo_dia == "Martes" or nuevo_dia == "Miércoles" or nuevo_dia == "Jueves" or nuevo_dia == "Viernes":
                if nueva_hora >= 2300 or nueva_hora < 600:
                    retorno = False
                
            if nueva_hora >= 2200:
                retorno = False
            else:
                retorno = True
                
        elif dra in g1:
            
            if nuevo_dia == d1:
                if nueva_hora >= h1 and nueva_hora < f1 or nueva_hora < h1 and f6 > h1:
                    retorno = False
                else:
                    retorno = True
                        
            elif nuevo_dia == d2:
                if nueva_hora >= h2 and nueva_hora < f2 or nueva_hora < h2 and f6 > h2:
                    retorno = False
                else:
                    retorno = True
                        
            elif nuevo_dia == d3:
                if nueva_hora >= h3 and nueva_hora < f3 or nueva_hora < h3 and f6 > h3:
                    retorno = False
                else:
                    retorno = True
                        
            elif nuevo_dia == d4:
                if nueva_hora >= h4 and nueva_hora < f4 or nueva_hora < h4 and f6 > h4:
                    retorno = False
                else:
                    retorno = True
                        
            elif nuevo_dia == d5:
                if nueva_hora >= h5 and nueva_hora < f5 or nueva_hora < h5 and f6 > h5:
                    retorno = False
                else:
                    retorno = True
            elif nuevo_dia != d1 and nuevo_dia != d2 and nuevo_dia != d3 and nuevo_dia != d4 and nuevo_dia != d5:
                retorno = True
                
            if nuevo_dia == "Lunes" or nuevo_dia == "Martes" or nuevo_dia == "Miércoles" or nuevo_dia == "Jueves" or nuevo_dia == "Viernes":
                if nueva_hora >= 2300 or nueva_hora < 600:
                    retorno = False
                else:
                    retorno = True
            if nuevo_dia == "Viernes":
                retorno = False
            
            
            
                
        if doc not in g1 and dra not in g1:
            if nuevo_dia == "Lunes" or nuevo_dia == "Martes" or nuevo_dia == "Miércoles" or nuevo_dia == "Jueves" or nuevo_dia == "Viernes":
                if nueva_hora >= 2300 or nueva_hora < 600:
                    retorno = False
            elif nuevo_dia != d1 and nuevo_dia != d2 and nuevo_dia != d3 and nuevo_dia != d4 and nuevo_dia != d5:
                retorno = True
            
    return retorno

p1 = {'nombre': 'Sherk', 'genero': 'familiar', 'duracion': 120, 'anio': 2000, 'clasificacion': 'todos', 'hora': 1625, 'dia': 'Lunes'}
p2 = {'nombre': 'Shrek2', 'genero': 'Familiar, Comedia', 'duracion': 92, 'anio': 2001, 'clasificacion': 'Todos', 'hora': 1700, 'dia': 'Viernes'}
p3 = {'nombre': 'Get Out', 'genero': 'Suspenso, Terror', 'duracion': 104, 'anio': 2017, 'clasificacion': '18+', 'hora': 2330, 'dia': 'Sábado'}
p6 = {'nombre': 'Icarus', 'genero': 'Documental, Suspenso', 'duracion': 122, 'anio': 2017, 'clasificacion': '18+', 'hora': 800, 'dia': 'Domingo'}
p5 = {'nombre': 'Inception', 'genero': 'Acción, Drama', 'duracion': 148, 'anio': 2010, 'clasificacion': '13+', 'hora': 1300, 'dia': 'Lunes'}
p4 = {'nombre': 'The Empire Strikes Back', 'genero': 'Familiar, Ciencia-Ficción', 'duracion': 124, 'anio': 1980, 'clasificacion': '7+', 'hora': 1415, 'dia': 'Miércoles'}
nueva_hora = 2320
nuevo_dia = "Martes"
control_horario = True

print(reagendar_pelicula(p6, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5))

def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    retorno = False
    
    c1 = peli["clasificacion"]
    g1 = peli["genero"]
    terr = "Terror"
    doc = "Documental"
    fam = "Familiar"
    
    if edad_invitado >= 18:
        retorno = True
    elif edad_invitado < 18:
        if autorizacion_padres == True:
            if edad_invitado < 15:
                if terr in g1:
                    retorno = False
                else:
                    retorno = True
            if edad_invitado < 10:
                if fam in g1:
                    retorno = True
                else:
                    retorno = False
        elif autorizacion_padres == False:
            if doc in g1:
                retorno = True
            if doc not in g1:
                if c1 == "18+":
                    retorno = False
                elif c1 == "16+":
                    if edad_invitado > 16:
                        retorno = True
                    else:
                        retorno = False
                elif c1 == "13+":
                    if edad_invitado > 13:
                        retorno = True
                    else:
                        retorno = False
                elif c1 == "7+":
                    if edad_invitado > 7:
                        retorno = True
                    else:
                        retorno = False
                else:
                    retorno = True
            if edad_invitado < 15:
                if terr in g1:
                    retorno = False
                elif c1 == "13+":
                    if edad_invitado > 13:
                        retorno = True
                    else:
                        retorno = False
                elif c1 == "7+":
                    if edad_invitado > 7:
                        retorno = True
                    else:
                        retorno = False
                else:
                    retorno = True
            if edad_invitado < 10:
                if fam in g1:
                    if c1 == "7+":
                        if edad_invitado > 7:
                            retorno = True
                        else:
                            retorno = False
                    elif c1 == "Todos":
                        retorno = True
                else:
                    retorno = False

    return retorno









