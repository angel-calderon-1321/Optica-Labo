# Convolucion animada.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#definimos la función gaussiana
def f(x):
    return np.exp(-x**2)
#definimos la función escalonada
def g(x):
    return np.heaviside(x, 1)
#convolución entre dos funciones
def convolucion(f, g, x):
    dx = x[1] - x[0]  # Paso en x
    conv = np.convolve(f, g, mode='same') * dx  # Convolución y ajuste por el paso
    return conv

# Definimos el rango de x
x = np.linspace(-10, 10, 1000)

# Calculamos f(x) y g(x)
f_x = f(x)
g_x = g(x)

#convolución de f y g
convol = convolucion(f_x, g_x, x)

# Creamos la figura y los ejes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,8))
line, = ax1.plot([], [], lw=2, color='red')
ax1.plot(x, f_x, label='f(x) = exp(-x**2)', color='blue')
ax1.set_title('Convolución f * g')
ax1.set_xlim(-5, 5)
ax1.grid(True)

ax2.plot(x, convol, label='Convolución f * g')
ax2.set_title('Convolución de f y g')
ax2.set_xlim(-5, 5)
ax2.grid(True)
ax2.legend()

# Inicialización
def init():
    line.set_data([], [])
    return line,

# Función de animación
def update(frame):
    shift = frame * 0.1   # paso de desplazamiento
    y = g((-x + shift)-4)
    #y = np.sin(x - shift) # desplazamiento horizontal
    line.set_data(x, y)
    line.set_label(f'headside(x - {shift:.1f})')
    ax1.legend()
    return line,

# Animación
ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=350)

plt.show()