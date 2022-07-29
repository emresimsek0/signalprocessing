import numpy as np
import matplotlib.pyplot as plt
import random
A = 1 #sinyalin genlik deðerini temsil eder
s = 101
n = np.arange(s) # orneklenen sinyalin  x eksenini ifade eder
x = A*np.cos(2*np.pi* (n/32)) #orneklenen sinyali ifade eder
e = 0.0008*np.asarray(random.sample(range(0,1000),s)) #gürültü sinyalini ifade eder
y = x+e #toplam sinyali ifade eder
plt.stem(n,y)    
plt.show()


