import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def escalon(x):
    return  np.heaviside(x,1)

x = np.linspace(-10, 10, 1000)
# Las dos funciones a convolucionar
h_vals = escalon(x)
g_vals = escalon(x)
a = -3
g_vals_tras = escalon(a-x)

#Resultado de la convolución
conv_result = signal.convolve(h_vals, g_vals, mode='same')*0.01

# Inicializamos la figura
fig, axs = plt.subplots(2)
axs[0].plot(x, h_vals, 'r', lw=2, label=r'rect($\xi$)')
axs[0].plot(x, g_vals_tras, 'b', lw=2, label=r'rect(x-$\xi$)')

axs[1].plot(x, conv_result, 'k', lw=2, label='h * g (convolución)')
 
axs[0].set_title("Señal Originial y Filtro")
axs[0].legend()
axs[0].set_ylim([0, 1.5])
axs[0].set_xlim([-5, 5])
axs[0].set_xlabel(r'$\xi$')
axs[0].grid()

axs[1].set_title("Señal Filtrada")
axs[1].set_ylim([0, 1.5])
axs[1].set_xlim([-5, 5])
axs[1].set_xlabel('x')
axs[1].legend()
axs[1].grid()

fig.tight_layout()