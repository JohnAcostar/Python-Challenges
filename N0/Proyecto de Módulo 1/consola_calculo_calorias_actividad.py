# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 00:15:18 2023

@author: john2
"""

import calculadora_indices as calc

print("En esta Funcion se va a calcular la cantidad de calorias que una persona quema al realizar algun tipo de actividad física "+"\n")

peso = float(input("Ingrese el peso de la persona en Kilogramos(Kg): "+"\n"))

altura = float(input("Ingrese la altura de la persona en centímetros(cm): "+"\n"))

edad = int(input("Ingrese la edad de la persona(en años): "+"\n"))

valor_genero = float(input("Ingrese el valor de 5 en caso de ser hombre y -161 en caso de ser mujer: "+"\n"))

valor_actividad = float(input(""""Ingrese el valor correspondiente a su nivel de actividad fisica semanal: \n\n 
• 1.2: poco o ningún ejercicio
• 1.375: ejercicio ligero (1 a 3 días a la semana)
• 1.55: ejercicio moderado (3 a 5 días a la semana)
• 1.725: deportista (6 -7 días a la semana)
• 1.9: atleta (entrenamientos mañana y tarde) \n\n""" ))

TMB_actividad_fisica = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print ("La cantidad de calorías que una persona quema, al realizar algún tipo de actividad física semanalmente es: ",TMB_actividad_fisica,"cal")