# --- zadanie3 ---

#Wyznacz ranking skorelowania w danych irysy.csv columny 'gatunek' z innymi kolumnami. Podaj liste kolumn
#w porządku od nabardziej skorelowamych do najmniej skorelowanych wraz z podaniem współczynnika korelacji.
#Przetestuj wszystkie trzy rodzaje korelacji.

import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn.preprocessing import LabelEncoder

dane = pd.read_csv('../dane/iris.csv', index_col=0)

names = ['sepal length','sepal width','petal length','petal width','label']
label_encoder = LabelEncoder()
dane['label'] = label_encoder.fit_transform(dane['label'])

correlations_pearson = dane.corr(method='pearson')
correlations_kendall = dane.corr(method='kendall')
correlations_spearman = dane.corr(method='spearman')

print("Pearson Correlation:")
print(correlations_pearson)
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
cax = ax.matshow(correlations_pearson, vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()

print("\nKendall Correlation:")
print(correlations_kendall)
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
cax = ax.matshow(correlations_kendall, vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()

print("\nSpearman Correlation:")
print(correlations_spearman)
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
cax = ax.matshow(correlations_spearman, vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()