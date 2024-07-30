# Proyecto_Gestion
Materia Gestión de Proyectos

![Logo](https://github.com/user-attachments/assets/6226ebc7-81fd-4824-89f6-4f99410cdaec) ![Logo](https://github.com/user-attachments/assets/e1770a30-44ca-4e0c-8e93-717bb01edeab)

## Autores
- Patsy Rios [@Sole1999](https://github.com/Sole1999)
- Daniel Bonilla [@DannyB2023](https://github.com/DannyB2023)

## Descripción
Realizar un análisis del dataset mediante la utilización de las librerías de Python.

## Introducción
La gestión de proyectos es una disciplina esencial en el mundo de los negocios y la tecnología, que se centra en la planificación, ejecución y supervisión de proyectos para alcanzar objetivos específicos dentro de un plazo definido y con un presupuesto establecido. Su objetivo principal es asegurar que los proyectos se completen de manera eficiente y efectiva, satisfaciendo las expectativas de los interesados.

Un proyecto es un esfuerzo temporal que busca crear un producto, servicio o resultado único. La gestión de proyectos implica la aplicación de conocimientos, habilidades, herramientas y técnicas para cumplir con los requisitos del proyecto y garantizar su éxito. Los gestores de proyectos deben equilibrar tres variables clave: el alcance, el tiempo y el costo, y manejar las expectativas y los riesgos asociados.

## Herramientas
- Visual Studio Code
- Python versión 3.12.4
- Librerías de Python
- Una dataset
  
### Librerías requeridas

Instalar todas las librerias necesarias, con el archivo librerias.txt que se encuentra en el repositorio mediante el siguiente código:

        pip install librerias.txt

### Dataset

Acerca del Dataset

Este archivo contiene varios parámetros/características en base a los cuales un asteroide en particular que ya está clasificado como objeto terrestre más cercano puede o no ser peligroso.

[Dataset: NASA | Nearest Earth Objects (1910-2024)](https://www.kaggle.com/datasets/ivansher/nasa-nearest-earth-objects-1910-2024)

## Desarrollo
### Menú gráfico de todas las funciones
_Funciones que se trabajará con el Dataset para el análisis._

![image](https://github.com/user-attachments/assets/1da78c15-2935-4be4-aa31-91f874218935) ![image](https://github.com/user-attachments/assets/a81664bf-62d0-4544-a415-30b81281c035)


### Impresión de todos los datos de la Dataset
_Se imprime todos los datos del Dataset desde las primeras hasta las últimas filas._

![image](https://github.com/user-attachments/assets/8f028b7d-b61a-47f3-9c54-33bbb26d6794)

### Impresión de las primeras n filas
_En este caso se realiza la impresión de los primeras 10 filas del Dataset._

![image](https://github.com/user-attachments/assets/03e361cc-94f0-4b49-9902-716b6e552912)

### Impresión de la dimensión del Dataframe
_La dimensión de un DataFrame en el contexto de análisis de datos y programación con bibliotecas como pandas en Python se refiere a la estructura del DataFrame en términos del número de filas y columnas que contiene._

![image](https://github.com/user-attachments/assets/0bc786d3-86ba-4cf0-ae34-44f9f7564f6c)

### Impresión de los tipos de datos
_Se refiere a mostrar la información sobre el tipo de datos (data type) de cada columna en el DataFrame. Esta información es crucial para entender qué tipo de datos estamos manejando en cada columna, ya que los diferentes tipos de datos (numéricos, categóricos, de texto, etc.) pueden requerir diferentes tipos de procesamiento y análisis._

![image](https://github.com/user-attachments/assets/9758ad3b-da44-43f4-b8b3-acb75af1d2e8)

### Cálculo de la cantidad de datos por clase
_Este cálculo se realiza el conteo de cuántas veces aparece cada categoría o clase dentro de una columna específica, que generalmente es la columna objetivo en problemas de clasificación. Esta operación es crucial en análisis de datos y en tareas de machine learning, ya que permite entender la distribución de las clases y detectar posibles problemas de desequilibrio (cuando algunas clases están sobrerrepresentadas y otras subrepresentadas)._

![image](https://github.com/user-attachments/assets/bcb2de49-e48a-4b0d-9bd6-90d7f1076b5f)

### Resumen general de los datos
_El resumen general de los datos de un dataset es una visión global que proporciona información estadística y estructural sobre el conjunto de datos. Es crucial para el análisis exploratorio de datos (EDA, por sus siglas en inglés) y ayuda a los analistas a entender mejor la naturaleza y las características de los datos con los que están trabajando._

![image](https://github.com/user-attachments/assets/4693c39a-6e8e-4de0-9224-ea9b099fcc08)

### Correlación de los datos
_La correlación de los datos de un dataset es la medida de la relación lineal entre dos variables. En otras palabras, la correlación indica cómo una variable se mueve en relación con otra variable. Y es crucial en el análisis de datos y en la construcción de modelos predictivos, ya que puede ayudar a identificar relaciones significativas entre variables._

![image](https://github.com/user-attachments/assets/16dbdf6d-b60a-4b6a-8f9c-a3daa2d13098)

### Sesgo de los datos
_El sesgo de los datos en un dataset se refiere a la presencia de prejuicios o desequilibrios sistemáticos en los datos que pueden distorsionar el análisis y los resultados de los modelos de machine learning. El sesgo puede surgir de diversas fuentes y tener múltiples efectos adversos, incluidos resultados injustos, discriminación y decisiones incorrectas._

![image](https://github.com/user-attachments/assets/31114de0-d0ab-4956-b8e0-7a6424ad9feb)

### Matriz de Densidad
_La matriz de densidad es una representación gráfica utilizada para visualizar la distribución de datos y la relación entre múltiples variables en un conjunto de datos. Este tipo de gráfico es particularmente útil para identificar patrones, correlaciones y densidades de puntos en conjuntos de datos multivariados._

![image](https://github.com/user-attachments/assets/e60efddf-dea2-49c0-a3b8-9a06b0cb100e)

### Matriz de Diagrama de Caja
_La matriz de diagrama de caja (o matriz de boxplots) es una visualización gráfica que muestra la distribución de varias variables en un dataset utilizando diagramas de caja. Cada diagrama de caja proporciona un resumen visual de la distribución de una variable, mostrando la mediana, los cuartiles y los posibles valores atípicos._

![image](https://github.com/user-attachments/assets/6a563c01-3c5c-4cb4-a170-2ab84a717648)

### Matriz de Correlación
_Una matriz de correlación es una tabla que muestra los coeficientes de correlación entre las variables de un dataset. Cada celda en la matriz muestra la correlación entre dos variables, proporcionando una medida de cómo una variable cambia con respecto a otra. Esta herramienta es fundamental en el análisis de datos exploratorio, ya que ayuda a identificar relaciones lineales entre variables._

![image](https://github.com/user-attachments/assets/a1d13230-a36a-4b87-bd43-6435e9fdac06)

### Matriz de Dispersión
_Una matriz de dispersión, también conocida como scatterplot matrix o pair plot, es una visualización gráfica que muestra gráficos de dispersión (scatter plots) para cada par de variables en un dataset. Este tipo de visualización es útil para explorar relaciones entre múltiples variables, identificar patrones, detectar valores atípicos y comprender la estructura del dataset._

![image](https://github.com/user-attachments/assets/30d7967a-70c3-4d52-9d16-68b27ab30205)

### Validación cruzada - Validación Kfold
_La validación cruzada es una técnica utilizada en el aprendizaje automático para evaluar la capacidad de generalización de un modelo y para evitar el sobreajuste (overfitting). La validación K-fold es uno de los métodos más comunes de validación cruzada, que consiste en dividir el dataset en 𝐾 subconjuntos o "folds" de aproximadamente el mismo tamaño para entrenar y evaluar el modelo._

![image](https://github.com/user-attachments/assets/50dfb9e1-6154-4599-b12e-5ff60f7b422b)

### Hold - out Validation
_La validación hold-out (o validación de separación) es una técnica simple de validación utilizada para evaluar el rendimiento de un modelo de machine learning. En este método, el dataset se divide en dos subconjuntos: uno para entrenamiento y otro para prueba. El modelo se entrena utilizando el subconjunto de entrenamiento y se evalúa utilizando el subconjunto de prueba._

![image](https://github.com/user-attachments/assets/53d622f0-b1dc-4d8b-b55f-f9129065efae)

### Matriz de Confusión
_Una matriz de confusión es una herramienta utilizada en clasificación para evaluar el rendimiento de un modelo. Proporciona una visualización de las predicciones del modelo en comparación con los valores reales. La matriz de confusión muestra las frecuencias de las predicciones correctas e incorrectas del modelo, y ayuda a identificar qué clases se confunden entre sí._

![image](https://github.com/user-attachments/assets/4823092c-9730-4de1-9cec-75c0c3eb1775)

### Porcentaje de exactitud - Accuracy
_El porcentaje de exactitud (o simplemente exactitud en inglés, accuracy) es una métrica utilizada para evaluar el rendimiento de un modelo de clasificación. Representa la proporción de predicciones correctas realizadas por el modelo sobre el total de predicciones realizadas._

![image](https://github.com/user-attachments/assets/f0d23938-51d1-4734-839b-4f93aa51321c)

### Puntaje de Acierto Cohen-Kappa
_El puntaje de acierto Cohen-Kappa (o simplemente Kappa de Cohen) es una métrica que evalúa la concordancia entre dos clasificadores o entre un clasificador y una verdad de referencia, teniendo en cuenta la posibilidad de que la concordancia se haya producido por casualidad. Es particularmente útil cuando se trabaja con datos categóricos y se quiere medir la consistencia en la clasificación._

![image](https://github.com/user-attachments/assets/7dfbf1c0-ae63-4767-a375-6cb938d8f639)

### Reporte de clasificación
_Un reporte de clasificación es una herramienta de evaluación que proporciona un resumen detallado de la calidad de un modelo de clasificación. Generalmente incluye varias métricas importantes que ayudan a entender cómo el modelo está funcionando en términos de precisión, recall, y otras métricas de rendimiento._

![image](https://github.com/user-attachments/assets/b373f351-e28d-4bd4-b0f1-8d76ed2a6952)

### Error Medio Absoluto
_El Error Medio Absoluto (MAE) es una métrica de evaluación utilizada en problemas de regresión para medir la precisión de las predicciones de un modelo. Calcula el promedio de las diferencias absolutas entre los valores predichos por el modelo y los valores reales. Es una métrica simple y fácil de interpretar que proporciona una medida de la magnitud de los errores en el modelo de forma directa._

![image](https://github.com/user-attachments/assets/2f5771b3-d92b-46a2-8a29-fb0bdae63ee1)

### Error Cuadrático Medio
_El Error Cuadrático Medio (MSE) es una métrica utilizada en problemas de regresión para medir la precisión de un modelo. Mide el promedio de los cuadrados de los errores, que son las diferencias entre los valores predichos por el modelo y los valores reales. Es útil para cuantificar la variabilidad en los errores y penaliza errores grandes de manera más severa que el Error Medio Absoluto (MAE)._

![image](https://github.com/user-attachments/assets/e714faf1-cfd2-4224-9125-a3c6b55f3c0f)

### Coeficiente de Determinación (R2)
_El Coeficiente de Determinación (R²), también conocido como R cuadrado, es una métrica utilizada para evaluar la calidad de ajuste de un modelo de regresión. Mide la proporción de la variabilidad en la variable dependiente que es explicada por el modelo en comparación con un modelo de referencia (como el promedio de la variable dependiente)._

![image](https://github.com/user-attachments/assets/26e1e1ee-42a2-4e3e-85d4-32bdaa25b9d0)

# FIN! 👋










