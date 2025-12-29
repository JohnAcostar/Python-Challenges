import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

plt.rcParams.update({'font.size': 12})

def cargar_datos(nombre_archivo:str)->pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo CSV que se debe cargar
    Retorno:
        (DataFrame) : El DataFrame con todos los datos contenidos en el archivo
    """
    retorno = pd.read_csv(nombre_archivo)
    
    return retorno
        

def histograma_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe
        aparecer la cantidad de planetas descubiertos por anho.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    
    descubrir = datos["DESCUBRIMIENTO"]
    ax = descubrir.plot(kind = "hist",figsize=(10,4),bins = 30, title = "Cantidad de planetas descubiertos entre 1988 y 2018")
    ax.set_xlabel("Años")
    ax.set_ylabel("Cantidad de planetas descubiertos")
    fig = ax.get_figure()
    fig.savefig("histograma.svg")
    
    
def estado_publicacion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de publicacion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    desc_por_pub = datos[["DESCUBRIMIENTO", "ESTADO_PUBLICACION"]]
    ax = desc_por_pub.boxplot(by = "ESTADO_PUBLICACION", rot =90, figsize = (8,8))
    plt.title("Tipo de Publicación vs año de descubrimiento")
    plt.xlabel("Tipo de Ubicación")
    plt.ylabel("Año de Descubrimiento")
    plt.show()
    
def deteccion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de deteccion
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    desc_por_pub = datos[["DESCUBRIMIENTO", "TIPO_DETECCION"]]
    ax = desc_por_pub.boxplot(by = "TIPO_DETECCION", rot =90, figsize = (8,8))
    plt.title("Tipo de Detección vs año de descubrimiento")
    plt.xlabel("Tipo de Detección")
    plt.ylabel("Año de Descubrimiento")
    plt.show()

def deteccion_y_descubrimiento(datos:pd.DataFrame,anho:int)->None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un anho particular, clasificados de acuerdo
        con el tipo de publicacion.
        Si el anho es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
        anho (int): el anho para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
    

    if anho == 0:
        titulo = "Tipos de detección en todos los años"
        filtrar_dataframe = datos["TIPO_DETECCION"].unique()
    else:
        titulo = f"Tipos de detección en el año {anho}"
        filtrar_anho = datos[datos["DESCUBRIMIENTO"] == anho]
        filtrar_dataframe = filtrar_anho["TIPO_DETECCION"].unique()

    porcentaje = len(datos) if anho == 0 else len(filtrar_anho)

    graf = {}

    for i in filtrar_dataframe:
        cantidad = 0
        tipo = datos[datos["TIPO_DETECCION"] == i] if anho == 0 else filtrar_anho[filtrar_anho["TIPO_DETECCION"] == i]
        for j in range(0,len(tipo)):
            if tipo.iloc[j]["TIPO_DETECCION"] == i:
             cantidad += 1
             porcentaje_f = cantidad / porcentaje

        if i not in graf.keys():
            graf[i] = porcentaje_f

    plt.figure(figsize=(8, 8))

    plt.pie(graf.values(), labels=graf.keys(), autopct="%1.1f%%")

    plt.title(titulo, fontsize=16, color="black")
    plt.show()

def cantidad_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    agrupado = datos.groupby(['TIPO_DETECCION', 'DESCUBRIMIENTO']).size().reset_index(name='CANTIDAD')


    pivotado = agrupado.pivot(index='DESCUBRIMIENTO', columns='TIPO_DETECCION', values='CANTIDAD')

    plt.figure(figsize=(12, 8))

    for tipo_deteccion in pivotado.columns:
        plt.plot(pivotado.index, pivotado[tipo_deteccion], label=tipo_deteccion)

    plt.title('Cantidad de Planetas Descubiertos segun el Tipo de Detección')
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Cantidad de Planetas')
    plt.legend()
    plt.show()  
        
    
def masa_promedio_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """

    grafomt = pd.pivot_table(datos, values='MASA', index='DESCUBRIMIENTO', columns='TIPO_DETECCION', aggfunc=np.mean)

    ax_plot = grafomt.plot(figsize = (12,8))
    ax_plot.set_ylabel('Masa Promedio')
    ax_plot.set_xlabel('Año de Descubrimiento')
    ax_plot.set_title('Masa promedio de los planetas según el tipo de detección')
    ax_plot.legend()
     
    plt.show()
    

def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas. Cada punto en el diagrama correspondera
        a un planeta y estara ubicado de acuerdo con su masa y la masa de la
        estrella más cercana.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    ax = datos.plot(kind="scatter", x = "MASA", y = "MASA_ESTRELLA", figsize=(10,6), title = "Masa de los planetas vs. masa de la estrella más cercana"
                    , xlim=(-5,100), )
    
    plt.yscale('log')
    ax.set_xlabel("Masa del planeta")
    ax.set_ylabel("Masa de la estrella (log)")
    fig = ax.get_figure()
    fig.savefig("dispersion.svg")
    plt.title("Masa de los planetas vs. masa de la estrella más cercana")
    plt.xlabel("Masa del planeta")
    plt.ylabel("Masa de la estrella (log)")
    plt.show()
    
    
def graficar_cielo(datos:pd.DataFrame)->list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado
        para descubirlo.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
    colors={"Microlensing":[0.94,0.10,0.10], 
    "Radial Velocity":[0.1,0.5,0.94], 
    "Imaging":[0.34,0.94,0.10],
    "Primary Transit":[0.10,0.94,0.85], 
    "Other":[0.94,0.10,0.85], 
    "Astrometry":[0.94,0.65,0.10], 
    "TTV":[1.0,1.0,1.0]}
    
    datos["IMG_FILA"]=99-abs(np.sin(datos["RA"])*np.cos(datos["DEC"])*100)
    
    datos["IMG_COL"]=(np.cos(datos["RA"])*np.cos(datos["DEC"])*100)+100
    
    img = np.zeros([100,200,3])
    
    for index, row in datos.iterrows():
        pixrow=int(row["IMG_FILA"])
        pixcol=int(row["IMG_COL"])
        pixcolor=colors.get(row["TIPO_DETECCION"],[0,0,0])
        img[pixrow,pixcol,:]=pixcolor
        
        
    plt.imshow(img)
    plt.show()
    
    return img


def filtrar_imagen_cielo(imagen:list)->None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz
        [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    mascara = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    
    alto = len(imagen)
    ancho = len(imagen[0])
    
    imagen_nueva = [] 
    
    
    for filas in range(alto):
        columnas = [(0, 0, 0)] * ancho
        imagen_nueva.append(columnas)

    for i in range(alto):
        for j in range(ancho):
            suma_colores = [0.0, 0.0, 0.0]  
            suma_coef_mascara = 0.0 
            x = 0
            
            for fila in range(i-1, i+2):  
                y = 0
                
                for columna in range(j-1, j+2):  
                    if fila >= 0 and fila < alto and columna >= 0 and columna < ancho:
             
                        suma_colores[0] += (mascara[x][y] * imagen[fila][columna][0])
                        suma_colores[1] += (mascara[x][y] * imagen[fila][columna][1])
                        suma_colores[2] += (mascara[x][y] * imagen[fila][columna][2])
                        suma_coef_mascara += mascara[x][y]
                        
                    y += 1
                x += 1
            if suma_coef_mascara != 0:
                nuevo_r = suma_colores[0] / suma_coef_mascara  
                nuevo_g = suma_colores[1] / suma_coef_mascara  
                nuevo_b = suma_colores[2] / suma_coef_mascara    
            else:
               
                nuevo_r = suma_colores[0]   
                nuevo_g = suma_colores[1]
                nuevo_b = suma_colores[2]
            
            nuevo_pixel = (nuevo_r, nuevo_g, nuevo_b)  
            imagen_nueva[i][j] = nuevo_pixel  
    
    plt.imshow(imagen_nueva)
    plt.show()
    



