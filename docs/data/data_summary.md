# Data Report

This document contains the results from the exploratory data analysis.

## General summary of the data & Data quality summary
### Data Set pascual
Exploración general de los campos del dataset pascual

RangeIndex: 276 entries, 0 to 275
Data columns (total 4 columns):
|#|Column|Non-NullCount|Dtype|  
|-|------|-------------|-----|  
|0|AUTHOR|259 non-null|object| 
|1|CONTENT|259 non-null|object| 
|2|PUBLISH_DATE|259 non-null|object| 
|3|SENTIMENT|259 non-null|object| 

types: object(4)
### Ejemplos post limpios
Post sin procesar:

* ['De estos señores se sabrá toda la verdad. Ahora que dirán Nito, Sucre, Bacal y la Pascual. https://t.co/B7NjhNuz1J']
* ['Al próximo perro que tenga le voy a poner PASCUAL, cómo a la mascota de  .@vanedelatorre']
* ['Pascual Gaviria además d marihuanero es un patán con las mujeres, ssi lo demostró con la senadora.']
* ['@prt1957 Gracias Don Pascual, usted es parte de esta grata historia 💪😎🇦🇹🔥'"]
* ['@UltraRoja07 saludos el Profe Gary - Chato Pascual, estamos triste por el momento negativo en su campaña actual, pero sabemos que vendran dias mejores, para mantener en alto el buen nombre del SANFRA y de sus seguidores a nivel nacional.']
 
 Post procesados:
* ['seores', 'sabr', 'toda', 'verdad', 'ahora', 'dirn', 'nito', 'sucre', 'bacal', 'pascual']
* ['prximo', 'perro', 'voy', 'poner', 'pascual', 'cmo', 'mascota']
* ['pascual', 'gaviria', 'adems', 'marihuanero', 'patn', 'mujeres', 'ssi', 'demostr', 'senadora']
* ['gracias', 'don', 'pascual', 'usted', 'parte', 'grata', 'historia']
* ['saludos', 'profe', 'gary', 'chato', 'pascual', 'triste', 'momento', 'negativo', 'campaa', 'actual', 'sabemos', 'vendran', 'dias', 'mejores', 'mantener', 'alto', 'buen', 'nombre', 'sanfra', 'seguidores', 'nivel', 'nacional']

### Exploración de 'CONTENT'
![wordcloud pascual](https://user-images.githubusercontent.com/43830019/144765882-d2d81d8e-d1af-4df5-b817-6445cd3d05ab.png)

### Palabras más frecuentes
|#|Word|Count|
|-|----|-----|
|0|pascual|152| 
|1|galletas|39| 
|2|hora|30| 
|3|galleta|27| 
|4|gracias|24| 
|5|ms|24|
|6|detalle|24| 
|7|panam|20| 
|8|mara|19| 
|9|si|19| 


## Target variable
El objetivo principal es generar etiquetas para clasificar los post en clusters similares
## Individual variables
La campo 'CONTENT' será la uníca variable que se usará para entrenar el modelo de agrupamiento

## Relationship between explanatory variables and target variable
Dependiendo del contenido de cada tweet, se busca agruparlos por semejanza y generar un etiquetado para el posterior uso del cliente 

