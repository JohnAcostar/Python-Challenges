"""
Ejercicio nivel 4: Rendimiento de cultivos en Colombia
Modulo de funciones.

@author: Cupi2
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Parte 1, Data frame crear

def cargar_datos(archivo:str)->pd.DataFrame:
    
    Col= pd.read_csv(archivo)
    
    return Col

#Parte 2, requerimiento 1 Análisis de la distribución de los datos

def piechart_tipo_cultivo (dataframe:pd.DataFrame, dpto:str) -> None:
    
    titulo= "Distribución de toneladas por tipo de cultivo en " + str(dpto)
    
    colores= ["purple", "red", "orange", "blue", "green", "pink", "brown", ]
    
    filtrar_dpto = dataframe[dataframe["Departamento"].isin([dpto])]
    
    filtrar_dataframe= filtrar_dpto["Tipo_Cultivo"].unique()
    
    porcentaje = len(filtrar_dpto)
    
    graf = {}
    
    for i in filtrar_dataframe:
        tipo = filtrar_dpto[filtrar_dpto["Tipo_Cultivo"] == i]
        cantidad = 0
        for j in range(0, len(tipo)):
            cantidad += tipo.iloc[j]["Toneladas"]
        porcentaje_f = cantidad / porcentaje
        
        if i not in graf.keys():
           graf[i] = porcentaje_f 
    
    plt.figure(figsize=(9,6))
    
    plt.pie(graf.values(), labels= graf, autopct= "%.1f%%", colors= colores, )

    plt.title(titulo, fontsize=16, color = "black")
    plt.show()
    
    
#Requerimiento 2 Top 10

def diagrama_barras(dataframe:pd.DataFrame)->None:
    
    barr = {}
    titulo = "Top 10 de cultivos con mayor cantidad de toneladas cosechadas por hectárea"

    for cultivo in dataframe["Cultivo"].unique():
        cultivo_data = dataframe[dataframe["Cultivo"] == cultivo]
        total_toneladas = cultivo_data["Toneladas"].sum()
        total_hectareas = cultivo_data["Hectareas_cosechadas"].sum()

        barr[cultivo] = total_toneladas / total_hectareas

    
    final = pd.DataFrame(list(barr.items()), columns=["Cultivo", "Toneladas cosechadas X Hectáreas"])
    final = final.sort_values(by="Toneladas cosechadas X Hectáreas", ascending=False).head(10)

    # Plot the bar chart
    plt.figure()
    plt.bar(final["Cultivo"], final["Toneladas cosechadas X Hectáreas"], color="palegreen")
    plt.title(titulo, fontsize=16, color="black")
    plt.xlabel("Cultivo")
    plt.ylabel("Toneladas cosechadas x Hectáreas")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.show()


#Requerimiento 3: Caja y bigotes de las toneladas

def toneladas_tipo_cultivo(dataframe:pd.DataFrame, limite_inf:int ,limite_sup:int)->None:
    
    filtrar = dataframe[(dataframe['Toneladas'] >= limite_inf) & (dataframe['Toneladas'] <= limite_sup)]

# Create a boxplot for the tons produced by each type of crop
    plt.figure(figsize=(12, 6))
    ax = sns.boxplot(x='Tipo_Cultivo', y='Toneladas', data=filtrar, palette='viridis')
    ax.set_title("|Toneladas producidas por tipo de cultivo", fontsize=16)
    ax.set_xlabel('Tipo de Cultivo', fontsize=14)
    ax.set_ylabel('Toneladas', fontsize=14)
    ax.tick_params(axis='x', rotation=45, labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    plt.tight_layout()

    plt.show()

#Parte 3, Estudiar la producción en toneladas por departamento


def crear_matriz(dataframe: pd.DataFrame)->pd.DataFrame:
    #Esqueleto diccionarios

    deptos =  sorted(dataframe["Departamento"].unique())
    dept_dict = dict(list(enumerate(deptos)))

    tipos_cultivos =  sorted(dataframe["Tipo_Cultivo"].unique())
    tipos_cultivos_dict = dict(list(enumerate(tipos_cultivos)))
    
    matrix = pd.DataFrame(columns= tipos_cultivos)
    for i in dept_dict.values():
        filtrar = dataframe[dataframe["Departamento"] == i]
        for j in tipos_cultivos_dict.values():
            cantidad = filtrar[filtrar["Tipo_Cultivo"] == j]["Toneladas"].sum()
            matrix.loc[i, j] = cantidad
            
    return matrix, tipos_cultivos, dept_dict

    #TODO completar la construcción de la matriz

#Requerimiento 5: Contar la cantidad total

def cantidad_toneladas_departamento(matriz: tuple, dpto:str)->int:
    matriz_1 = matriz[0]
    x = dpto
    filtrar = matriz_1[matriz_1.index == x]
    colum = filtrar.sum()
    return int(colum.sum())

#Requerimiento 6: Encontrar el departamento mayor o menor productor

def depto_mayor_o_menor_productor(matrix_1:tuple, parametro:bool, tipo:str)->tuple:
    (matrix, tipos_cultivos_dict, dept_dict) = matrix_1
    filtrar = matrix[tipo]
    
    if parametro == True:
        organizacion = filtrar.sort_values(ascending=False)
        retorno = organizacion.head(1)
        retorno_2 = retorno[0]
        dpto = retorno.index[0]
        
    elif parametro == False:
        
        ceros = filtrar[filtrar!=0]
        organizacion = ceros.sort_values(ascending=False)
        retorno = organizacion.tail(1)
        retorno_2 = retorno[0]
        dpto = retorno.index[0]
        
    return (dpto, retorno_2)

#requerimiento 7 Encontrar departamento productor estrella dado

def funcion(matriz:pd.DataFrame, dpto:str, cantidad:int)-> tuple:
    
    lis = []
    tipaje = matriz.loc[dpto]
    filtrar = matriz.loc[dpto]
    for i in tipaje:
        if filtrar[i] > cantidad:
            lis.append(i)
    return len(lis) >=3, lis[:3]

        
    

def departamento_estrella(matriz:tuple, cantidad:int)->dict:
    matrix = matriz[0]
    dpto = matriz[2]
    
    dictt = {}
    retorno = {}
    auxiliar = {}
    
    for municipio in dpto.values():
        (boolean, lista) = funcion(matrix, municipio, cantidad)
        if boolean:
            dictt[municipio] = lista
    if dictt:
        retorno["depto"] = list(dictt.keys())[0]
        retorno["tipos"] = list(dictt.values())[0]
    else:
        retorno["depto"] = "Ninguno"
        retorno["tipos"] = []
        
    return retorno

import matplotlib.image as mpimg
map_image = mpimg.imread("mapa.png")

def coordenadas(file_name: str) -> dict:
    deptos = {}
    with open(file_name, encoding="utf8") as file:
        titles = file.readline()
        line = file.readline()
        while len(line) > 0:
            line = line.strip()
            data = line.split(";")
            deptos[data[0]] = (int(data[1]), int(data[2]))
            line = file.readline()
    return deptos

coordinates_dict = coordenadas("coordenadas.txt")

def color(value: int) -> list:
    if value < 10:
        return [0.94, 0.10, 0.10]  
    elif value < 100:
        return [0.94, 0.10, 0.85]  
    elif value < 1000:
        return [0.10, 0.50, 0.94]  
    elif value < 100000:
        return [0.34, 0.94, 0.10]  
    else:
        return [0.99, 0.82, 0.09]  
    

import matplotlib.patches as mpatches

def cultivo_en_mapa(map_image, coordinates, production_data, crop_type):
    plt.imshow(map_image)

    legends = []
    for i in production_data:
        colors = color(production_data[i])
        legends.append(mpatches.Patch(color=colors, label=i))
        x, y = coordinates[i]
        map_image[x - 6: x + 7, y - 6: y + 7] = color

    plt.legend(handles=legends, loc=3, fontsize='x-small')
    plt.title("producción en toneladas de" + crop_type, fontsize='x-small')
    plt.show()
            
            





    
    
    