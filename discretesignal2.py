
import numpy as np
import matplotlib.pyplot as plt

A = 1 #ayr�k sinyalin genlik de�eri
s = 101
n =  np.arange(s) # ayr�k sinyalin x ekseninidir ve n domenini temsil eder
y = A*np.cos(2*np.pi* (n/32)) #ayr�k sinyalin ifadesi
plt.stem(n,y)#ayr�k sinyalin grafikte belirlenmesi
plt.show()

