def carga_datos():
    import pandas as pd
    filename = 'dataset/nearest-earth-objects(1910-2024).csv'
    data = pd.read_csv(filename)
    data = data.drop(columns=['name', 'orbiting_body'])
    data = data.dropna(axis=0)
    array= data.values
    X_reg = array[:,0:6]
    Y_reg = array[:,3]
    
    return X_reg, Y_reg


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
    print(f"Error medio abosluto: {MAE}")


def mean_square_error():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.linear_model import LinearRegression


    test_size = 0.33
    seed = 7
    X_reg, Y_reg = carga_datos()
    X_train, X_test, Y_train, Y_test = train_test_split(X_reg, Y_reg, test_size=test_size, random_state=seed)
    model= LinearRegression()
    model.fit(X_train, Y_train)
    predict = model.predict(X_test)
    
    MSE = mean_squared_error(Y_test, predict)
    print(f"Error cuadratico medio: {MSE}")


def r2():
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score
    from sklearn.linear_model import LinearRegression


    test_size = 0.33
    seed = 7
    X_reg, Y_reg = carga_datos()
    X_train, X_test, Y_train, Y_test = train_test_split(X_reg, Y_reg, test_size=test_size, random_state=seed)
    model= LinearRegression()
    model.fit(X_train, Y_train)
    predict = model.predict(X_test)
    R2 = r2_score(Y_test, predict)
    print(f"Coeficiente de determinacion: {R2}")
    

error_medio_absoluto()
mean_square_error()
r2()