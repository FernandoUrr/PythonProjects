import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm

#dist = norm(0, 1)
# x = np.arange(-4, 4, 0.1) #Linspace no funciona con floats
# y = [dist.pdf(value) for value in x]
# plt.plot(x, y)
# plt.show()

#Panda sirve para leer dataframes
df = pd.read_excel("data_frames/s057.xls")
arr = df["Normally Distributed Housefly Wing Lengths"].values[4:]
# values, dist = np.unique(arr, return_counts = True)
# plt.bar(values, dist)
# plt.show()
#Estimar la distribución
mu = arr.mean() #Calcula el promedio
sigma = arr.std() #Calcula la desviación
dist = norm(mu, sigma)
x = np.arange(30, 60, 0.1)
y = [dist.pdf(value) for value in x]
plt.plot(x, y)
values, dist = np.unique(arr, return_counts = True)
plt.bar(values, dist/len(arr))
plt.show()