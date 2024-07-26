import pandas as pd

# Cargar el archivo CSV
file_path = 'dataset/nearest-earth-objects(1910-2024).csv'
data = pd.read_csv(file_path)

# Primeras filas
print("Primeras filas:")
print(data.head())

# Dimensiones
print("\nDimensiones:")
print(data.shape)

# Tipos de datos
print("\nTipos de datos:")
print(data.dtypes)

# Resumen de los datos
print("\nResumen de los datos:")
print(data.describe())

# Cantidad de datos por clase (si hay una columna de clase)
print("\nCantidad de datos por clase:")
if 'miss_distance' in data.columns:
    print(data['miss_distance'].value_counts())

numeric_data = data.select_dtypes(include=['number'])

specific_column = 'absolute_magnitude'  # Reemplaza con el nombre real de la columna específica
if specific_column in numeric_data.columns:
    skewness = numeric_data[specific_column].skew()
    print(f"\nSesgo de '{specific_column}': {skewness}")
else:
    print(f"\nLa columna '{specific_column}' no se encuentra en los datos numéricos.")

# Correlación
print("\nCorrelación:")
print(numeric_data.corr())

class_column = 'relative_velocity'
# Distribución entre clases (si hay una columna de clase)
print("\nDistribución entre clases:")
if class_column in data.columns:
    distribution = data.groupby(class_column).size()
    print(distribution)
