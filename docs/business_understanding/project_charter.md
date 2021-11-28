# Project Charter

## Business background

* Cliente: Empresas panameñas de alimentos
* Dominio: Consumo masivo
* Problema del negocio: Identificar la percepcion de los clientes sobre las marcas asociadas a la compañia en tweeter  

## Scope
* Solucion de datascience
* Modelo no supervisado para preparar un set de datos etiquetado que se alamacenará en una base de datos 

* Que se va a hacer
	* Desplegar API para que el cliente cargue tweets y sean clasificados y almacenados en una base de datos para después ser visualizados en un dashboard

* Como se va a consumir por el cliente
	* Cargando datos a la API
	* Visulizando el dashboard

## Personnel
* Who are on this project:
	* Ingenieros de datos
		* Julio Bolaños (julioandres.bp@gmail.com) 
		* Jonatan Parra (japarrat@unal.edu.co)
	* Cientificos de datos
		* Simon Jaramillo (sijaramillogo94@gmail.com)
		* Cristian Mendez (cristianr.mendez@gmail.com)
	* Arquitecto de solución
		* Melissa de la Pava  	  
	* Client:
		* Simon Jaramillo
		* Juan Lara
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn)
	* Mejorar la escucha digital de la empresa referente a la marca
* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
	* Incremento periódico de tweets clasificados para la marca 
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%) 
	* Clasificar alrededor de 100 tweets en categorias periódicamente referentes a la marca 	 
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
	* 0 % 	 
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
	* Seguimiento de cuántos tweets se clasifican en un periodo de tiempo.	 

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.
* https://docs.google.com/spreadsheets/d/1hAFUNcaKeDpTUoin8-wbDFWf14Aw9dqJai-nJnnUVd8/edit?usp=sharing


## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
  * Datos en texto plano con feedback de clientes en redes sociales
  
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * Una muestra de los datos suficiente para la generacion del modelo

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * Proveedor de servicios en la nueve -> **Heroku**
  * Framework API REST -> **Flask**
  * Lenguaje de Programacion -> **pyhton**
  * Investigacion y generacion de modelos -> **Google colab y jupyter notebooks**
  * Provedor de base de datos -> **Mongo DB Atlas**
  * Dsahboard -> **PowerBI, PlotlyJs** 
  
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * El usuario va a disponer de una API para realizar carga de documentos con el contenido que desea analizar
  * El usuario va a poder visualizar el resultado del analisis en un dasboard conectado a la base de datos
  
  ![](https://github.com/jonatan-parra/mlds6/blob/master/docs/business_understanding/Diagrama%20Mejora%20escucha%20digital.jpeg){width='100px'}

## Communication
* How will we keep in touch? Weekly meetings?
	* Usar el tablero kanban de github y hacer reuniones semanales para revision y planeacion de tareas 
* Who are the contact persons on both sides?
	 
