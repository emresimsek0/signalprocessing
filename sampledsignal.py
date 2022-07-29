import numpy as np
import matplotlib.pyplot as plt
FS = 100 #�rnekleme frekans�
F = 50 #analog sinyalin frekans� 50 dir ve sabittir
A = 1 #analog sinyalin genlik de�eri
T = 1 / F #analog sinyalin periyodu
TS = 1 / FS # ornekleme sinyalin periyodu
cycles = 11 # d�ng� say�s�
t = np.arange(0.0 ,0.21 ,0.001) #analog sinyalin gerceklesti�i zaman aral���
x = A*np.cos(2*np.pi*F*t) # x(t) analog sinyalin elde edilmesi
n = np.arange(0,cycles*T,TS) #orneklenen sinyalin n domeni 
y = A*np.cos(2*np.pi*(F/FS)*n) # orneklenen sinyali ifade eder

plt.plot(t,x,'C1',label = 'analog')
plt.stem(n,y,'C2', label = 'orneklenmis')
plt.legend() 
plt.show() # grafikleri g�r�nt�ler


