# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:02:44 2023

@author: john2
"""

import calculadora_empanadas as emp

def ejecutar_precio_venta_promocion()->None: 
    
    print("Dar un mensaje con el precio de venta total en promoción de una cantidad de empanadas suponiendo que la promoción es “pague 3 y lleve 5""."+"\n")
    
    cantidad_empanadas = int(input("Ingrese la cantidad de empanadas: "))
    precio_venta_unidad = float(input("Ingrese el precio de venta de una empanda: "))
    
    promocion = emp.calcular_precio_venta_promocion(precio_venta_unidad, cantidad_empanadas)
    
    print (promocion)
    
ejecutar_precio_venta_promocion()