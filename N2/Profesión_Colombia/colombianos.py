# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22:23:06 2023

@author: john2
"""

import datetime 
def cargar_datos(datos:str)->dict:
    archivo= open(datos, "r")
    linea = archivo.readline()
    colombianos  = []
    
    for linea in archivo:
        
        dato =linea.split(",")
        persona = {}
        persona["nombre"] = dato[0]
        persona["genero"] = dato[1]
        persona["anio_nacimiento"] = int(dato[2])
        persona["anio_muerte"] = int(dato[3])
        persona["ocupacion"] = dato[4]
        persona["ciudadania"] = dato[5]
        persona["numero_lectores"] = int(dato[6])
        
        colombianos.append(persona)
        
    ocupaciones = []
    
    for i in colombianos:
        if i["ocupacion"] not in ocupaciones:
            ocupaciones.append(i["ocupacion"])
    
    por = {}
    for ocupacion in ocupaciones:
        personas = []
        for colombiano in colombianos:
           if colombiano["ocupacion"] == ocupacion:
               personas.append(colombiano)
        por[ocupacion] = personas
        
        
    archivo.close()
    return por


def mayor_lectores(diccionario:dict)->str:
    
    retorno  = ""
    mayor = 0
    for cadacomp in diccionario.keys():
        for persona in diccionario[cadacomp]:
            
            if persona["numero_lectores"] > mayor:
                mayor = persona["numero_lectores"]
                retorno = persona["nombre"]
                
    return retorno

def hay_3_colombianos (diccionario:dict, ocupacion:str, genero:str, num_lectores:int)->bool:
    
    contador = 0

    for persona in diccionario[ocupacion]:
        if (persona["genero"] == genero) and (persona["numero_lectores"]> num_lectores):
                contador += 1
    if contador >= 3:
        return True

    return False

def promedio_lectores(diccionario:dict, ocupacion:str)->float:
    
    total_lectores = 0
    num_colombianos = len(diccionario[ocupacion])
    
    for colombiano in diccionario[ocupacion]:
        
        total_lectores += colombiano["numero_lectores"]
        
    promedio = total_lectores / num_colombianos
    return (round(promedio, 2))


def mayor_rating(diccionario: dict)->str:
    
    ocupacion  = ""
    mayor = 0
    for cadacomp in diccionario.keys():
        for persona in diccionario[cadacomp]:
            prom = promedio_lectores(diccionario, cadacomp)
            if prom > mayor:
                mayor = prom
                ocupacion = cadacomp
                
    return ocupacion

def colombianos_rango(diccionario:dict,ocupacion:str,menor:int,mayor:int)->list:
    
    lista = []
    for persona in diccionario[ocupacion]:
        if persona["anio_nacimiento"] >= menor and persona["anio_nacimiento"] <= (mayor):
            lista.append(persona)

    return lista

def nacionalidades (diccionario:dict)->dict:
    new_dict = {}
    for cadacomp in diccionario.values():
        for persona in cadacomp:
            if persona["ciudadania"] not in new_dict:
                new_dict[persona["ciudadania"]] = 1
            else:
                new_dict[persona["ciudadania"]] += 1
                
    return new_dict


def calcular_edad(diccionario:dict)->dict:
    
    for cadacomp in diccionario.values():
        for persona in cadacomp:
            if persona["anio_muerte"] != 0:
                edad = persona["anio_muerte"] - persona["anio_nacimiento"] 
            else:
                currentDateTime = datetime.datetime.now()
                date = currentDateTime.date()
                year = int(date.strftime("%Y"))
                
                edad = year - persona["anio_nacimiento"]
            persona["edad"] = edad
        
    return diccionario


def colombianos_fallecidos (diccionario:dict)->dict: 
    lista_muerto = []
    ocupaciones_muerto = []
    for cadacomp in diccionario.values():
        for persona in cadacomp:
            if persona["anio_muerte"] != 0:
                lista_muerto.append(persona)
                if persona["ocupacion"] not in ocupaciones_muerto:
                    ocupaciones_muerto.append(persona["ocupacion"])
    muertos = {}
    for ocupacion in ocupaciones_muerto:
         personas = []
         for muerto in lista_muerto:
            if muerto["ocupacion"] == ocupacion:
                personas.append(muerto)
         muertos[ocupacion] = personas
         
    return muertos
        
    
    
    