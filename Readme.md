# Proyecto Trasversal de "Gestión de Proyectos de Investigación y Ciencia Abierta"
## Titulo: Características de la Población con mayor adopción del Bitcoin como moneda de curso legal en el Salvador. 

### Artículo:
#### Graham, K., & Knittel, C. R. (2024). Assessing the distribution of employment vulnerability to the energy transition using employment carbon footprints. Proceedings of the National Academy of Sciences, 121 (7), e2314773121. https://doi.org/10.1073/pnas.2314773121

### Integrantes:
#### Yilmer Alexis Palacios Rodriguez / Analista de datos
#### Kevin Andres Rico Torres / Econometrista
#### Juan Felipe Vargas Guacheta / Documentador técnico

### Descripción general del proyecto de replicación:

Una de las grandes conclusiones del artículo es que hay características de la población que los hace más abiertos a adoptar el uso de la aplicación Chivo, es decir, que hay características que hacen más probable que usen el Bitcoin; los autores encontraron que las personas que han intentado descargar Chivo son principalmente personas jóvenes, educadas y bancarizadas; consideramos que identificar estas características son relevantes a la hora de entender el potencial de adopción de la tecnología en países similares al Salvador y es por esto que queremos replicar el estudio de esta conclusión. Para esto debemos realizar una limpieza y procesamiento de los datos suministrados por la encuesta nacional del 2022, y realizaremos una regresión MPL donde la variable dependiente es "Have you tried to download Chivo?" y las independientes son diferentes caracteristicas de los encuestados.

### Directorio y Explicación

#### Directorio:  
 ├───Codigo_Fuente  
 ├───Data  
 │   ├───Data_raw  
 │   └───Data_procesada  
 ├───Docs  
 └───Resultados  

* Cógido Fuente: Alcena el código usado para realizar los modelos de probabilidad lineal MPL.
* Data: Contiene los datos
* Data_raw: Contiene los datos originales de la encuesta nacional del 2022.
* Data_procesada: Contiene los datos limpiados y procesados, listos para correr los modelos. 
* Docs: Se almacenan los documentos originales de la investigación, y la documentación relacionada con el proyecto de replicación.
* Resultados: Almacena las tablas con los resultados de los modelos corridos en la reproducción.

### Requisitos iniciales identificados
* Software para procesamiento de texto
* Software para procesamiento de datos y de modelamiento estadistico


