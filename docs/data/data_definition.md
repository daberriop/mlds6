
# Definicion de datos y caracteristicas
## fuentes de datos

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| pascual.csv | Dataset que contiene la extracción de la esucha digital referente a la marca Pascual [pascual.csv](https://drive.google.com/file/d/1fLFVfTDaV7-2QWo3qYnpPae5ff0IKxFC/view?usp=sharing) | |[downloadFromGDrive.py](https://github.com/jonatan-parra/mlds6/blob/master/scripts/data_acquisition/downloadFromGDrive.py) |


* pascual.csv. La información inicial es proporcionada por el cliente. Archivos planos en formato csv compartidos via mail.

![rawcolums](https://drive.google.com/file/d/1xJc0oI0tt3fbp2lqBgJGTdcKVEMDqKVp/view?usp=sharing)



## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: |
| Tweets pascual | [pascual.csv](link/to/dataset1/report),  | [EDA.py](https://github.com/jonatan-parra/mlds6/blob/master/scripts/eda/EDA.py) | [EDA Report](https://github.com/jonatan-parra/mlds6/blob/e6da49921826414294d8f625562f8e298246ce9b/scripts/eda/EDA.pdf)|

![selectedcolums](https://drive.google.com/file/d/1LqdLwgdryjj2u95s5WH-4izrren91m87/view?usp=sharing)


* dataset pascual. conserva las columnas ['AUTHOR', 'CONTENT', 'PUBLISH_DATE', 'SENTIMENT']
* dataset tweets. Extrae la columna ['CONTENT'] del dataset pascual y lo almacena en una lista
* dataset norm_corpus. Se aplica limpieza a los datos: se eliminan: usuarios, url, emjois, stopwords. Se deja caratcteres [a-zA-Z] y se pasa todo a minúscula
* tokenized_corpus. Se tokeniza por palabra el dataset norm_corups
* tokenized_corpus1. Toma tokenized_corpus y se eliminan elementos vacíos

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: |
| preprocessing | [pascual.csv](https://drive.google.com/file/d/1fLFVfTDaV7-2QWo3qYnpPae5ff0IKxFC/view?usp=sharing) | [script de preprocesamiento](https://github.com/jonatan-parra/mlds6/blob/e6da49921826414294d8f625562f8e298246ce9b/scripts/preprocessing/main.py) | |

El script de prerpocesamiento aplica la limpieza de datos originales y el rpocesamiento de texto que consite en lo siguiente:
- remplazar caracteres latinos
- eliminar caracteres especiales
- eliminar urls
- eliminar emojis
- eliminar stopwrods
- eliminar username 
