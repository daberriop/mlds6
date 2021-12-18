# Reporte final del modelo
Depues de realizar validaciones del modelo se definio realizar dos modelos. un Modelo de KMeans que nos ermite obtener los clusters de los comentarios y un segundo modelo suando T-SNE para generar una representacion de los datos

Como resultado de proceso de entrenamiento se generaun archivo pickle con el modelo entrenado listo para usarse

- [modelo.pkl](https://github.com/jonatan-parra/mlds6/blob/621bdbac0fd579941bc744e0f0bfa7e839733fb8/digitallistening/models/model.pkl)

- [Modulo para consumir el modelo](https://github.com/jonatan-parra/mlds6/blob/621bdbac0fd579941bc744e0f0bfa7e839733fb8/digitallistening/models/model.py)
 
## Datos
La fuente de datos es un archivo de texto plano ubicado en: https://drive.google.com/file/d/1fLFVfTDaV7-2QWo3qYnpPae5ff0IKxFC/view?usp=sharing que se obtiene mediante el siguiente [script](https://github.com/jonatan-parra/mlds6/blob/1c8653769ecb0855fe3e1f91dbc761a7528abf85/scripts/data_acquisition/downloadFromGDrive.py)


## Caracteristicas

en ambos casos la extraccion de caracteristicas se realiza con un modelo Word2Vec usando promedios 

### Modelo para extraccion de caracteristicas

WORD2VEC

    feature_size = 100
    window_context = 5
    min_word_count = 1
    sample = 1e-3
    epochs = 100
 
ver [Modulo de extraccion de caracteristicas](https://github.com/jonatan-parra/mlds6/blob/1c8653769ecb0855fe3e1f91dbc761a7528abf85/digitallistening/training/feature_extraction.py)

## Algoritmos utilizados

### Selección de hiperparametros para el modelo K-MEANS

![codo](https://user-images.githubusercontent.com/43830019/145693019-fbd8f434-d9d5-4003-8721-8824b5d1246c.png)


Se selecciona el hiper parámetro K= 6 con apoyo de la gráfica


### Modelo para generacion de clusters

K-MEANS

    n_clusters=6
    init='k-means++'
    max_iter=1000

var [Modulo de entrenamiento](https://github.com/jonatan-parra/mlds6/blob/1c8653769ecb0855fe3e1f91dbc761a7528abf85/digitallistening/training/model_training.py)

### Modelo para transformacion y visualizacion de clusters

en este caso a diferencia del modelo base se utilizan 3 componentes para generar una mejor visualizacion

T-SNE

    En este caso, se selecciona un T-SNE (T-distributed Stochastic Neighbor Embedding) ya que usa transformación no lineal para conservar relaciones entre puntos de grandes diminesionalidaes
    n_components=3,
        random_state=0,
        n_iter=1000,
        perplexity=2,
        verbose=1
ver [Dashboard](https://github.com/jonatan-parra/mlds6/blob/1c8653769ecb0855fe3e1f91dbc761a7528abf85/scripts/dashboard/app.py)

## Resultados

### Visualizacion del T-SNE en dasboard con clusters fenerados usando KMeans

![KMENAS](https://github.com/jonatan-parra/mlds6/blob/master/docs/modeling/dashboard.png)
