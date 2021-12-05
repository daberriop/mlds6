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

## Target variable
El objetivo principal es generar etiquetas para clasificar los post en clusters similares
## Individual variables
La campo 'CONTENT' será la uníca variable que se usará para entrenar el modelo de agrupamiento

## Relationship between explanatory variables and target variable
Dependiendo del contenido de cada tweet, se busca agruparlos por semejanza y generar un etiquetado para el posterior uso del cliente 

