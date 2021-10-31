import pandas as pd
import matplotlib.pyplot as plt

document = pd.read_csv('flights.csv')
prices = document.groupby('CARGO')['PRICE'].sum()
weights = document.groupby('CARGO')['WEIGHT'].sum()
flights = document.groupby('CARGO')['CARGO'].size()

x = ['Jumbo', 'Medium', 'Nimble']
y_flights = [flights[0], flights[1], flights[2]]
y_prices = [prices[0], prices[1], prices[2]]
y_weights = [weights[0], weights[1], weights[2]]

fig, ax = plt.subplots()

ax.bar(x, y_prices)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
plt.title('overall prices')
plt.show()

fig, ax = plt.subplots()

ax.bar(x, y_weights)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
plt.title('Overall weight')
plt.show()

fig, ax = plt.subplots()

ax.bar(x, y_flights)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
plt.title('Number of flights')
plt.show()



