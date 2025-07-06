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
DIAM
82.10    1
82.02    1
79.63    1
74.81    1
73.53    2
        ..
31.18    1
30.94    2
30.56    1
29.74    1
28.42    1


### NUMBER_LAYERS
0    364612
3       739
2      3435
1     15467
4        85
5         5

### MORPHOLOGY_EJECTA_1
                      339718
Rd/MLERS                 199
Rd                     24892
Rd/DLEPC/DLERS            33
SLERS                   4828
                       ...
MLEPC/MLERC/MSLEPS         1
DLERCPd/DLERSPd            1
MLERSRd                    1
DLERC/Rd/SLERS             1
Rd/SLEPCRd                 1

Después, dada que nuestra pregunta de interés se basa en la variedad de Morfología, creamos un nuevo sub-data basado en el que quitamos aquellos registros que no tienen ninguna forma de Morfología, haciendo un nuevo documento de datos con menos registros pero únicamente con los necesarios.

### Nuevo Data, con registros unicamente con datos de morfología
CRATER_ID CRATER_NAME  LONGITUDE   DIAM MORPHOLOGY_EJECTA_1  NUMBER_LAYERS
1       01-000001     Korolev    164.464  82.02            Rd/MLERS              3
8       01-000008                 13.829  58.40                  Rd              0
12      01-000012       Dokka   -145.681  51.08                  Rd              0
20      01-000020                177.982  45.71      Rd/DLEPC/DLERS              2
25      01-000025                 -7.939  39.51               SLERS              1
...           ...         ...        ...    ...                 ...            ...
378373  30-007721               -133.362   1.53                  Rd              0
378404  30-007752               -125.126   1.53                  Rd              0
378457  30-007805               -121.640   1.52                  Rd              0
378520  30-007868               -115.428   1.51                  Rd              0
378532  30-007880                122.205   1.51                  Rd              0

[44625 rows x 6 columns]


Al final, en el código, hicimos un análisis agrupando los datos de morfología para determinar la cantidad de registros por cada opción de morfología del que se tiene registro.

### VALORES AGRUADOS DE MORPHOLOGY_EJECTA_1
DLEPC             232
DLEPC/DLEPCPd       4
DLEPC/DLEPS       145
DLEPC/DLEPS/Rd      2
DLEPC/DLEPSPd       3
                 ...
SLERS/Rd          281
SLERS/Rd/SLERS      1
SLERSPd            16
SLERSRd             4
SLErS               1
Length: 155, dtype: int64

### Obervaciones
- Por los datos obtenidos, podemos decir que la morfología con mayor registro es "DLEPC" y "SLERS/Rd", por lo que son nuestras candidatas a tener una única capa, ya que por el anális de frecuencias la cantidad de registros con unaúnica capa es de 15467 registros.

- Lo siguiente a hacer es un análisis sobre esas morfologías mencionadas y su cantidad de capas. 

César 'Diablo de los números' Alejándrez &copy; 2025
