#Vamos a esquematixar las franjas de interferencia del TP2-1
#La ineterencia es de dos ondas con igual intensidad, polarización, frecuencia y longitud de onda.
import numpy as np
import matplotlib.pyplot as plt

def inter(x, I0, k, theta_1, theta_2):
    '''Calcula la intensidad resultante de la interferencia de dos ondas
     en función de la posición x, la intensidad individual I0, el número de onda k,
     y los ángulos de incidencia theta_1 y theta_2.'''
    
    I = 4*I0*np.cos(k*(np.sin(theta_1)-np.sin(theta_2))*x/2)**2
    return I

#Definimos los parámetros
I0 = 1 #intensidad de cada onda. [J/(s*m^2)]

long_onda = 600e-9 #longitud de onda en nm
k = 2 * np.pi / long_onda #número de onda

#Ángulos de incidencia
theta_1 = 34 #ángulo de incidencia de la onda 1
theta_2 = 35 #ángulo de incidencia de la onda 2

#Definimos el rango de posiciones x
x = np.linspace(0, 100*long_onda, 1000) #en metros va desde 0 hasta 60 micrometros
#Calculamos la intensidad resultante
I = inter(x, I0, k, np.radians(theta_1),np.radians(theta_2))

#Graficamos la intensidad resultante
plt.figure(figsize=(10, 6))
plt.plot(x*1e6, I, label=f'Interferencia de dos ondas\nθ1={theta_1}°, θ2={theta_2}°')
plt.title('Patrón de interferencia')
plt.xlabel('Posición x (μm)')
plt.ylabel('Intensidad I (J/(s·m²))')
plt.ylim(0, 4*I0)
plt.legend()
plt.grid(True)
plt.savefig('interferencia_tp2_1b.png', dpi=300)
plt.tight_layout()
plt.show()

