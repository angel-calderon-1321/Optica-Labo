#Interferencia entre dos ondas esfércias sobre uel eje optico, cuyo
#plan de observación es perpendicular al eje óptico.
#Consideramos dos fuentes puntuales S1 y S2 ubicadas en el eje óptico
#ambas distan del plano de observación una distancia R1 y R2 respectivamente.
#y ambas fuentes estan separada una de otra una distancia d.

import numpy as np
import matplotlib.pyplot as plt

def inter(x, y, k, I0, R1, R2, d):
    '''Calcula la intensidad resultante de la interferencia de dos ondas
    esféricas en función de las coordenadas x, y, el número de onda k,
    la intensidad individual I0, y las distancias R1 y R2.
    Tambien utilice la aproximación de fresnel para la distancia
    desde el origen a un punto (x,y,R1) y (x,y,R2).'''
    
    d_fase = k*d*(1-(x**2 + y**2)/(2*R1*R2))  # Distancia desde el origen
    I = 2*I0 * (1 + np.cos(d_fase))
    return I

#Definimos los parámetros
I0 = 1 #intensidad de cada onda. [J/(s*m^2)]
long_onda = 600e-9 #longitud de onda en nm
k = 2 * np.pi / long_onda #número de onda
R1 = 0.1 #distancia de la fuente S1 al plano de observación [m]
R2 = 0.035 #distancia de la fuente S2 al plano de observación [m]
d = R1 - R2 #distancia entre las fuentes S1 y S2 [m]

x_ran = 1e-3  # Rango de x en metros
y_ran = 1e-3  # Rango de y en metros

#Definimos el rango de posiciones x e y
x = np.linspace(-x_ran, x_ran , 500) #en metros va desde -2 mm hasta 2 mm
y = np.linspace(-y_ran,y_ran, 500) #en metros va desde -2 mm hasta 2 mm
X, Y = np.meshgrid(x, y) #Creamos una malla de puntos (x,y)

#Calculamos la intensidad resultante
I = inter(X, Y, k, I0, R1, R2, d)

#Graficamos la intensidad resultante
plt.figure(figsize=(8, 6))
plt.imshow(I, extent=(-1, 1, -1, 1), cmap='viridis', origin='lower')
plt.colorbar(label='Intensidad I (J/(s·m²))')
plt.title('Patrón de interferencia entre dos ondas esféricas')
plt.xlabel('Posición x (mm)')
plt.ylabel('Posición y (mm)')
plt.text(-0.8, -0.8, f'd:{d:.2f}m \n long onda:{long_onda*1e9} nm', fontsize=12, color='white',bbox=dict(boxstyle="round,pad=0.3", facecolor="black", alpha=0.8))
plt.clim(0, 2*I0) #Ajustamos los límites de color
plt.savefig('interferencia_tp2_3b.png', dpi=300) #Guardamos la figura
plt.tight_layout()
plt.show()