#Experimento de young con dos fuentes puntuales S1 y S2.
#Interferencia entre dos ondas esféricas sobre el eje óptico, cuyo
#plano de observación es paralelo al eje óptico. Separado una distancia D del plano.
#Ambas fuentes estan separadas una de otra una distancia d. Con D>>d

import numpy as np
import matplotlib.pyplot as plt

def inter(y, k, I0, d, D):
    '''Calcula la intensidad resultante de la interferencia de dos ondas
    esféricas en función de las coordenadas x, el número de onda k,
    la intensidad individual I0, la distancia d entre las fuentes y D
    la distancia del plano de observación al origen.'''
    
    d_fase = k * d * y / D  # Distancia desde el origen
    I = 2 * I0 * (1 + np.cos(d_fase))  # Interferencia
    return I

#Definimos los parámetros
I0 = 1 #intensidad de cada onda. [J/(s*m^2)]
long_onda = 600e-9 #longitud de onda en nm
k = 2 * np.pi / long_onda #número de onda
D = 0.8 #distancia del plano de observación al origen [m]
d = 0.0002 #distancia entre las fuentes S1 y S2 [m]

#Definimos el rango de posiciones x
y = np.linspace(-0.01, 0.01, 500) #en metros va desde -10 mm hasta 10 mm

#Calculamos la intensidad resultante
I = inter(y, k, I0, d, D)

#Graficamos la intensidad resultante
plt.figure(figsize=(10, 6))
plt.plot(y , I, label=f'Interferencia de dos ondas\n d={d*1e3} mm, D={D} m')
plt.title('Patrón de interferencia entre dos ondas esféricas')
plt.xlabel('Posición x (mm)')
plt.ylabel('Intensidad I (J/(s·m²))')
#plt.ylim(0, 2 * I0)
plt.legend()
plt.grid(True)
plt.savefig('interferencia_tp2_4.png', dpi=300) #Guardamos la figura
plt.tight_layout()
plt.show()