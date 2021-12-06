
# Data and Feature Definitions
## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| pascual.csv | Dataset que contiene la extracción de la esucha digital referente a la marca Pascual | |[downloadFromGDrive.py](https://github.com/jonatan-parra/mlds6/blob/master/scripts/data_acquisition/downloadFromGDrive.py) |


* pascual.csv. La información inicial es proporcionada por el cliente. Archivos planos en formato csv compartidos via mail.

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: |
| Tweets pascual | [pascual.csv](link/to/dataset1/report),  | [EDA.py](https://github.com/jonatan-parra/mlds6/blob/master/scripts/eda/EDA.py) | [EDA Report](https://github.com/jonatan-parra/mlds6/blob/master/scripts/eda/EDA_report.html)|
* dataset pascual. conserva las columnas ['AUTHOR', 'CONTENT', 'PUBLISH_DATE', 'SENTIMENT']
* dataset tweets. Extrae la columna ['CONTENT'] del dataset pascual y lo almacena en una lista
* dataset norm_corpus. Se aplica limpieza a los datos: se eliminan: usuarios, url, emjois, stopwords. Se deja caratcteres [a-zA-Z] y se pasa todo a minúscula
* tokenized_corpus. Se tokeniza por palabra el dataset norm_corups
* tokenized_corpus1. Toma tokenized_corpus y se eliminan elementos vacíos

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: |
| preprocessing | [pascual.csv](link/to/dataset1/report) | [EDA.py](https://github.com/jonatan-parra/mlds6/blob/master/scripts/eda/EDA.py) | |

* preprocessing. Elimina los usernames, las URLs y emojis de los tweets
