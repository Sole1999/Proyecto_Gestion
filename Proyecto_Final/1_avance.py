import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
from pandas.plotting import scatter_matrix

filename = 'dataset/nearest-earth-objects(1910-2024).csv'
data = pd.read_csv(filename)

numeric_data = data.select_dtypes(include=['number'])

#Imprimir todos los datos
def print_all_data():
    print(data)

#Imprimir las primeras n filas
def print_first_rows(n):
    print(data.head(n))

#Imprimir la dimensi+on del df (Dataframe)
def print_dimensions():
    print(data.shape)


#Imprimir los tipos de datos
def print_data_types():
    print(data.dtypes)


#Calcular la cantidad de datos por clase (columna)
def count_data_by_class():
    class_count = data.groupby('Outcome').size()
    print (class_count)


#Resumen general de la dataset
def summary():
    print(data.describe())


def correlation():
    
    
    correlations = numeric_data.corr(method='pearson')
    print(correlations)


def skew(): #sesgo
    a = numeric_data.skew()
    print(a)
    


def densidad_matriz():
#Código básico para graficar
    fig = plt.figure(figsize=(6,6))
    ax = fig.gca()
    #Código para graficar una matriz de dispersión
    numeric_data.plot(ax=ax, kind='density', subplots=True, layout=(3,3), sharex=False)
    plt.show()


def Matriz_del_diagrama_de_caja():
    #Código básico para graficar
    fig = plt.figure(figsize=(12,12))
    ax = fig.gca()
    #Código para graficar una matriz de un diagrama de caja
    data.plot(ax=ax, kind='box', subplots=True, layout=(6,6), sharex=False)
    plt.show()
  
# Crear el box plot para 'price' por categoría de producto, por ejemplo 'product_category'
    #plt.figure(figsize=(12, 12))
    #sns.boxplot(x='category', y='actual_price', data=data)
    #plt.title('Box Plot of Price by Product Category')
    #plt.xlabel('Product Category')
    #plt.ylabel('Price')
    #plt.xticks(rotation=90)
    #plt.show()

def Matriz_de_correlacion():
    #correlations = data.corr(method='pearson')
    plt.figure(figsize=(12,10))
    plt.title('Matriz de correlacion')
    # Seleccionar columnas numéricas para la matriz de correlación
    numeric_data = data.select_dtypes(include=['float64', 'int64', 'string'])
    correlation_matrix = numeric_data.corr()
    sns.heatmap(correlation_matrix, vmax=1, square=True, annot=True, cmap='viridis')
    plt.show()


def Matriz_de_dispersion():
    # Crear la matriz de dispersión
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    sns.pairplot(numeric_data)
    plt.suptitle('Scatter Plot Matrix', y=1.02)
    plt.show()



#print_all_data() 
#print_first_rows(10)
#print_dimensions()
#print_data_types()
#count_data_by_class()
#summary()
#correlation()
#skew()

#densidad_matriz()
#Matriz_del_diagrama_de_caja()
#Matriz_de_correlacion()
Matriz_de_dispersion()

densidad_matriz()
#Matriz_del_diagrama_de_caja()
#Matriz_de_correlacion()
#Matriz_de_dispersion()
