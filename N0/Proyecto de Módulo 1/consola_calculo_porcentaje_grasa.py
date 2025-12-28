# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 00:15:12 2023

@author: john2
"""

import calculadora_indices as calc

print("En esta Funcion se va a calcular el porcentaje de grasa (%GC) de una persona"+"\n")

peso = float(input("Ingrese el peso de la persona en Kilogramos(Kg): "+"\n"))

altura = float(input("Ingrese la altura de la persona en Metros(M): "+"\n"))

edad = int(input("Ingrese la edad de la persona(en años): "+"\n"))

valor_genero = float(input("Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: "+"\n\n"))

GC = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)

print ("La cantidad de calorías que la persona quema en reposo es: ",GC, "%")