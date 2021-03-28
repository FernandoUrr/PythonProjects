#Soluciones de todos los ejercicios en el apéndice D
"""Algoritmo para realizar descenso
del gradiente"""

from matplotlib import cm
import numpy as np 
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(subplot_kw = {"projection":"3d"})
#Ahora, definir la función de costos
def f(x, y):
    return x**2 + 3*y**2 + 2*x + y

res = 1000
#Se generan los vectores que darán valores a x y y
x = np.linspace(-4, 4, res)
y = np.linspace(-4, 4, res)

x, y = np.meshgrid(x, y)
z = f(x, y)

#Ahora hacer las curvas de nivel
surf = ax.plot_surface(x, y, z, cmap = cm.cool)
fig.colorbar(surf)

level_map = np.linspace(np.min(z), np.max(z), num = res)
plt.contourf(x, y, z, level_map)
plt.title("Descenso del gradiente")
#Seleccionar punto aleatorio entre 0 y 1
p = np.random.rand(2)* 8 - 4
plt.plot(p[0], p[1], "o", c = "k")

h = 0.001
lr = 0.001

def derivada (cp , p):
    return (f(cp[0], cp[1]) - f(p[0], p[1]))/h
    #Se usa definición de límites de la derivada

def gradiente(p):
    grad = np.zeros(2)
    for i, val in enumerate(p):
        cp = np.copy(p)
        cp[i] = cp[i] + h
        dp = derivada(cp, p)
        grad[i] = dp

    return grad

for i in range(1000):
    p = p - lr*gradiente(p)
    if i%10 == 0:
        plt.plot(p[0], p[1], "o", c = "r")

plt.plot(p[0], p[1], "o", c = "w")




