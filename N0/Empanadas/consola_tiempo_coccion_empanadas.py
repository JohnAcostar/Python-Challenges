# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 9:52:20 2023

@author: john2

"""
import calculadora_empanadas as emp

def ejecutar_tiempo_coccion_lote_empanadas()->None: 
    
    print("Calcular cuánto tiempo tardarían en cocinarse una cantidad determinada de empanadas a partir del tiempo que tarda una única empanada."+"\n\n")
    
    tiempo_por_empanada = int(input("Ingrese el tiempo por cada empanada: "))
    cantidad_empanadas = int(input("Ingrese la cantidad de empanadas: "))
    
    lote = emp.calcular_tiempo_coccion_lote_empanadas(tiempo_por_empanada, cantidad_empanadas)
    
    print ("\n"+ str(cantidad_empanadas) + " empanadas tardarian " + str(lote) + " unidades de tiempo en cocinarse.")

ejecutar_tiempo_coccion_lote_empanadas()