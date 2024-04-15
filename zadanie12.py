# --- Zadanie 12 ---

#Wykonać wykres słupkowy liczby ludności w poszczególnych województwach.
#Dane do pobrania pod linkiem:
#http://www.gminy.pl/Rank/W/Rank_W_L.html
import matplotlib.pyplot as plt

nazwy_wojewodztw = ["mazow", "ślą", "wielk", "małopl", "dolnośl", "łódz", "pomor", "lubel", "podkarp", "kujawsko-pom", "zachodniopom", "warmińsko-maz", "świętok", "podl", "lubus", "opol"]
ludnosc_wojewodztw = [5349114, 4570849, 3475323, 3372618, 2904207, 2493603, 2307710, 2139726, 2127657, 2086210, 1710482, 1439675, 1257179, 1188800, 1018075, 996011]
pozycje = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

plt.figure(figsize=(15, 7)) #Rozmiary okna z wykresem
plt.bar(pozycje, ludnosc_wojewodztw, align='center', alpha=0.9)
plt.xticks(pozycje, nazwy_wojewodztw)
plt.ylabel("Liczba ludności (mln)")
plt.title("Liczba ludności wg województw")
plt.show()