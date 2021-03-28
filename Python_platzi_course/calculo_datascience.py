import matplotlib.pyplot as plt #Librería para graficar
import numpy as np #Libreria para manejo de vectores y utilidades matemáticas
#Función lineal

def f(m,x,b):
    return m*x + b

res = 100 #100 puntos

m = 10
b = 5

x = np.linspace(-10.0, 10.0, num=res) #En este caso, pongo rango inicial, final y numero de puntos en el rango
y = f(m, x, b)

fig, ax = plt.subplots()

ax.plot(x,y) #dominio y función
ax.grid() #Añade una los cuadrados
ax.axhline(y=0, color="r") #Línea Horizontal
ax.axvline(x=0, color="r") #Línea vertical
#Nos añade los límites a los gráficos
plt.ylim(-10, 10)
plt.xlim(-10, 10)

plt.show() #Me muestra la gráfica porque soy rebelde


