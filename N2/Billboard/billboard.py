# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:08:45 2023

@author: john2
"""

def cargar_canciones(datos:str)->list:
    archivo = open(datos, "r")
    cancion = archivo.readline()
    canciones = []

    for cancion in archivo:
        
        
        titulos = cancion.split(",")
        
        lista_cancion = {}
        lista_cancion["posicion"] = int(titulos[0])
        lista_cancion["nombre_cancion"] = titulos[1]
        lista_cancion["nombre_artista"] = titulos[2]
        lista_cancion["anio"] = int(titulos[3])
        lista_cancion["letra"] = titulos[4]
        
        canciones.append(lista_cancion)
    
    return canciones



def buscar_cancion(lista:list,nombre:str,año:int)->dict:
    retorno = {}
    
    for cancion in lista:
        if cancion["nombre_cancion"] == nombre and cancion["anio"] == año:
            retorno = cancion
        
    if retorno == {}:
        retorno = None
        
    return retorno


lista = [{"nombre_cancion":"radioactive", "anio":2013}]

def canciones_anio(lista:list,año:int)->list:
    
    retorno = []
    
    for cancion in lista:
        new_dict = {}
        if cancion["anio"] == año:
            new_dict["posicion"] = int(cancion["posicion"])
            new_dict["nombre_cancion"] = (cancion["nombre_cancion"])
            new_dict["nombre_artista"] = (cancion["nombre_artista"])
            new_dict["anio"] = int(cancion["anio"])
            retorno.append(new_dict)
    
    return retorno

def canciones_artista_periodo(lista:list,nombre:str,menor:int,mayor:int)->list:
    
    retorno = []
    
    for cancion in lista:
        new_dict = {}
        if cancion["nombre_artista"] == nombre and cancion["anio"] >= menor and cancion["anio"] <= mayor:
            new_dict["posicion"] = int(cancion["posicion"])
            new_dict["nombre_cancion"] = (cancion["nombre_cancion"])
            new_dict["nombre_artista"] = (cancion["nombre_artista"])
            new_dict["anio"] = int(cancion["anio"])
            retorno.append(new_dict)
    
    return retorno
            
def todas_canciones_artista(lista:list,nombre:str)->list:
    
    retorno = []
    
    for cancion in lista:
        new_dict = {}
        if cancion["nombre_artista"] == nombre:
            new_dict["posicion"] = int(cancion["posicion"])
            new_dict["nombre_cancion"] = (cancion["nombre_cancion"])
            new_dict["nombre_artista"] = (cancion["nombre_artista"])
            new_dict["anio"] = int(cancion["anio"])
            retorno.append(new_dict)
            
    return retorno

def todos_artistas_cancion(lista:list,nombre:str)->list:
    
    retorno = []
    
    for cancion in lista:
        if cancion["nombre_cancion"] == nombre:
            retorno.append(cancion["nombre_artista"])
            
    return retorno

def artistas_mas_populares(lista:list, valor:int)->dict:
    
    retorno = {}
    artistas = {}
    for cancion in lista:
        tope = 0
        if cancion["nombre_artista"] not in artistas:
            tope = 1
            artistas[cancion["nombre_artista"]] = tope
        elif cancion["nombre_artista"] in artistas:
            artistas[cancion["nombre_artista"]] += 1
        
        if artistas[cancion["nombre_artista"]] > valor:
            retorno[cancion["nombre_artista"]] =  artistas[cancion["nombre_artista"]]
    return retorno
    
    
def artista_estrella(lista:list)->dict:
    
    retorno = {}
    artistas = {}
    valor = 0
    final = ""
    for cancion in lista:
        tope = 0
        if cancion["nombre_artista"] not in artistas:
            tope = 1
            artistas[cancion["nombre_artista"]] = tope
        elif cancion["nombre_artista"] in artistas:
            artistas[cancion["nombre_artista"]] += 1
        
        if artistas[cancion["nombre_artista"]] > valor:
            valor = artistas[cancion["nombre_artista"]]
            final = cancion["nombre_artista"]
    
    retorno[final] = valor
    
    return retorno
    
def artistas_y_sus_canciones(lista:list)->dict:
    

    artistas = {}
    for cancion in lista:
        if cancion["nombre_artista"] not in artistas:
            list_canciones = [cancion["nombre_cancion"]]
            artistas[cancion["nombre_artista"]] = list_canciones
        elif cancion["nombre_artista"] in artistas:
            if cancion["nombre_cancion"] not in artistas[cancion["nombre_artista"]]:
                artistas[cancion["nombre_artista"]].append(cancion["nombre_cancion"])
    
    return artistas
    
    
def promedio_canciones_por_artista(lista:list)->float:
    
    valor = 0
    retorno = {}
    artistas = {}
    canciones = {}
    for cancion in lista:
        tope = 0
        if cancion["nombre_artista"] not in artistas:
            tope = 1
            artistas[cancion["nombre_artista"]] = tope
            list_canciones = [cancion["nombre_cancion"]]
            canciones[cancion["nombre_artista"]] = list_canciones
        elif cancion["nombre_artista"] in artistas:
            if cancion["nombre_cancion"] not in canciones[cancion["nombre_artista"]]:
                canciones[cancion["nombre_artista"]].append(cancion["nombre_cancion"])
                artistas[cancion["nombre_artista"]] += 1
        
        if artistas[cancion["nombre_artista"]] > valor:
            retorno[cancion["nombre_artista"]] =  artistas[cancion["nombre_artista"]]
            
            
    can_total_canciones = 0
    can_total_artistas = len(retorno)

    for cancion2 in retorno.values():
          
        can_total_canciones += cancion2
    
    promedio = can_total_canciones/can_total_artistas
        
    return promedio

        

            
            