# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 06:50:02 2023

@author: ja.acostar1
"""
def calcular_precio_pollo_adicional(gramos_de_pollo:float,valor_cada_gramo:float)->float:
    
    valor = gramos_de_pollo * valor_cada_gramo
    
    return valor

def calcular_precio_salchicha_adicional(num_salchicha:int)->int:
    
    costo_salchica = num_salchicha * 350
    
    return costo_salchica

def calcular_precio_hogao_adicional(num_cucharadas:float)->float:
    
    onzas = num_cucharadas * 0.8
    
    precio = onzas * 50
    
    return precio