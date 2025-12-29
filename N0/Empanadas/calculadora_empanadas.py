# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 09:58:43 2023

@author: john2
"""

import math

def calcular_costo_empanada(precio_carne:int, precio_papa:int,precio_aceite:int)->float:
    
    costo = (2.5*precio_carne + 3*precio_papa + precio_aceite)/50
    
    re_costo = round(costo,2)
    
    return re_costo
    
def calcular_tiempo_coccion_lote_empanadas(tiempo_por_empanada:int, cantidad_empanadas:int)->int:
    
    tiempo = tiempo_por_empanada * cantidad_empanadas
    
    return tiempo

def calcular_rentabilidad(precio_venta:float, precio_carne:int, precio_papa:int, precio_aceite:int)->float:
    
    precio_total = calcular_costo_empanada(precio_carne, precio_papa, precio_aceite)
    
    rentabilidad = precio_venta - precio_total
    
    return round(rentabilidad,2)

def calcular_cantidad_empanadas_meta(arriendo:float, numero_empleados:int, precio_venta:float, precio_carne:int, precio_papa:int,precio_aceite)->int:
    
    renta = calcular_rentabilidad(precio_venta, precio_carne, precio_papa, precio_aceite)
    
    meta = (arriendo + numero_empleados * 45000)/ renta
    
    return math.floor(meta)

def calcular_precio_venta_promocion(precio_venta_unidad:float, cantidad_empanadas:int)->str:
    
    precio_final = int(((cantidad_empanadas//5)*3 +(cantidad_empanadas % 5)) * precio_venta_unidad)
    
    return ("\n\nEl precio de venta en promoción de "+ str(cantidad_empanadas) + " empanadas sería de $" + str(precio_final))
    
    
    
    