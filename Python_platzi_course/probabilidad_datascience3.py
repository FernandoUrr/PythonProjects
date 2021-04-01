#MLE = Maximun Likeilhood Estimation
#Problema de optimización
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
from matplotlib import cm
import numpy as np 
import pandas as pd 

def MLE():
    # print("""
    # Muestra la función de máxima verosimilitud
    # para una regresión logística
    # """)

    def likeilhood(y, yp):
        return yp*y + (1-yp)*(1-y)

    fig = plt.figure() #Crea un objeto figura
    ax = fig.gca(projection = "3d")

    Y = np.arange(0, 1, 0.1)
    YP = np.arange(0, 1, 0.1)
    Y, YP = np.meshgrid(Y, YP)

    Z = likeilhood(Y, YP)

    surf = ax.plot_surface(Y, YP, Z, cmap = cm.coolwarm)
    fig.colorbar(surf, shrink = 0.5, aspect = 5)
    return plt.show()

def MLElog():
    # print("""
    # Muestra la función de máxima verosimilitud
    # para una regresión logística cambiando por
    # p ==> log(p)
    # """)

    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    atrib_names = ["sepal length", "sepal width", "petal length", "petal width"]
    X, y = load_iris(return_X_y = True)
    clf = LogisticRegression(random_state = 10, solver = "liblinear").fit(X[:100], y[:100])
    return print(clf.coef_)
    
MLElog()
