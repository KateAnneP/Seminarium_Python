# --- Zadanie 9 ---

#Rozwiązać rysunkowo problem wyznaczenia punktu przecięcia funkcji f1(x)=x^2+2x+2 oraz f2(x)=2/(x-1)

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 5, 400)

def f1(x):
    return x**2 + 2*x + 2

def f2(x):
    return np.where(x != 1, 2 / (x - 1), np.nan)

y1_values = f1(x)
y2_values = f2(x)

plt.plot(x, y1_values, label="f1(x) = x^2 + 2x + 2")
plt.plot(x, y2_values, label="f2(x) = 2/(x-1)")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.title('Wykres funkcji f1(x) i f2(x)')
plt.grid(True)
plt.show()