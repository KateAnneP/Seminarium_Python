# --- Zadanie 2 ---

#Jedną z najważniejszych w dzisiejszych czasach miar znaczenia państw jest wielkość produktu krajowego
#brutto (w skrócie PKB), a miarą zamożności obywateli jest wielkość PKB na jednego mieszkańca.
#W 2006 roku PKB Polski wyniósł 14880 USD. Natomiast przyrost PKB w stosunku do roku 2005 był na poziomie 6,2%.
#Dla porównania, PKB Niemiec na jednego mieszkańca w 2005 roku wyniósł 33400 USD przy wzroście w stosunku do
#roku 2004 o 1,6%. Zakładając, że w ciągu kolejnych lat tempo wzrostu PKB w Polsce i w Niemczech nie zmieniło się,
#napisać program, który odpowie na dwa następujące pytania.
#1.Ile lat miało minąć, aby PKB Polski podwoił się?
#2.Ile lat miało minąć, aby PKB Polski przewyższył PKB Niemiec?

#ad 1.
przyrost = 0.062
PKB_pl_06 = 14880
PKB_pl = PKB_pl_06 + (PKB_pl_06 * przyrost)

ilosc_lat = 0

while (PKB_pl < PKB_pl_06*2):
    ilosc_lat = ilosc_lat + 1
    PKB_pl = PKB_pl + (PKB_pl * przyrost)
    #print(f"PKB: {PKB_pl}")
    #print(f"Ilość lat: {ilosc_lat}")

print(f"Minęło {ilosc_lat} zanim PKB Polski podwoiło się w stosunku do 2006 roku")

#ad 2.
PKB_de_05 = 33400
przyrost2 = 0.016   #przyrost dla Niemiec
PKB_de = PKB_de_05 + (PKB_de_05 * przyrost2)    #PKB Niemiec w 2006
PKB_pl = PKB_pl_06

ilosc_lat2 = 0

while (PKB_pl < PKB_de):
    ilosc_lat2 = ilosc_lat2 + 1
    PKB_pl = PKB_pl + (PKB_pl * przyrost)
    PKB_de = PKB_de + (PKB_de * przyrost2)
    # print(f"PKB_pl: {PKB_pl}")
    # print(f"PKB_de: {PKB_de}")
    # print(f"ilosc_lat2: {ilosc_lat2}")

print(f"Minęło {ilosc_lat2} zanim PKB Polski przekroczyło PKB Niemiec")


