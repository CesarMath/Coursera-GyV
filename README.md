# Coursera-GyV

En este repositorio estré subiendo las actualizaciones de mi información. A continuación se presente la priemra parte. 

Si hay algo de su interes o alguna duda, pueden contactarme por 
los siguientes medios:

- Facbook: ---
- Instagram: @DiableBlau
- Coursera

### Entrega-Fecha 1-Módulo 1

El libro de datos que he seleccionado es el que habla acerca de los cráteres de Marte ya que me interesa mucho la astronomía y la cantidad de datos a estudiar me parece impresionante, se pueden obtener mucha información a traves de ellos.

Y en particular el tema específico que me interesa es sobre algunas medidas de los cráteres, su morfología principal y el número de capas, es decir, consideraré de primera estancia las siguientes variables:

- CRATER_ID
- DEPTH_RIMFLOOR_TOPOG
- DIAM_CIRCLE_IMAGE
- MORPHOLOGY_EJECTA_1
- NUMBER_LAYERS

Por lo que adjunto en los documentos de este repositorio el arcihivo *DATA BOOK-propio* con las variables a ultilizar para mi investigación personal.

Y es que la pregunta inicial que tengo por responder es *¿Qué medidas de diametro y profundidad tienen la morfología más variada?, ¿Esa morfoloía implica mayor o menor numero de capas?* y para futuras investigaciones podemos preguntarnos si pasa algo similar en cráteres más recientes o en cráteres de otros planetas. 

Para tener una hipótesis inicial de las respuestas a estas preguntas hicimos una revisión bibliográfica rápida.

#### Revisió Bibliográfica
Las palabras clave utilizadas para la busqueda de infromación son las siguientes: cráteres de impacto, meteoritos, evolución geológica.

En [1] y [3] se nos muestra un informe acerca de cráteres complejos y de algunos patrones que pudieron observar los autores, y en ambos se tiene el patrón de que para cráteres en la Luna con menor profundidad y mayor diametro presentan morfologías de ejecta normal, lo que quiere decir que el material expulsadoa al mmento de la colisción entre un proyectil y el cuerpo astronómico, se exparció no muy lejos del propio impacto, mientra que para cráteres con mayor profundidad y menir diametro la morfología es más simple y la ejecta suele ser lineal y más distribuida. Esto último apoyado por [2].

Lo importante de esto, es que nos da pauta para proponer nuestra propia hipotesis de lo que podría pasar para el caso de los cráteres de Marte. 

*Hipotesis:* A menor profundidad la morfología ejecta varia más en los alrededores proximos del cráter, lo cual implica menor número de capas.

En las próximas semanas, al hacer el análisis de los datos veremos si nuestras hipotesis están cerca de la realidad. 


**Bibliografía**

- [1] Bartali, R y S. Colli, M. “Características de los cráteres de impacto: cráteres complejos”. Revista METEORITOS, ISSN 2605-2946. Año 2, No. 11, 2018, pp. 26-47.

- [2] Bartali, R y Urrutia Fucugauchi, J. “Importancia de los cráteres de impacto”. Revista METEORITOS, ISSN 2605- 2946. Año 2, No. 8, 2018, pp. 30-35.

- [3] Bartali R., Nahmad-Molinari Y., Rodríguez-Liñan G.M., 2015. Low speed granular-granular impact cráter opening mechanism in 2D experiments. Earth Moon and Planets (2015) 116:115-138.

## Entrega-Fecha 2-Módulo 2

En los documentos agregados en esta pagina les adjunto el archivo "Mark1.py" que es el programa de python en el que desarrollo el análisis de datos de mi archivo de datos sobre los cráteres de Marte.

En las primeras líneas de código mostramos la frecuencia de las siguientes variables:

### LONGITUDE
<img src="/imagenes/Longitud-distribucion.jpg" alt="LONGITUDE" />


### DIAM
<img src="/imagenes/diametro-distribucion.jpg" alt="DIAM" />



### NUMBER_LAYERS
<img src="/imagenes/capas-distribucion.jpg" alt="NUMBER_LAYERS" />

### MORPHOLOGY_EJECTA_1
<img src="/imagenes/morfologia-distribucion.jpg" alt="MORPHOLOGY_EJECTA_1" />


Después, dada que nuestra pregunta de interés se basa en la variedad de Morfología, creamos un nuevo sub-data basado en el que quitamos aquellos registros que no tienen ninguna forma de Morfología, haciendo un nuevo documento de datos con menos registros pero únicamente con los necesarios.

### Nuevo Data, con registros unicamente con datos de morfología
<img src="/imagenes/subdata-morfologia.jpg" alt="LONGITUDE" />


Al final, en el código, hicimos un análisis agrupando los datos de morfología para determinar la cantidad de registros por cada opción de morfología del que se tiene registro.

### VALORES AGRUADOS DE MORPHOLOGY_EJECTA_1
<img src="/imagenes/morfologia-valores-agrupados.jpg" alt="LONGITUDE" />

### Obervaciones
- Por los datos obtenidos, podemos decir que la morfología con mayor registro es "DLEPC" y "SLERS/Rd", por lo que son nuestras candidatas a tener una única capa, ya que por el anális de frecuencias la cantidad de registros con unaúnica capa es de 15467 registros.

- Lo siguiente a hacer es un análisis sobre esas morfologías mencionadas y su cantidad de capas. 

César 'Diablo de los números' Alejándrez &copy; 2025
