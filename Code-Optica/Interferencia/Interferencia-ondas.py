import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros, para la AMPLITUD ESPACIAL
A1 = 1  # Amplitud del primer campo
A2 = A1
#A2 = 0.7  # Amplitud del segundo campo
k1= 2 * np.pi / 600  # Número de onda, onda 1
k2 = 2 * np.pi / 600  # Número de onda, onda 2
delta1 = 0  # Fase inicial del primera onda
delta2 = np.pi # Fase inicial del segunda onda

# Definir el rango de tiempo
x = np.linspace(0, 1000, 1000)

#diferencia de fase
phi1 = k1*x + delta1 #fase de onda 1
phi2 = k2*x + delta2 #fase de onda 2
d_fase = phi2 - phi1

# Calcular los campos eléctricos
E1 = A1 * np.cos(phi1)
E2 = A2 * np.cos(phi2)

#Intensidades individuales
I1 = E1**2
I2 = E2 **2

#Intensdad resultante
I = I1+I2+2*np.sqrt(I1*I2)*np.cos(d_fase)

# Graficar los campos eléctricos y el resultante
plt.figure(figsize=(10, 6))
plt.plot(x, E1, '-',label='campo E1')
plt.plot(x, E2, label='campo E2', linestyle='--')
plt.plot(x, I1,'-', label='I1')
plt.plot(x, I2, label='I2', linestyle='--')
plt.plot(x, I, label='Intensidad Resultante', linewidth=2)
plt.title(f'Interferencia de dos ondas: delta_fase = pi')
plt.xlabel('Posición')
plt.ylabel('Intensidad I; onda E')
plt.legend()
plt.grid(True)
plt.show()
