# --- Zadanie 10 ---

#Wykonać wykres punktowy ludności Polski na przestrzeni wieków.
#Dane do wykresu na stronie: https://pl.wikipedia.org/wiki/Ludno%C5%9B%C4%87_Polski
import matplotlib.pyplot as plt;
import numpy as np

lata = [1000, 1370, 1582, 1634, 1750, 1800, 1846, 1911, 1921, 1931, 1938, 1946, 1950, 1960, 1970, 1978, 1988, 1990, 1995, 2000, 2005, 2009, 2010, 2011, 2013, 2015, 2017, 2018, 2019, 2021, 2023]
ludnosc = [1, 1.9, 7.5, 11, 12, 9, 11.107, 22.11, 27.177, 32.107, 34.849, 23.93, 25.008, 29.776, 32.642, 35.061, 37.879, 28.183, 38.61, 38.654, 38.191, 38.167, 38.53, 38.538, 38.496, 38.437, 38.434, 38.411, 38.383, 38.1, 37.698]

plt.plot(lata, ludnosc, 'ro')
plt.xlabel('Rok')
plt.ylabel('Liczba ludności')
plt.title('Liczba ludności przez wieki')

plt.show()