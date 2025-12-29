# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 07:23:44 2023

@author: john2
"""

import calculadora_empanadas as emp

def ejecutar_costo_empanada()->None: 

    print("Calcular cuánto costaría hacer una empanada a partir del costo de cada uno de sus ingredientes."+"\n\n")
    
    precio_carne = int(input("Ingrese el precio de la carne por kg: "))
    precio_papa = int(input("Ingrese el precio de la papa por libra: "))
    precio_aceite = int(input("Ingrese el precio del aceite por litro: "))
    
    costo = emp.calcular_costo_empanada(precio_carne, precio_papa, precio_aceite)
    
    print ("\nEl costo de fabricar una única empanada es: ",costo)

ejecutar_costo_empanada()