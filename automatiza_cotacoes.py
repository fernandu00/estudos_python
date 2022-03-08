import pandas as pd
import pandas_datareader as pdr
import yfinance
from datetime import date

inicio20 = '2020-01-01'

final20 = '2020-12-31'

inicio21 = '2021-01-01'

final21 = '2021-12-31'

acao = input('Digite uma ação: ')


# pega primeiro preço de 2020

df = pdr.data.get_data_yahoo(acao,start=inicio20,end=final20)

primeiro_20 = df.head(1)

p = primeiro_20.iloc[0]['Adj Close']

primeiro20 = str(round(p,2))

# print(primeiro20)


# pega ultimo preço de 2020

df = pdr.data.get_data_yahoo(acao,start=inicio20,end=final20)

ultimo_20 = df[-1:]

ult = ultimo_20.iloc[0]

u = ultimo_20.iloc[0]['Adj Close']

ultimo20 = str(round(u,2))

# print(ultimo20)



# pega o preço minimo de 2020

ordenaMin = df.sort_values(by=['Adj Close'])

ordem = ordenaMin.iloc[0]['Adj Close']

minimo20 = str(round(ordem,2))

# print(minimo20)


# pega o preço maximo de 2020

ordenaMax = df.sort_values(by=['Adj Close'],ascending=False)

ordem = ordenaMax.iloc[0]['Adj Close']

maximo20 = str(round(ordem,2))

# print(maximo20)


# pega primeiro preço de 2021

df2 = pdr.data.get_data_yahoo(acao,start=inicio21,end=final21)

primeiro_21 = df2.head(1)

pri = primeiro_21.iloc[0]

p = primeiro_21.iloc[0]['Adj Close']

primeiro21 = str(round(p,2))

# print(primeiro21)


# pega ultimo preço de 2021
df2 = pdr.data.get_data_yahoo(acao,start=inicio21,end=final21)

ultimo_21 = df2[-1:]


u = ultimo_21.iloc[0]['Adj Close']

ultimo21 = str(round(u,2))

# print(ultimo21)


# pega o preço minimo de 2021

df2 = pdr.data.get_data_yahoo(acao,start=inicio21,end=final21)

ordenaMin = df2.sort_values(by=['Adj Close'])

ordem = ordenaMin.iloc[0]['Adj Close']

minimo21 = str(round(ordem,2))

# print(minimo21)


# pega o preço maximo de 2021

ordenaMax = df2.sort_values(by=['Adj Close'],ascending=False)

ordem = ordenaMax.iloc[0]['Adj Close']

maximo21 = str(round(ordem,2))

# print(maximo21)


# variacao do preço em 2020

variacao = pd.concat([primeiro_20,ultimo_20])

variacao.head()

var = variacao.pct_change()

va = var.iloc[1]['Adj Close']

va = "{:.2%}".format(va)

# print(va)


# variacao do preço em 2021

variacao = pd.concat([primeiro_21,ultimo_21])

variacao.head()

var21 = variacao.pct_change()

va21 = var21.iloc[1]['Adj Close']

va21 = "{:.2%}".format(va21)

# print(va21)


print(f'\n {acao} \n 2020 \n Último preço : {ultimo20} \n Preço Máximo: {maximo20} \n Preço Mínimo: {minimo20} \n \n 2021 \n Último preço : {ultimo21} \n Preço Máximo: {maximo21} \n Preço Mínimo: {minimo21} \n \n Variação em 2020: {va} \n Variação em 2021: {va21}')
