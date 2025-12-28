# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 00:15:20 2023

@author: john2
"""

import calculadora_indices as calc

print("En esta Funcion se va a calcular el rango de calorias que una persona debe consumir diariamente en caso de que deseea adelgazar "+"\n")

peso = float(input("Ingrese el peso de la persona en Kilogramos(Kg): "+"\n"))

altura = float(input("Ingrese la altura de la persona en centímetros(cm): "+"\n"))

edad = int(input("Ingrese la edad de la persona(en años): "+"\n"))

valor_genero = float(input("Ingrese el valor de 5 en caso de ser hombre y -161 en caso de ser mujer: "+"\n\n"))



rango = str(calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero))

