import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
from pandas.plotting import scatter_matrix

filename= 'dataset/nearest-earth-objects(1910-2024).csv'
data = pd.read_csv(filename)

def density_matrix():
#Código básico para graficar
    fig = plt.figure(figsize=(6,6))
    ax = fig.gca()
    #Código para graficar una matriz de dispersión
    data.plot(ax=ax, kind='density', subplots=True, layout=(3,3), sharex=False)
    plt.show()


def box_plot_matrix():
    #Código básico para graficar
    fig = plt.figure(figsize=(6,6))
    ax = fig.gca()
    #Código para graficar una matriz de un diagrama de caja
    data.plot(ax=ax, kind='box', subplots=True, layout=(3,3), sharex=False)
    plt.show()


def correlation_matrix():
    correlations = data.corr(method='pearson')
    plt.figure(figsize=(6,6))
    plt.title('Matriz de correlacion')
    sns.heatmap(correlations, vmax=1, square= True, annot= True, cmap='viridis')
    plt.show()


def dispersion_matrix():
    plt.rcParams['figure.figsize'] = (6,6)
    scatter_matrix(data)
    plt.show()

density_matrix()
#box_plot_matrix()
#correlation_matrix()
#dispersion_matrix()