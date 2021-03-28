import matplotlib.pyplot as plt
import numpy as np
#Funciones trascendentales: cosenos, senos, exponenciales, logaritmo
def f(x):
    return np.cos(x)

res = 100 #100 puntos

x = np.linspace(-10.0, 10.0, num=res) #En este caso, pongo rango inicial, final y numero de puntos en el rango
y = f(x)

fig, ax = plt.subplots()

ax.plot(x,y) #dominio y función
ax.grid() #Añade una los cuadrados
ax.axhline(y=0, color="r") #Línea Horizontal
ax.axvline(x=0, color="r") #Línea vertical
#Nos añade los límites a los gráficos
plt.ylim(-5, 5)
plt.xlim(-10, 10)

plt.show() #Me muestra la gráfica porque soy rebelde