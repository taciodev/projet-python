import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1.

dataset = pd.read_csv('./dadosreduzidos.csv')
dataset['Month'] = np.random.randint(1,13,size=1797)
df_aux = dataset[['Month','DepDelay','ArrDelay','Cancelled']].copy()
df_aux = df_aux[df_aux['Cancelled'] == 0]
obj = df_aux.groupby(['Month']).mean()
obj.index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#print(obj)
# Construção do gráfico
plt.bar(obj.index, obj['DepDelay'])
plt.bar(obj.index, obj['ArrDelay'])
plt.xticks(range(1,13))
plt.xlabel('mes')
plt.ylabel('atraso em minutos')
plt.xticks(range(13))
#plt.show()

# 2.
dataset2 = pd.read_csv('./dadosreduzidos.csv')
df_aux2 = dataset2[['UniqueCarrier','DepDelay','ArrDelay','Cancelled']].copy()
df_aux2 = df_aux2[df_aux2['Cancelled'] == 0]
obj2 = df_aux2.groupby(['UniqueCarrier']).mean()
print(obj2)

'''# Construção do gráfico

plt.bar(obj2.index, obj2['UniqueCarrier'])
plt.xticks(range(1,13))
plt.xlabel('Companhia')
plt.ylabel('atraso em minutos')
plt.xticks(range(13))
plt.show()'''

# 3. Qual a quantidade de voos por rota

dataset3 = pd.read_csv('./dadosreduzidos.csv')

""" r = dataset3.groupby(['Origin','Dest']).size()
print(r) """

o = dataset3.groupby(['Origin']).size()

d = dataset3.groupby(['Dest']).size()

table = pd.concat([o,d])

#print(table)






# 4. Qual a concentração de voos por aeroporto0
dataset4 = pd.read_csv('./dadosreduzidos.csv')
# a)voos cancelados (aeroporto de origem)
df_aux4a = dataset4[['Origin','Cancelled']].copy()
df_aux4a = df_aux4a[df_aux4a['Cancelled'] == 1]
df_aux4a = df_aux4a.groupby(['Origin']).count()
#print(df_aux4a)

# b)voos realizados (aeroporto de origem)

df_aux4b = dataset4[['Origin','Cancelled']].copy()
df_aux4b = df_aux4b[df_aux4b['Cancelled'] == 0]
df_aux4b = df_aux4b.groupby(['Origin']).count()
df_aux4b=df_aux4b.rename(columns={'Cancelled':'Realizados'})
print(df_aux4b)

# c)voos cancelados (aeroporto de destino)
df_aux4c = dataset4[['Dest','Cancelled']].copy()
df_aux4c = df_aux4c[df_aux4c['Cancelled'] == 1]
df_aux4c = df_aux4c.groupby(['Dest']).count()
#print(df_aux4c)


# d)voos realizados (aeroporto de destino)
df_aux4d = dataset4[['Dest','Cancelled']].copy()
df_aux4d = df_aux4d[df_aux4d['Cancelled'] == 0]
df_aux4d = df_aux4d.groupby(['Dest']).count()
df_aux4d=df_aux4d.rename(columns={'Cancelled':'Realizados'})
print(df_aux4d)
