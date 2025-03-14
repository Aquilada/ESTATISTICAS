import numpy as hp
import matplotlib.pyplot as plt
from itertools import product
import pandas as pd
listacity = ['Itapetinigga', 'Tatuí', 'São Miguel Arcanjo', 'Capela do Alto', 'Sorocaba', 'Buri'] 
listafruit = ['Banana', 'Maçã', 'Pera', 'Uva', 'Morango']
#listacombinada = listacity + listafruit
#print(listacombinada)

df = pd.DataFrame (product (listacity, listafruit), columns = ['cidades', 'frutas']) 
hp.random.seed(42)
df ['produção' ]=hp.random.randint(0, 1000, size=len (df)) 
soma_frutas=df.groupby('frutas')['produção' ].sum() 
soma_frutas.to_csv('soma_frutas.csv', sep=';', decimal=',')
g_frutas_conjuntos = plt.bar(listafruit, soma_frutas)
plt.savefig('soma_frutas.pdf')
print(df)
print(soma_frutas)
