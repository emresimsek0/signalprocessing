
import numpy as np
import matplotlib.pyplot as plt

A = 1 #ayrýk sinyalin genlik deðeri
s = 101
n =  np.arange(s) # ayrýk sinyalin x ekseninidir ve n domenini temsil eder
y = A*np.cos(2*np.pi* (n/32)) #ayrýk sinyalin ifadesi
plt.stem(n,y)#ayrýk sinyalin grafikte belirlenmesi
plt.show()

