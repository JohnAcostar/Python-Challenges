# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:03:14 2023

@author: john2
"""

import calculadora_empanadas as emp

def ejecutar_rentabilidad()->None: 
    
    print("Calcular cuánto se está ganando por cada empanada vendida a partir de su costo de fabricación y su precio de venta."+"\n\n")
    
    precio_venta = float(input("Ingrese el precio de venta de una empanda: "))
    precio_carne = int(input("Ingrese el precio de la carne por kg: "))
    precio_papa = int(input("Ingrese el precio de la papa por libra: "))
    precio_aceite = int(input("Ingrese el precio del aceite por litro: "))
    
    rentabilidad = emp.calcular_rentabilidad(precio_venta, precio_carne, precio_papa, precio_aceite)
    
    print ("\nLa ganancia neta de una única empanada es: " + str(rentabilidad))
    
ejecutar_rentabilidad()