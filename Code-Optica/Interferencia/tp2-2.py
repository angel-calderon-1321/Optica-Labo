#Interferencia entre una onda plana y una onda esferica
#Consideramos una fuente puntual S localizada en el origen de un sistema
#coordenado emitiendo ondas esféricas que interfiere con una onda
#plana de igual frecuencia que se propaga a lo largo del eje z. Se
#ubica una película fotosensible en un plano (x0-y0) perpendicular al
#eje z que se encuentra a una distancia z0=D del origen

import numpy as np
import matplotlib.pyplot as plt

def inter(x,y,k,I0,z0):
    '''Calcula la intensidad resultante de la interferencia de una onda
    plana y una onda esférica en función de las coordenadas x, y, el número
    de onda k, la intensidad individual I0 y la distancia z0.
    Aqui utilizo la aproximación de fresnel para la distancia desde
    el origen a un punto (x,y,z0)'''
    
    d_fase = k/(2*z0)*(x**2+y**2) # Distancia desde el origen
    I = 2*I0 * (1 + np.cos(d_fase))  # Interferencia
    return I

#Definimos los parámetros
I0 = 1 #intensidad de cada onda. [J/(s*m^2)]
long_onda = 600e-9 #longitud de onda en nm
k = 2 * np.pi / long_onda #número de onda
z0 = 0.1 #distancia del plano fotosensible al origen [m]

#Definimos el rango de posiciones x e y
x = np.linspace(-0.002,0.002, 500) #en metros va desde -1 cm hasta 1 cm
y = np.linspace(-0.002, 0.002, 500) #en metros va desde -1 cm hasta 1 cm
X, Y = np.meshgrid(x, y) #Creamos una malla de puntos (x,y)

#Calculamos la intensidad resultante
I = inter(X, Y, k, I0, z0)
#Graficamos la intensidad resultante
plt.figure(figsize=(8, 6))
plt.imshow(I, extent=(-1, 1, -1, 1), cmap='viridis', origin='lower')
plt.colorbar(label='Intensidad I (J/(s·m²))')
plt.title('Patrón de interferencia entre onda plana y onda esférica')
plt.xlabel('Posición x (mm)')
plt.ylabel('Posición y (mm)')
plt.clim(0, 2*I0) #Ajustamos los límites de color
plt.savefig('interferencia_tp2_2.png', dpi=300) #Guardamos la figura
plt.tight_layout()
plt.show()