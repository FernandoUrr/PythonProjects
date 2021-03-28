#Funciones dentro de otras funciones
import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return x**2

def f(x):
    return np.sin(x)

x = np.linspace(-10, 10 , num = 1000) #Genera un vector
fog = f(g(x)) #Función compuesta
plt.plot(x, fog)
plt.show()