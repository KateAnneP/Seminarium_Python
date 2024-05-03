# --- Zadanie 13 ---

#Wykonać wykres słupkowy struktura płci i wieku ludności w Polsce w grupach wiekowych: 0-14, 15-64, 65+
#Każdą grupę charakteryzujemy przez liczbę kobiet i mężczyzn.
#Dane do pobrania pod linkiem:
#https://pl.wikipedia.org/wiki/Ludno%C5%9B%C4%87_Polski

import matplotlib.pyplot as plt
import numpy as np

n_groups = 3
grupa_wiekowa = ['0-14', '15-64', '65+']
mezczyzni = [2979026, 13615652, 2056763]
kobiety = [2828298, 13707173, 3346877]

fig, ax = plt.subplots()
index = np.arange(n_groups)

bar_width = 0.25
opacity = 0.8

slupek1 = plt.bar(index, mezczyzni, bar_width, alpha=opacity, color='b', label='mężczyzni')
slupek2 = plt.bar(index + bar_width, kobiety, bar_width, alpha=opacity, color='r', label='kobiety')

plt.xlabel('Grupy wiekowe')
plt.ylabel('Liczba ludności (mln)')
plt.title('Podział ludności w grupach wiekowych')

plt.xticks(index + bar_width, grupa_wiekowa)
plt.legend()

plt.tight_layout()

fig = plt.gcf()
fig.set_size_inches(10, 8)

plt.show()