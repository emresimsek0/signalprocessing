
import numpy as np
import matplotlib.pyplot as plt

f = 10; # sinyalin frekans de�eri belirtiliyor.
t = np.arange(0.0, 1.0, 0.01)  # sinyalin 0 ile 1 saniye zaman aral���nda olu�tu�u belirtiliyor.
A = 2; # genlik de�eri belirtiliyor

sinyal = A*np.cos(2*np.pi*f*t) #2*cos(2*pi*f*t) sinyali tan�mlan�yor
plt.plot(t, sinyal, lw=5) #sinyali zamana g�re de�i�iminin grafi�e aktar�lmas�
plt.show() #grafi�i g�steren komuttur.