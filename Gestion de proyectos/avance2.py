def load_classification_problem():
    import pandas as pd

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

def matriz_confusion():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    from sklearn.linear_model import LogisticRegression

    test_size = 0.33
    seed = 7

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
    print(f"Matriz de Confusión:\n{matriz}")

#matriz_confusion()

def accuracy():
    from sklearn.model_selection import KFold
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression

    X_clas, Y_clas = load_classification_problem()

    num_folds = 10
    seed = 7
    
    kfold= KFold(n_splits=num_folds, shuffle=True, random_state=seed)
    model=LogisticRegression(solver='lbfgs', max_iter=1000)
    scoring= 'accuracy'
    results= cross_val_score(model, X_clas, Y_clas, cv=kfold, scoring=scoring)
    print(f"Accurancy : {results.mean()*100.0:.3f}%")
    print(f"Desviacion estandar: {results.std()*100.0:.3f}%")

#accuracy()

def cohen():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import cohen_kappa_score
    from sklearn.linear_model import LogisticRegression

    test_size= 0.33
    seed = 7
    X_clas, Y_clas = load_classification_problem()
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size=test_size, random_state=seed)
    model= LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)
    prediccion= model.predict(X_test)
    puntaje_cohen= cohen_kappa_score(Y_test, prediccion)
    print(f"Puntaje de Prediccion: {puntaje_cohen*100.0:.3f}%")

#cohen()
def reporte():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    from sklearn.linear_model import LogisticRegression

    
    test_size= 0.33
    seed = 7
    X_clas, Y_clas = load_classification_problem()
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size=test_size, random_state=seed)
    model= LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)
    prediccion= model.predict(X_test)

    report = classification_report(Y_test, prediccion)
    print(report)

reporte()