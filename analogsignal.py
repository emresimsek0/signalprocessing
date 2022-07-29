
import numpy as np
import matplotlib.pyplot as plt

f = 10; # sinyalin frekans deðeri belirtiliyor.
t = np.arange(0.0, 1.0, 0.01)  # sinyalin 0 ile 1 saniye zaman aralýðýnda oluþtuðu belirtiliyor.
A = 2; # genlik deðeri belirtiliyor

sinyal = A*np.cos(2*np.pi*f*t) #2*cos(2*pi*f*t) sinyali tanýmlanýyor
plt.plot(t, sinyal, lw=5) #sinyali zamana göre deðiþiminin grafiðe aktarýlmasý
plt.show() #grafiði gösteren komuttur.