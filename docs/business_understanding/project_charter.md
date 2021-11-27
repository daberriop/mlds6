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
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?
* Who are the contact persons on both sides?
