import pandas as pd

document = pd.read_csv('C://Users//Мвидео//Downloads//transactions.csv')
filt = document['STATUS'] == 'OK'
first = document.loc[filt].sort_values(by='SUM', ascending=False).head(3)
filt2 = document['CONTRACTOR'] == 'Umbrella, Inc'
second = document.loc[filt & filt2]
summa = second['SUM'].sum()
print(first)
print(summa)
