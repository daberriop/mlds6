# Data Report

This document contains the results from the exploratory data analysis.

## General summary of the data & Data quality summary
### Data Set pascual
RangeIndex: 276 entries, 0 to 275
Data columns (total 4 columns):
|#|Column|Non-NullCount|Dtype|  
|-|------|-------------|-----|  
|0|AUTHOR|259 non-null|object| 
|1|CONTENT|259 non-null|object| 
|2|PUBLISH_DATE|259 non-null|object| 
|3|SENTIMENT|259 non-null|object| 

types: object(4)
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

