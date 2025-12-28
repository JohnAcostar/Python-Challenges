# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 00:15:16 2023

@author: john2
"""

import calculadora_indices as calc

print("En esta Funcion se va a calcular la cantidad de calorias que una persona quema estando en reposo a travez de la tasa metabolica basal (TMB)"+"\n")

peso = float(input("Ingrese el peso de la persona en Kilogramos(Kg): "+"\n"))

altura = float(input("Ingrese la altura de la persona en centímetros(cm): "+"\n"))

edad = int(input("Ingrese la edad de la persona(en años): "+"\n"))

valor_genero = int(input("Ingrese el valor de 5 en caso de ser hombre y -161 en caso de ser mujer: "+"\n\n"))

TMB = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print ("La cantidad de calorías que la persona quema en reposo es: ",TMB,"cal")