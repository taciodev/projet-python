import pandas as pd
import numpy as np


# 1.
""" 
dataset = pd.read_csv('./dadosreduzidos.csv')

dataset['Month'] = np.random.randint(1,13,size=1797)

df_aux = dataset[['Month','DepDelay','ArrDelay','Cancelled']].copy()
df_aux = df_aux[df_aux['Cancelled'] == 0]
obj = df_aux.groupby(['Month']).mean()

obj.index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

print(obj)

# Construção do gráfico

plt.bar(obj.index, obj['DepDelay'])

plt.xticks(range(1,13))
plt.xlabel('mes')
plt.ylabel('atraso em minutos')
plt.xticks(range(13))
plt.show()  """

# 2.

""" dataset2 = pd.read_csv('./dadosreduzidos.csv')

df_aux2 = dataset2[['UniqueCarrier','DepDelay','ArrDelay','Cancelled']].copy()

df_aux2 = df_aux2[df_aux2['Cancelled'] == 0]

obj2 = df_aux2.groupby(['UniqueCarrier']).mean()

print(obj2) """

# Construção do gráfico

""" plt.bar(obj.index, obj['DepDelay'])

plt.xticks(range(1,13))
plt.xlabel('mes')
plt.ylabel('atraso em minutos')
plt.xticks(range(13))
plt.show()  """

# 3. Qual a quantidade de voos por rota

dataset3 = pd.read_csv('./dadosreduzidos.csv')

""" r = dataset3.groupby(['Origin','Dest']).size()

print(r) """

o = dataset3.groupby(['Origin']).size()

d = dataset3.groupby(['Dest']).size()

table = pd.concat([o,d])

print(table)





# 4. Qual a concentração de voos por aeroporto

# a)voos cancelados (aeroporto de origem)

# b)voos realizados (aeroporto de origem)

# c)voos cancelados (aeroporto de destino)

# d)voos realizados (aeroporto de destino)
