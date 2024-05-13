# --- Zadanie 14 ---

#Wykonać wykres kołowy liczby ludności w poszczególnych województwach.
#Dane do pobrania pod linkiem:
#http://www.gminy.pl/Rank/W/Rank_W_L.html

import matplotlib.pyplot as plt

nazwy_wojewodztw = ["mazowieckie", "śląskie", "wielkopolskie", "małopolskie", "dolnośląskie", "łódzkie", "pomorskie", "lubelskie", "podkarpackie", "kujawsko-pomorskie", "zachodniopomorskie", "warmińsko-mazurskie", "świętokrzyskie", "podlaskie", "lubuskie", "opolskie"]
ludnosc_wojewodztw = [5349114, 4570849, 3475323, 3372618, 2904207, 2493603, 2307710, 2139726, 2127657, 2086210, 1710482, 1439675, 1257179, 1188800, 1018075, 996011]

plt.figure(figsize=(10, 7))
plt.pie(ludnosc_wojewodztw, labels=nazwy_wojewodztw, autopct='%1.1f%%')
plt.title("Ludność wg województw (w mln)")
plt.show()
