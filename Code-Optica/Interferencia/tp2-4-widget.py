import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def inter(y, k, I0, d, D):
    '''Calcula la intensidad resultante de la interferencia de dos ondas
    esféricas en función de las coordenadas y, el número de onda k,
    la intensidad individual I0, la distancia d entre las fuentes y D
    la distancia del plano de observación al origen.'''
    
    d_fase = k * d * y / D  # Diferencia de fase
    I = 2 * I0 * (1 + np.cos(d_fase))  # Interferencia
    return I

# Configuración de la figura
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

# Parámetros iniciales
I0 = 1
long_onda_inicial = 600e-9  # metros
d_inicial = 0.0002  # metros
D_inicial = 0.8  # metros

# Rango de posiciones
y = np.linspace(-0.01, 0.01, 500)  # metros

# Cálculo inicial
k_inicial = 2 * np.pi / long_onda_inicial
I_inicial = inter(y, k_inicial, I0, d_inicial, D_inicial)

# Gráfico inicial
line, = ax.plot(y * 1000, I_inicial, 'b-', linewidth=2)
ax.set_xlabel('Posición y (mm)')
ax.set_ylabel('Intensidad I (J/(s·m²))')
ax.set_title('Patrón de interferencia entre dos ondas esféricas')
ax.grid(True)

# Crear deslizadores
ax_wavelength = plt.axes([0.2, 0.15, 0.5, 0.03])
ax_d = plt.axes([0.2, 0.10, 0.5, 0.03])
ax_D = plt.axes([0.2, 0.05, 0.5, 0.03])

slider_wavelength = Slider(ax_wavelength, 'λ (nm)', 400, 700, valinit=600)
slider_d = Slider(ax_d, 'd (mm)', 0.1, 1.0, valinit=0.2)
slider_D = Slider(ax_D, 'D (m)', 0.5, 2.0, valinit=0.8)

def update(val):
    # Obtener valores
    wavelength = slider_wavelength.val * 1e-9  # convertir a metros
    d = slider_d.val * 1e-3  # convertir a metros
    D = slider_D.val
    
    # Calcular nuevo patrón
    k = 2 * np.pi / wavelength
    I_new = inter(y, k, I0, d, D)
    
    # Actualizar gráfico
    line.set_ydata(I_new)
    fig.canvas.draw_idle()

# Conectar deslizadores
slider_wavelength.on_changed(update)
slider_d.on_changed(update)
slider_D.on_changed(update)

plt.show()