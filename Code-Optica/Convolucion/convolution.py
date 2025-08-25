#voy a hacer la convolucion de dos funciones unidimensionales f(x) y g(x).

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, correlate

def f(x):
    return np.exp(-x**2)
def g(x):
    'funcion escalonada'
    return np.heaviside(x, 1)
#Convolución entre dos funciones
def convolucion(f, g, x):
    '''Calcula la convolución de dos funciones f y g sobre el eje x.'''
    dx = x[1] - x[0]  # Paso en x
    conv = convolve(f, g, mode='same') * dx  # Convolución y ajuste por el paso
    return conv
#Correlación entre dos funciones
def correlacion(f, g, x):
    '''Calcula la correlación cruzada de dos funciones f y g sobre el eje x.'''
    dx = x[1] - x[0]  # Paso en x
    corr = correlate(f, g, mode='same') * dx  # Correlación y ajuste por el paso
    return corr

#Definimos el rango de x
x = np.linspace(-4, 4, 1000)  # Rango de x
#Calculamos f(x) y g(x)
f_x = f(x)
g_x = g(x)
#Calculamos la convolución
conv_result = convolucion(f_x, g_x, x)
#Calculamos la correlación
corr_result = correlacion(f_x, g_x, x)

#Graficamos los resultados
plt.figure(figsize=(8, 8))
plt.subplot(4, 1, 1)
plt.plot(x, f_x, label='f(x) = exp(-x**2)', color='blue')
plt.title('Funciones y su Convolución')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.subplot(4, 1, 2)
plt.plot(x, g_x, label='g(x) = exp(-x**2 / 2)', color='orange')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()
plt.grid()
plt.subplot(4, 1, 3)
plt.plot(x, conv_result, label='Convolución f * g', color='green')
plt.xlabel('x')
plt.ylabel('Convolución')
plt.legend()
plt.grid()
plt.subplot(4, 1, 4)
plt.plot(x, corr_result, label='Correlación f ⋆ g', color='red')
plt.xlabel('x')
plt.ylabel('Correlación')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('convolucion.png', dpi=300) #Guardamos la figura
plt.show()