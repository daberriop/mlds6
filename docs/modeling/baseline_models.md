# Baseline Model Report

## Analytic Approach
* What is target definition
	* Principalemente, se pretende generar etiquetas para poder agrupar los diferentes post relativos a la marca Pascual
* What are inputs (description)
	* El input serán vectores numéricos de tamaño (m,) que representan a cada uno de los post limpios y procesados (sin url, sin nombres de usario, sin emojis, sin stopwords, sin caracateres especiales) tokenizados por palabras
* What kind of model was built?
	1. Se construye un modelo de representación de texto que tenga en cuenta el contexto y la semántica con el fin de poder agrupar post simialres.
	2. Para la verificación de la similaridad de los vectores, se realzia una técnica de reducción de dimensionalidad para visualizar las representaciones en un espacio bidimensional. 
	3. Por último, se usa un modelo de agrupamiento para los vecotres reducidos.

## Model Description

* Models and Parameters

* WORD2VEC
	* feature_size = 100 
	* window_context = 5 
	* min_word_count = 1 
	* sample = 1e-3
	* epochs = 100 

* T-SNE 
	* En este caso, se selecciona un T-SNE (T-distributed Stochastic Neighbor Embedding) ya que usa transformación no lineal para conservar relaciones entre puntos de grandes diminesionalidaes
	* n_components=2,
    	* random_state=0,
    	* n_iter=1000,
    	* perplexity=2,
    	* verbose=1
* K-MENAS
	* n_clusters=6
	* init='k-means++'
	* max_iter=1000

## Results (Model Performance)
* Resultado para word2vec + TSNE
 
 ![word2vec and TSNE](https://user-images.githubusercontent.com/43830019/145692892-e977520a-00fa-4a25-b41a-ac636c5bb7be.png)

* Resultado selección de cluster para el modelo K-MEANS

![codo](https://user-images.githubusercontent.com/43830019/145693019-fbd8f434-d9d5-4003-8721-8824b5d1246c.png)


Se selecciona el hiper parámetro K= 6 con apoyo de la gráfica

* Resultado para K-MEANS

![KMENAS](https://user-images.githubusercontent.com/43830019/145692959-b00cd66e-6b3c-4471-9416-1a72ddc5548a.png)


## Model Understanding

* Variable Importance (significance)

* Insight Derived from the Model

## Conclusion and Discussions for Next Steps

* Conclusion on Feasibility Assessment of the Machine Learning Task
	* Con los resultados preeliminares se puede observar viabilidad en la clasificación de los post bajo algortimo no supervisado

* What other Features Can Be Generated from the Current Data
	* Es posible usar también otras formas de representación de palabras como  Bag of Words, TF-IF, etc para crear vectores que representen los textos

