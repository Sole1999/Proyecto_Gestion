#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

#filename = 'dataset/amazon.csv'
#data = pd.read_csv(filename)

#Todos los valores numericos de mi dataset, sin el nombre de las columnas
#array = data.values
#Caracteristicas
#X = array[:,5:8] #Todas las filas, columnas 0 hasta la 8
#Y = array[:,8] #Todas las filas, columna 8 hasta el objetivo

# Kfold Validation

def cross_validation_repeated():
    from sklearn.model_selection import RepeatedKFold
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression #Algoritmo lineal

    num_folds = 10 #Número de particiones
    seed = 7 #Semilla aletoria
    num_repeats = 5 #Número de veces que se va a ir entrenando y validando
    kfold = RepeatedKFold(n_splits=num_folds, random_state=seed, n_repeats=num_repeats)
    model = LogisticRegression(solver='lbfgs', max_iter=1000) 
    results = cross_val_score(model, X, Y, cv=kfold)
    print(f"Porcentaje de acierto / Desviación estandar: {results.mean()*100.0:.3f}% ({results.std()*100.0:.3f}%)")

def data_divsion():
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    test_size = 0.33 #Representa el 33% de todos los datos que serán usados opara validación
    seed = 7
    #X_train: Variable que representa el conjunto de datos de entrenamiento.
    #X_test: Variable que representa conjunto de datos de prueba.
    #Y_train: Clase de entrenamiento
    #Y_test: Clase de prueba

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = test_size, random_state=seed)
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train) #Entrenando el modelo
    result = model.score(X_test, Y_test) #Predicción de mi modelo
    print(f"Porcentaje de acierto: {result*100.0:.3f}%")

def load_clasification_problem():
    import numpy as np 
    import pandas as pd 

    filename_clas = 'dataset/nearest-earth-objects(1910-2024).csv'
    df_clas = pd.read_csv(filename_clas)
    array_clas = df_clas.values
    X_clas = array_clas[:,0:8]
    Y_clas = array_clas[:,8]

    class_counts = df_clas.groupby('is_hazardous').size()
    #print(class_counts)

    return X_clas, Y_clas


#Porcentaje de acierto
def accuracy():
    from sklearn.model_selection import KFold
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression

    X_clas, Y_clas = load_clasification_problem()

    num_folds = 10 #Número de particiones
    seed= 7 #Semilla Aleatoria
    kfold = KFold(n_splits=num_folds, shuffle=True, random_state=seed)
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    scoring = 'accuracy'
    results = cross_val_score(model, X_clas, Y_clas, cv=kfold, scoring=scoring)

    print(f"Accuracy(Porcentaje de exactitud) / Desviación estándar: {results.mean()*100.0:.3f}% ({results.std()*100.0:.3f}%)")


def kappa():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import cohen_kappa_score
    from sklearn.linear_model import LogisticRegression

    test_size = 0.33
    seed = 7
    X_clas, Y_clas = load_clasification_problem()
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size=test_size, random_state=seed)
    model=LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)
    predicted= model.predict(X_test)
    cohen_score= cohen_kappa_score(Y_test, predicted)
    print(f"Puntaje de Cohen: {cohen_score*100.0:.3f}%")


def confusion_matrix():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    from sklearn.linear_model import LogisticRegression


    test_size = 0.33
    seed = 7
    X_clas, Y_clas = load_clasification_problem()
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size=test_size, random_state=seed)
    model=LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)
    predicted= model.predict(X_test)

    #Código para generar mi matriz de confusión
    matrix = confusion_matrix(Y_test, predicted)
    print(matrix)


def classification_report():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    from sklearn.linear_model import LogisticRegression
    
    test_size = 0.33
    seed = 7
    X_clas, Y_clas = load_clasification_problem()
    X_train, X_test, Y_train, Y_test = train_test_split(X_clas, Y_clas, test_size=test_size, random_state=seed)
    model=LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X_train, Y_train)
    predicted= model.predict(X_test)

    #Código para generar el reporte de clasificación
    report= classification_report(Y_test, predicted)
    print(report)


cross_validation_repeated()
#data_divsion()
#load_clasification_problem()
#accuracy()
#kappa()
#confusion_matrix()
#classification_report()