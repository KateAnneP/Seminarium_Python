# --- zadanie4 ---

#Wyznacz ranking skorelowania w danych serce.csv columny 'diagnoza' z innymi kolumnami. Podaj liste kolumn
#w porządku od nabardziej skorelowamych do najmniej skorelowanych wraz z podaniem współczynnika korelacji.
#Przetestuj wszystkie trzy rodzaje korelacji.

import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('../dane/serce.csv')

correlations_pearson = dane.corr(method='pearson')
correlations_kendall = dane.corr(method='kendall')
correlations_spearman = dane.corr(method='spearman')

print("Pearson Correlation:")
print(correlations_pearson['diagnoza'].sort_values(ascending=False))
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
cax = ax.matshow(correlations_pearson, vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()

print("\nKendall Correlation:")
print(correlations_kendall['diagnoza'].sort_values(ascending=False))
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
cax = ax.matshow(correlations_kendall, vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()

print("\nSpearman Correlation:")
print(correlations_spearman['diagnoza'].sort_values(ascending=False))
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
cax = ax.matshow(correlations_spearman, vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()