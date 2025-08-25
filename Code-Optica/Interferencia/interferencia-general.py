import numpy as np
import matplotlib.pyplot as plt

# Defino intensidades de dos ondas
I1 = 1.0
I2 = 0.5

# Rango de diferencias de fase
phi = np.linspace(0, 2 * np.pi, 500)

# Intensidad resultante
I = I1 + I2 + 2 * np.sqrt(I1 * I2) * np.cos(phi)

# Graficar
plt.plot(phi, I)
plt.title('Patrón de Interferencia')
plt.xlabel('Diferencia de Fase (Δφ)')
plt.ylabel('Intensidad')
plt.grid(True)
plt.show()
