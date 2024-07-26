import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
from pandas.plotting import scatter_matrix

filename = 'dataset/nearest-earth-objects(1910-2024).csv'
data = pd.read_csv(filename)

numeric_data = data.select_dtypes(include=['number'])

import tkinter as tk
from tkinter import messagebox

#Imprimir todos los datos
def print_all_data():
    # Ocultar la ventana principal
    root.withdraw()
    
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Impresión de todos los datos")
    ventana_secundaria.geometry("1160x400")
    ventana_secundaria.configure(bg='#ADD8E6')

    label = tk.Label(ventana_secundaria, text=data, font=("Arial", 12), bg='#e0f7fa')
    label.pack(pady=20)
    
    boton_regresar = tk.Button(ventana_secundaria, text="Regresar", font=("Arial", 14), bg='#CD5C5C', fg='#000000', command=lambda: regresar_a_principal(ventana_secundaria))
    boton_regresar.pack(pady=10)


#Imprimir las primeras n filas
def print_first_rows():
    # Ocultar la ventana principal
    root.withdraw()
    
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Impresión de las primeras n filas")
    ventana_secundaria.geometry("1160x400")
    ventana_secundaria.configure(bg='#ADD8E6')

    label = tk.Label(ventana_secundaria, text=data.head(10), font=("Arial", 12), bg='#e0f7fa')
    label.pack(pady=20)
    
    boton_regresar = tk.Button(ventana_secundaria, text="Regresar", font=("Arial", 14), bg='#CD5C5C', fg='#000000', command=lambda: regresar_a_principal(ventana_secundaria))
    boton_regresar.pack(pady=10)


#Imprimir la dimensión del df (Dataframe)
def print_dimensions():

    messagebox.showinfo("Impresión de la dimensión del Dataframe", "La dimensión es:", detail=data.shape) 


#Imprimir los tipos de datos
def print_data_types():
    # Ocultar la ventana principal
    root.withdraw()
    
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Impresión los tipos de datos")
    ventana_secundaria.geometry("300x300")
    ventana_secundaria.configure(bg='#ADD8E6')

    label = tk.Label(ventana_secundaria, text=data.dtypes, font=("Arial", 12), bg='#e0f7fa')
    label.pack(pady=20)
    
    boton_regresar = tk.Button(ventana_secundaria, text="Regresar", font=("Arial", 14), bg='#CD5C5C', fg='#000000', command=lambda: regresar_a_principal(ventana_secundaria))
    boton_regresar.pack(pady=10)


#Calcular la cantidad de datos por clase 
def count_data_by_class():
    class_count = data.groupby('is_hazardous').size()

    messagebox.showinfo("Impresión del cálculo de la cantidad de datos por clase", "La clase target : is_hazardous", detail=class_count)


#Resumen general de la dataset
def summary():
    # Ocultar la ventana principal
    root.withdraw()
    
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Resumen general de los datos")
    ventana_secundaria.geometry("1160x300")
    ventana_secundaria.configure(bg='#ADD8E6')

    resumen=data.describe()

    label = tk.Label(ventana_secundaria, text=resumen, font=("Arial", 12), bg='#e0f7fa')
    label.pack(pady=20)
    
    boton_regresar = tk.Button(ventana_secundaria, text="Regresar", font=("Arial", 14), bg='#CD5C5C', fg='#000000', command=lambda: regresar_a_principal(ventana_secundaria))
    boton_regresar.pack(pady=10)


#Correlación
def correlation():
    # Ocultar la ventana principal
    root.withdraw()
    
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Correlación de los datos")
    ventana_secundaria.geometry("1160x300")
    ventana_secundaria.configure(bg='#ADD8E6')

    correlations = numeric_data.corr(method='pearson')

    label = tk.Label(ventana_secundaria, text=correlations, font=("Arial", 12), bg='#e0f7fa')
    label.pack(pady=20)
    
    boton_regresar = tk.Button(ventana_secundaria, text="Regresar", font=("Arial", 14), bg='#CD5C5C', fg='#000000', command=lambda: regresar_a_principal(ventana_secundaria))
    boton_regresar.pack(pady=10)


#El Sesgo de los datos
def skew(): 
    # Ocultar la ventana principal
    root.withdraw()
    
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Impresión del Sesgo de los datos")
    ventana_secundaria.geometry("300x300")
    ventana_secundaria.configure(bg='#ADD8E6')

    a = numeric_data.skew()

    label = tk.Label(ventana_secundaria, text=a, font=("Arial", 12), bg='#e0f7fa')
    label.pack(pady=20)
    
    boton_regresar = tk.Button(ventana_secundaria, text="Regresar", font=("Arial", 14), bg='#CD5C5C', fg='#000000', command=lambda: regresar_a_principal(ventana_secundaria))
    boton_regresar.pack(pady=10)


#Matriz de Densidad
def densidad_matriz():
#Código básico para graficar
    fig = plt.figure(figsize=(15,8))
    plt.title('Matriz de Densidad')
    ax = fig.gca()
    #Código para graficar una matriz de dispersión
    numeric_data.plot(ax=ax, kind='density', subplots=True, layout=(3,3), sharex=False)
    plt.show()


#Matriz de diagrama de caja (box plot)
def Matriz_del_diagrama_de_caja():
    #Código básico para graficar
    fig = plt.figure(figsize=(15,8))
    plt.title('Matriz de Diagrama de Caja')
    ax = fig.gca()
    #Código para graficar una matriz de un diagrama de caja
    data.plot(ax=ax, kind='box', subplots=True, layout=(3,3), sharex=False)
    plt.show()


#Matriz de Correlación
def Matriz_de_correlacion():
    #correlations = data.corr(method='pearson')
    plt.figure(figsize=(10,10))
    plt.title('Matriz de Correlación')
    # Seleccionar columnas numéricas para la matriz de correlación
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numeric_data.corr()
    sns.heatmap(correlation_matrix, vmax=1, square=True, annot=True, cmap='viridis')
    plt.show()

#Matriz de Dispersión
def Matriz_de_dispersion():
    # Crear la matriz de dispersión
    plt.rcParams['figure.figsize'] = (6,6)
    scatter_matrix(data)
    plt.show()


#Función de cargar los datos de la dataset
def load_classification_problem():
    
    filename_clas = 'dataset/nearest-earth-objects(1910-2024).csv'
    df_clas = pd.read_csv(filename_clas)

    # Convertir columnas a enteros, usando 'coerce' para convertir valores no numéricos a NaN
    df_clas = df_clas.apply(pd.to_numeric, errors='coerce')

    # Convertir todos los valores numéricos a enteros (esto redondeará los valores flotantes a enteros)
    df_clas = df_clas.fillna(0)  # Rellenar NaN con 0 antes de convertir
    df_clas = df_clas.astype(int)  # Convertir a enteros

    # Eliminar filas con valores que no pueden ser convertidos a enteros (si hay algún valor restante como NaN, se eliminará)
    df_clas = df_clas.dropna()

    # Verificar si después de la limpieza hay datos disponibles
    if df_clas.shape[0] == 0:
        raise ValueError("No hay datos suficientes después de eliminar valores NaN.")

    # Separar las características y la variable objetivo
    array_clas = df_clas.values
    X_clas = array_clas[:, 0:8]
    Y_clas = array_clas[:, 8]

    # Verificar la distribución de clases
    class_counts = df_clas.groupby(df_clas.columns[8]).size()
    #print(f"Distribución de clases:\n{class_counts}")

    return X_clas, Y_clas


#Validación cruzada - Kfold Validation
def cross_validation_repeated():
    from sklearn.model_selection import RepeatedKFold
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression #Algoritmo lineal

    num_folds = 10 #Número de particiones
    seed = 1000 #Semilla aletoria
    num_repeats = 5 #Número de veces que se va a ir entrenando y validando
    kfold = RepeatedKFold(n_splits=num_folds, random_state=seed, n_repeats=num_repeats)
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    X_clas, Y_clas = load_classification_problem() 
    results = cross_val_score(model, X_clas, Y_clas, cv=kfold)
    #print(f"Porcentaje de acierto / Desviación estandar de Validación cruzada - Validación Kfold: {results.mean()*100.0:.3f}% ({results.std()*100.0:.3f}%)")
    result_1=(f"Porcentaje de acierto es: {results.mean()*100.0:.3f}%")
    result_2=(f"\nDesviación estandar de Validación cruzada - Validación Kfold es : {results.std()*100.0:.3f}%")
    ambos = result_1, result_2
    messagebox.showinfo("Validación cruzada - Kfold Validation", detail= ambos) 

     
    #results = cross_val_score(model, X_clas, Y_clas, cv=kfold)
    #print(f"Porcentaje de acierto / Desviación estandar de Validación cruzada - Validación Kfold: {results.mean()*100.0:.3f}% ({results.std()*100.0:.3f}%)")
    

# Hold - out Validation
def data_division():
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    test_size = 0.10 #Representa el 10% de todos los datos que serán usados opara validación
    seed = 1000
    #X_train: Variable que representa el conjunto de datos de entrenamiento.
    #X_test: Variable que representa conjunto de datos de prueba.
    #Y_train: Clase de entrenamiento
    #Y_test: Clase de prueba

    X_clas, Y_clas = load_classification_problem()
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size = test_size, random_state=seed)
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train) #Entrenando el modelo
    result = model.score(X_test, Y_test) #Predicción de mi modelo
    a=(f"Porcentaje de acierto de Validación Hold out es : {result*100.0:.3f}%")
    messagebox.showinfo("Hold - out Validation", detail= a) 


#Matrix de confusión para clasificación BINARIA
def matriz_confusion():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    from sklearn.linear_model import LogisticRegression

    test_size = 0.10
    seed = 1000

    # Cargar y preprocesar datos
    X_clas, Y_clas = load_classification_problem()

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size=test_size, random_state=seed)

    # Crear y ajustar el modelo
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)

    # Realizar predicciones
    prediccion = model.predict(X_test)

    # Calcular y mostrar la matriz de confusión
    matriz = confusion_matrix(Y_test, prediccion)
    a=(f"Matriz de Confusión:\n{matriz}")
    messagebox.showinfo("Matrix de confusión para clasificación BINARIA", detail= a)


#Porcentaje de exactitud - Accuracy
def accuracy():
    from sklearn.model_selection import KFold
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression

    X_clas, Y_clas = load_classification_problem()

    num_folds = 10
    seed = 1000
    
    kfold= KFold(n_splits=num_folds, shuffle=True, random_state=seed)
    model=LogisticRegression(solver='lbfgs', max_iter=1000)
    scoring= 'accuracy'
    results= cross_val_score(model, X_clas, Y_clas, cv=kfold, scoring=scoring)
    a=(f"Accurancy : {results.mean()*100.0:.3f}%")
    b=(f"\nDesviacion estandar: {results.std()*100.0:.3f}%")
    ambos= a, b
    messagebox.showinfo("Porcentaje de exactitud - Accuracy", detail= ambos)


#Puntaje de Acierto Cohen-Kappa
def cohen():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import cohen_kappa_score
    from sklearn.linear_model import LogisticRegression

    test_size= 0.10
    seed = 1000
    X_clas, Y_clas = load_classification_problem()
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size=test_size, random_state=seed)
    model= LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)
    prediccion= model.predict(X_test)
    puntaje_cohen= cohen_kappa_score(Y_test, prediccion)
    a=(f"Puntaje de Prediccion Cohen-Kappa es : {puntaje_cohen*100.0:.3f}%")
    messagebox.showinfo("Puntaje de Acierto Cohen-Kappa", detail= a)


#Reporte de clasificación
def reporte():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    from sklearn.linear_model import LogisticRegression

    # Ocultar la ventana principal
    root.withdraw()
    
    # Crear la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Reporte de clasificación")
    ventana_secundaria.geometry("400x300")
    ventana_secundaria.configure(bg='#ADD8E6')

    test_size= 0.10
    seed = 1000
    X_clas, Y_clas = load_classification_problem()
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size=test_size, random_state=seed)
    model= LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)
    prediccion= model.predict(X_test)

    report = classification_report(Y_test, prediccion)

    label = tk.Label(ventana_secundaria, text=report, font=("Arial", 12), bg='#e0f7fa')
    label.pack(pady=20)
    
    boton_regresar = tk.Button(ventana_secundaria, text="Regresar", font=("Arial", 14), bg='#CD5C5C', fg='#000000', command=lambda: regresar_a_principal(ventana_secundaria))
    boton_regresar.pack(pady=10)


#Función para cargar datos del dataset
def carga_datos():
    import pandas as pd
    filename = 'dataset/nearest-earth-objects(1910-2024).csv'
    data = pd.read_csv(filename)
    data = data.drop(columns=['name', 'orbiting_body'])
    data = data.dropna(axis=0)
    array= data.values
    X_reg = array[:,0:6]
    Y_reg = array[:,6]
    
    return X_reg, Y_reg


#Error medio absoluto
def error_medio_absoluto(): 
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error
    from sklearn.linear_model import LinearRegression


    test_size = 0.33
    seed = 7
    X_reg, Y_reg = carga_datos()
    X_train, X_test, Y_train, Y_test = train_test_split(X_reg, Y_reg, test_size=test_size, random_state=seed)
    model= LinearRegression()
    model.fit(X_train, Y_train)
    predict = model.predict(X_test)
    MAE = mean_absolute_error(Y_test, predict)
    a=(f"Error medio abosluto es : {MAE}")
    messagebox.showinfo("Error medio absoluto", detail= a)


#Error Cuadrático Medio
def mean_square_error():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.linear_model import LinearRegression

    test_size = 0.10
    seed = 1000
    X_reg, Y_reg = carga_datos()
    X_train, X_test, Y_train, Y_test = train_test_split(X_reg, Y_reg, test_size=test_size, random_state=seed)
    model= LinearRegression()
    model.fit(X_train, Y_train)
    predict = model.predict(X_test)
    
    MSE = mean_squared_error(Y_test, predict)
    a=(f"Error cuadrático medio es : {MSE}")
    messagebox.showinfo("Error Cuadrático Medio", detail= a)


#Coeficiente de determinación
def r2():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score
    from sklearn.linear_model import LinearRegression


    test_size = 0.10
    seed = 1000
    X_reg, Y_reg = carga_datos()
    X_train, X_test, Y_train, Y_test = train_test_split(X_reg, Y_reg, test_size=test_size, random_state=seed)
    model= LinearRegression()
    model.fit(X_train, Y_train)
    predict = model.predict(X_test)
    R2 = r2_score(Y_test, predict)
    a=(f"Coeficiente de determinación (R2) es : {R2}")
    messagebox.showinfo("Coeficiente de determinación", detail= a)


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def regresar_a_principal(ventana_secundaria):
    ventana_secundaria.destroy()
    root.deiconify()

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("390x600")
root.configure(bg='#f0f0f0')

frame_principal = tk.Frame(root)
frame_principal.pack(fill="both", expand=True)

canvas = tk.Canvas(frame_principal, bg='#3CB371')
canvas.pack(side="right", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame_interno = tk.Frame(canvas, bg='#3CB371')

canvas.create_window((0,0), window=frame_interno, anchor="nw")


boton_abrir = tk.Button(frame_interno, text="Impresión de todos los datos", font=("Calibri", 14), bg='#90EE90', fg='#000000', command=print_all_data)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Impresión de las primeras n filas", font=("Calibri", 14), bg='#00FA9A', fg='#000000', command=print_first_rows)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Impresión de la dimensión del Dataframe", font=("Calibri", 14), bg='#7FFFD4', fg='#000000', command=print_dimensions)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Impresión de los tipos de datos", font=("Calibri", 14), bg='#00FA9A', fg='#000000', command=print_data_types)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Cálculo de la cantidad de datos por clase", font=("Calibri", 14), bg='#90EE90', fg='#000000', command=count_data_by_class)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Resumen general de los datos", font=("Calibri", 14), bg='#7FFFD4', fg='#000000', command=summary)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Correlación de los datos", font=("Calibri", 14), bg='#90EE90', fg='#000000', command=correlation)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Sesgo de los datos", font=("Calibri", 14), bg='#00FA9A', fg='#000000', command=skew)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Matriz de Densidad", font=("Calibri", 14), bg='#7FFFD4', fg='#000000', command=densidad_matriz)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Matriz de Diagrama de Caja", font=("Calibri", 14), bg='#90EE90', fg='#000000', command=Matriz_del_diagrama_de_caja)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Matriz de Correlación", font=("Calibri", 14), bg='#00FA9A', fg='#000000', command=Matriz_de_correlacion)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Matriz de Dispersión", font=("Calibri", 14), bg='#7FFFD4', fg='#000000', command=Matriz_de_dispersion)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Validación cruzada - Validación Kfold", font=("Calibri", 14), bg='#90EE90', fg='#000000', command=cross_validation_repeated)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Hold - out Validation", font=("Calibri", 14), bg='#7FFFD4', fg='#000000', command=data_division)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Matriz Confusion", font=("Calibri", 14), bg='#00FA9A', fg='#000000', command=matriz_confusion)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Porcentaje de exactitud - Accuracy", font=("Calibri", 14), bg='#7FFFD4', fg='#000000', command=accuracy)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Puntaje de Acierto Cohen-Kappa", font=("Calibri", 14), bg='#90EE90', fg='#000000', command=cohen)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Reporte de clasificación", font=("Calibri", 14), bg='#00FA9A', fg='#000000', command=reporte)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Error Medio Absoluto", font=("Calibri", 14), bg='#7FFFD4', fg='#000000', command=error_medio_absoluto)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Error Cuadrático Medio", font=("Calibri", 14), bg='#00FA9A', fg='#000000', command=mean_square_error)
boton_abrir.pack(pady=5)

boton_abrir = tk.Button(frame_interno, text="Coeficiente de Determinación (R2)", font=("Calibri", 14), bg='#90EE90', fg='#000000', command=r2)
boton_abrir.pack(pady=5)


# Iniciar el bucle principal de la ventana
root.mainloop()

