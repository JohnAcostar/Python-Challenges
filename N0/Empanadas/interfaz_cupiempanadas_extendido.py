# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 06:50:01 2023

@author: ja.acostar1
"""

import cupiempanadas_extendido as ext
import calculadora_empanadas as emp

def consola_costo_empanada_extendido()->None:

     print("Calcular el costo final de una empanada con las adiciones de pollo, salchicha y hogao."+"\n\n")
     
     precio_carne = int(input("Ingrese el precio de la carne por kg: "))
     precio_papa = int(input("Ingrese el precio de la papa por libra: "))
     precio_aceite = int(input("Ingrese el precio del aceite por litro: "))
     
     costo_base_empanada = emp.calcular_costo_empanada(precio_carne, precio_papa, precio_aceite)
     
     gramos_de_pollo = float(input("Ingrese los gramos de pollo: "))
     valor_cada_gramo = float(input("Ingrese el valor de cada gramo de pollo: "))
     
     num_salchicha = int(input("Ingrese el numero de salchicas: "))
     
     num_cucharadas = float(input("Ingrese el numero de cucharadas de hogao: "))
     
     pollo_adicional = ext.calcular_precio_pollo_adicional(gramos_de_pollo, valor_cada_gramo)
     
     salchica_adicional = ext.calcular_precio_salchicha_adicional(num_salchicha)
     
     hogao_adicional = ext.calcular_precio_hogao_adicional(num_cucharadas)
     
     costo_final = costo_base_empanada + pollo_adicional + salchica_adicional + hogao_adicional
     
     redondeo = round(costo_final,1)
     
     print ("\nEl precio total de una empanada con " + str(gramos_de_pollo) +" gramos de pollo, "+ str(num_salchicha) + " salchicas y " + str(num_cucharadas) + " cucharadas de hogao es: ",redondeo)
     
consola_costo_empanada_extendido()     
     