import numpy as np
import matplotlib.pyplot as plt
n = np.arange(21); # 0 < n < 20 olarak tanýmlanýyor
fo = 0.25;  #frekans deðeri belirtiliyor.

A = 2; #genlik deðeri belirtiliyor
signal = A*np.cos(2 * np.pi * n * fo) #ayrýk zamanlý sinyalin ifade edilmesi
plt.stem(n, signal) # ayrýk zamanlý sinyal grafik ile ifade ediliyor
plt.show() # grafik gösteriliyor

