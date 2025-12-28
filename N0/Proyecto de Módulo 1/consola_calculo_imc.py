# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 00:15:08 2023

@author: john2
"""

import calculadora_indices as calc

print("En esta Funcion se va a calcular el indice de masa corporal (IMC) de una persona"+"\n")

peso = float(input("Ingrese el peso de la persona en Kilogramos(Kg): "+"\n"))

altura = float(input("Ingrese la altura de la persona en Metros(M): "+"\n\n"))


IMC = calc.calcular_IMC(peso, altura)

print("El índice de masa corporal de la persona es: ",IMC)
    
    