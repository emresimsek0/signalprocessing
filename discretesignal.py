import numpy as np
import matplotlib.pyplot as plt
n = np.arange(21); # 0 < n < 20 olarak tan�mlan�yor
fo = 0.25;  #frekans de�eri belirtiliyor.

A = 2; #genlik de�eri belirtiliyor
signal = A*np.cos(2 * np.pi * n * fo) #ayr�k zamanl� sinyalin ifade edilmesi
plt.stem(n, signal) # ayr�k zamanl� sinyal grafik ile ifade ediliyor
plt.show() # grafik g�steriliyor

