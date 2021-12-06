# Data and Feature Definitions
## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| pascual.csv | Dataset que contiene la extracción de la esucha digital referente a la marca Pascual | [script1.py](link/to/python/script/file/in/Code) | [Dataset 1 Report](link/to/report1)|


* pascual.csv. La información inicial es proporcionada por el cliente. Archivos planos en formato csv compartidos via mail.

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: |
| Tweets pascual | [pascual.csv](link/to/dataset1/report),  | [EDA.py](https://github.com/jonatan-parra/mlds6/blob/master/scripts/eda/EDA.py) | [Processed Dataset 1 Report](link/to/report1)|
* dataset pascual. conserva las columnas ['AUTHOR', 'CONTENT', 'PUBLISH_DATE', 'SENTIMENT']
* dataset tweets. Extrae la columna ['CONTENT'] del dataset pascual y lo almacena en una lista
* dataset norm_corpus. Se aplica limpieza a los datos: se eliminan: usuarios, url, emjois, stopwords. Se deja caratcteres [a-zA-Z] y se pasa todo a minúscula
* tokenized_corpus. Se tokeniza por palabra el dataset norm_corups
* tokenized_corpus1. Toma tokenized_corpus y se eliminan elementos vacíos

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: |
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>
* Feature Set2 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set2 Report.>
