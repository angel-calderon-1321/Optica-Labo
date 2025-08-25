#Grafica de una función rect(x)
import numpy as np
import matplotlib.pyplot as plt

#definimos la función rect
def rect(x, long_onda=1, periodo=2):
    # reducimos x módulo periodo, pero centrado en 0
    x_mod = np.mod(x + periodo/2, periodo) - periodo/2
    return np.where(np.abs(x_mod-long_onda/2) <= long_onda/2, 1, -1)

#aprox. serie de fourier
def serie_fourier_rect(x, long_onda=1, periodo=2, N=10):
    suma = np.zeros_like(x)
    for n in range(1, N+1, 2):  # solo términos impares
        suma += (4/(n*np.pi)) * np.sin(2 * np.pi * n * x / periodo)
    return suma

# Parámetro de la función rect
long_onda = 1 # longitud de onda
periodo = long_onda  # periodo de la función
N = 4  # número de términos en la serie de Fourier
# Definimos el rango de x
x = np.linspace(-2*long_onda, 2*long_onda, 1000)
y = rect(x, long_onda, periodo)

#calculo aprox. serie de fourier
y_fourier = serie_fourier_rect(x, long_onda, periodo, N)

# Creamos la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label=f'rect(x), long_onda={long_onda}', color='blue')
ax.plot(x, y_fourier, label=f'Aprox. Serie de Fourier (N={N})', color='red')
ax.set_title('Función rect(x)')
ax.set_xlabel('x')
ax.set_ylabel('rect(x)')
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
ax.legend()
#plt.savefig('rect_function3.png')
plt.show()

