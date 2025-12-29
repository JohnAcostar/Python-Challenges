# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:43:57 2023

@author: john2
"""

import calculadora_empanadas as emp

def ejecutar_meta()->None: 

    print("Calcular cuántas empanadas se deben hacer para lograr la meta establecida, esto según el precio de venta de las empanadas y teniendo en cuenta el costo de fabricación."+"\n")
    
    
    arriendo = float(input("Ingrese el valor diario del arriendo del local: "))
    numero_empleados = int(input("Ingrese el numero de empleadps en turno: "))
    precio_venta = float(input("Ingrese el precio de venta de una empanda: "))
    precio_carne = int(input("Ingrese el precio de la carne por kg: "))
    precio_papa = int(input("Ingrese el precio de la papa por libra: "))
    precio_aceite = int(input("Ingrese el precio del aceite por litro: "))
    
    meta = emp.calcular_cantidad_empanadas_meta(arriendo, numero_empleados, precio_venta, precio_carne, precio_papa, precio_aceite)
    
    print ("\nLa Cantidad de empanadas necesarias para cumplir la meta es: ",meta)
        
ejecutar_meta()