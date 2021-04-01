import numpy as np
from numpy.random import binomial
from scipy.stats import binom #Importa del paquete scipy el atributo stats
from math import factorial
import matplotlib.pyplot as plt

# def b(k, n, p):
#     return factorial(n)/(factorial(k)*factorial(n-k))*pow(p,k)*pow(1-p,n-k)

# resultado = 0
# for i in 0, 1, 2:
#     resultado = resultado + b(i, n = 3, p = 0.5)

# print(f"La probabilidad acumulada es {resultado}")

# #Calcular con librería SciPy
# dist = binom(3, 0.5)
# dist.pmf(2) #Probability mass function

# dist.cdf(2) #Cummulaive density function`

#Simular una secuencia con generador aleatorio
p = 0.5
n = 3

#Realizar en jumpynotebook
def plot_hist(num_trials):
    values = [0, 1, 2, 3]
    arr = []
    for _ in range(num_trials):
        arr.append(binom(n, p))
    sim = np.unique(arr, return_counts = True)[1]/len(arr)
    teorica = [binom(3, 0.5).pmf(k) for k in values]
    plt.bar(values, sim, color = "red")
    plt.bar(values, teorica, alpha = 0.5, color ="blue")
    plt.title(f"{num_trials} experimentos")
    plt.show()

plot_hist(20)