# --- Zadanie 11 ---

#Wykonać wykres punktowy ludności Polski w latach 1950-2017 (jest tam 8 pomiarów) z podziałem na miasta,
#wieś i razem  (będą trzy rodzaje punktów).
#Dane do wykresu na stronie: https://pl.wikipedia.org/wiki/Ludno%C5%9B%C4%87_Polski
import matplotlib.pyplot as plt;

lata = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2017]
razem = [25, 29.8, 32.7, 35.7, 38.1, 38.3, 38.5, 38.4]
miasta = [9.225, 14.39, 17.1, 20.96, 23.55, 23.71, 23.41, 23.08]
wsie = [razem[0] - miasta[0], miasta[1] - razem[1], razem[2] - miasta[2], razem[3] - miasta[3], razem[4] - miasta[4], razem[5] - miasta[5], razem[6] - miasta[6], razem[7] - miasta[7]]

plt.plot(lata, razem, 'ro', lata, miasta, 'bs', lata, wsie, 'g^')
plt.xlabel('Rok')
plt.ylabel('Liczba ludności (mln)')
plt.title('Ludność Polski we wsiach, miastach i razem w latach 1950 - 2017')

plt.show()