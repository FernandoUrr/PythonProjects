#Importar paquetes nuevamente
import numpy as np
from numpy.random import normal 
import matplotlib.pyplot as plt 
from scipy.stats import norm
from numpy import hstack
from sklearn.neighbors import KernelDensity #Metodo de suavización

#sample = normal(size = 10000) #Generador de numeros aleatorios
#plt.hist(sample, bins = 30)
#plt.show()

#Estimación paramétrica
def pam():
    sample = normal(loc = 50, scale = 5, size = 1000) #mu = 50, sigma = 5
    mu = sample.mean()
    sigma = sample.std()
    dist = norm(mu, sigma)
    values = [value for value in range(30, 70)]
    p = [dist.pdf(value) for value in values]
    plt.hist(sample, bins = 30, density = True)
    plt.plot(values, p)
    return plt.show()

# pam() #Llama a la función y muestra la estimación paramétrica

#Estimación no paramétrica
def no_pam():
    sample1 = normal(loc = 20, scale = 5, size = 300)
    sample2 = normal(loc = 40, scale = 5, size = 700)
    sample = hstack((sample1, sample2))
    model = KernelDensity(bandwidth = 2, kernel = "gaussian") #Parámetro de suavización, distribución
    sample = sample.reshape((len(sample), 1)) #Arregla la estructura de datos
    model.fit(sample)

    values = np.asarray([value for value in range(1,60)])
    values = values.reshape((len(values), 1))
    p = model.score_samples(values) #Probabilidad logarítmica
    p = np.exp(p) #Probabilidad inversa
    plt.hist(sample, bins = 50, density = True)
    plt.plot(values, p)
    return plt.show()

no_pam()