# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:45:25 2023

@author: john2
"""

def calcular_IMC(peso:float, altura:float)->float:
    
    "En esta Funcion se va a calcular el indice de masa corporal IMC"
    IMC = peso/(altura)**2
    return round(IMC,2)

def calcular_porcentaje_grasa(peso:float, altura:float,edad:int,valor_genero:float)->float:
    
    "En esta Funcion se va a calcular el porcentaje de grasa"
    IMC = peso/(altura)**2
    GC = 1.2 *IMC + 0.23 * edad - 5.4 - valor_genero
    return round(GC,2)

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int,valor_genero:int)->float:
    
    "En esta Funcion se va a calcular la cantidad de calorias que una persona quema estando en reposo"   
    TMB = (10 *peso) + (6.25 * altura) - (5 * edad ) + valor_genero
    return round(TMB,2)


def calcular_calorias_en_actividad(peso:float, altura:float,edad:int,valor_genero:float,valor_actividad:float)->float:
    
    "En esta Funcion se va a calcular la cantidad de calorias que una persona quema al realizar algun tipo de actividad física"   
    TMB = (10 *peso) + (6.25* altura) - (5*edad ) + valor_genero    
    Actividad = TMB * valor_actividad
    
    return round(Actividad,2)

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:float)->str:
    
    "En esta Funcion se va a calcular el rango de calorias que una persona debe consumir diariamente en caso de que deseea adelgazar"     
    calrecmin = ((10*peso)+(6.25*altura)-(5*edad)+valor_genero)*0.80
    
    calrecmax = ((10*peso)+(6.25*altura)-(5*edad)+valor_genero)*0.85
    
    
    return print("Para adelgazar es recomendado que consumas entre: ",round(calrecmin,2),"y",round(calrecmax,2),"calorias al día.\nSiendo",round(calrecmin,2),"el rango inferior y",round(calrecmax,2),"el rango superior")
    
