print("Bienvenido señor Stark")

import pandas
import numpy 

data = pandas.read_csv("craters-data.csv", low_memory=False)

print("El número de obersaviones es",  len(data)) #Cantidad de datos
print("El número de variables es",  len(data.columns)) #Cantidad de variables

print("Las variables son las siguientes:")
print(data.columns)

c1=data["LONGITUDE"].value_counts(sort=False) 
#Crea una tabala para ver cuantas veces aparece cada dato de longitud, como casi ningun crater
#tiene la mimsa logitud, entonces cada dato aparece normalmente una vez
print(c1)

p1=data["LONGITUDE"].value_counts(sort=False, normalize=True)
#Crea una tabala para ver los porcentajes de aparacipon de cada dato, es como arriba pero
#con porcertajes, cada dato de longitud tiene un porcentaje de aparición muy bajo
print(p1)

c2 = data["DIAM"].value_counts(sort=False)
print(c2)

p2=data["DIAM"].value_counts(sort=False,normalize=True)
print(p2)

c3 = data["NUMBER_LAYERS"].value_counts(sort=False)
print(c3)

p3 = data["NUMBER_LAYERS"].value_counts(sort=False,normalize=True)
print(p3)