import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

# Configuración de la simulación
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
plt.subplots_adjust(bottom=0.25)

# Parámetros iniciales
t_max = 10  # tiempo total de simulación
dt = 0.01   # paso de tiempo
x = np.linspace(0, 10, 1000)  # posición espacial
t = np.arange(0, t_max, dt)

# Parámetros de las ondas
A1 = 1.0    # amplitud onda 1
A2 = 1.0    # amplitud onda 2
f1 = 1.0    # frecuencia onda 1 (Hz)
f2_coherent = 1.0      # frecuencia onda 2 coherente (igual a f1)
f2_incoherent = 1.1    # frecuencia onda 2 incoherente (diferente)
phi1 = 0.0  # fase inicial onda 1
phi2 = np.pi/3  # fase inicial onda 2 (60 grados de diferencia)

# Funciones para calcular las ondas
def wave1(x, t, f, phi):
    """Onda 1"""
    return A1 * np.sin(2*np.pi*f*t - 2*np.pi*x + phi)

def wave2(x, t, f, phi):
    """Onda 2"""
    return A2 * np.sin(2*np.pi*f*t - 2*np.pi*x + phi)

def interference_pattern(x, t, f1, f2, phi1, phi2):
    """Patrón de interferencia total"""
    w1 = wave1(x, t, f1, phi1)
    w2 = wave2(x, t, f2, phi2)
    return w1 + w2

# Calcular intensidad promedio (coherencia temporal)
def calculate_average_intensity(x, t_array, f1, f2, phi1, phi2):
    """Calcula la intensidad promediada en el tiempo"""
    intensities = []
    for t_val in t_array:
        pattern = interference_pattern(x, t_val, f1, f2, phi1, phi2)
        intensities.append(pattern**2)
    return np.mean(intensities, axis=0)

# Tiempo específico para mostrar ondas instantáneas
t_snapshot = 0

# Calcular patrones
# Caso coherente (mismas frecuencias)
pattern_coherent = interference_pattern(x, t_snapshot, f1, f2_coherent, phi1, phi2)
intensity_coherent_avg = calculate_average_intensity(x, t[:100], f1, f2_coherent, phi1, phi2)

# Caso incoherente (frecuencias diferentes)
pattern_incoherent = interference_pattern(x, t_snapshot, f1, f2_incoherent, phi1, phi2)
intensity_incoherent_avg = calculate_average_intensity(x, t[:100], f1, f2_incoherent, phi1, phi2)

# Plotting
# 1. Ondas individuales coherentes
ax1.plot(x, wave1(x, t_snapshot, f1, phi1), 'b-', label=f'Onda 1 (f={f1} Hz, φ={phi1:.2f})', linewidth=2)
ax1.plot(x, wave2(x, t_snapshot, f2_coherent, phi2), 'r-', label=f'Onda 2 (f={f2_coherent} Hz, φ={phi2:.2f})', linewidth=2)
ax1.plot(x, pattern_coherent, 'k-', label='Interferencia', linewidth=3)
ax1.set_title('CASO COHERENTE: Frecuencias Iguales (f₁ = f₂)')
ax1.set_xlabel('Posición (x)')
ax1.set_ylabel('Amplitud')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-3, 3)

# 2. Intensidad promedio coherente
ax2.plot(x, intensity_coherent_avg, 'g-', linewidth=3)
ax2.set_title('Intensidad Promedio - COHERENTE\n(Patrón de interferencia VISIBLE)')
ax2.set_xlabel('Posición (x)')
ax2.set_ylabel('Intensidad')
ax2.grid(True, alpha=0.3)
ax2.fill_between(x, intensity_coherent_avg, alpha=0.3, color='green')

# 3. Ondas individuales incoherentes
ax3.plot(x, wave1(x, t_snapshot, f1, phi1), 'b-', label=f'Onda 1 (f={f1} Hz, φ={phi1:.2f})', linewidth=2)
ax3.plot(x, wave2(x, t_snapshot, f2_incoherent, phi2), 'r-', label=f'Onda 2 (f={f2_incoherent} Hz, φ={phi2:.2f})', linewidth=2)
ax3.plot(x, pattern_incoherent, 'k-', label='Interferencia', linewidth=3)
ax3.set_title('CASO INCOHERENTE: Frecuencias Diferentes (f₁ ≠ f₂)')
ax3.set_xlabel('Posición (x)')
ax3.set_ylabel('Amplitud')
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_ylim(-3, 3)

# 4. Intensidad promedio incoherente
ax4.plot(x, intensity_incoherent_avg, 'm-', linewidth=3)
ax4.set_title('Intensidad Promedio - INCOHERENTE\n(Patrón de interferencia NO VISIBLE)')
ax4.set_xlabel('Posición (x)')
ax4.set_ylabel('Intensidad')
ax4.grid(True, alpha=0.3)
ax4.fill_between(x, intensity_incoherent_avg, alpha=0.3, color='magenta')

# Agregar sliders para interactividad
ax_phi2 = plt.axes([0.2, 0.1, 0.5, 0.03])
ax_f2_incoh = plt.axes([0.2, 0.05, 0.5, 0.03])

slider_phi2 = Slider(ax_phi2, 'Diferencia de Fase φ₂', 0, 2*np.pi, valinit=phi2, valfmt='%.2f rad')
slider_f2 = Slider(ax_f2_incoh, 'Frecuencia f₂ (incoherente)', 0.5, 2.0, valinit=f2_incoherent, valfmt='%.2f Hz')

def update(val):
    new_phi2 = slider_phi2.val
    new_f2_incoh = slider_f2.val
    
    # Recalcular patrones
    new_pattern_coherent = interference_pattern(x, t_snapshot, f1, f2_coherent, phi1, new_phi2)
    new_intensity_coherent_avg = calculate_average_intensity(x, t[:100], f1, f2_coherent, phi1, new_phi2)
    
    new_pattern_incoherent = interference_pattern(x, t_snapshot, f1, new_f2_incoh, phi1, new_phi2)
    new_intensity_incoherent_avg = calculate_average_intensity(x, t[:100], f1, new_f2_incoh, phi1, new_phi2)
    
    # Actualizar gráficos
    ax1.clear()
    ax1.plot(x, wave1(x, t_snapshot, f1, phi1), 'b-', label=f'Onda 1 (f={f1} Hz, φ={phi1:.2f})', linewidth=2)
    ax1.plot(x, wave2(x, t_snapshot, f2_coherent, new_phi2), 'r-', label=f'Onda 2 (f={f2_coherent} Hz, φ={new_phi2:.2f})', linewidth=2)
    ax1.plot(x, new_pattern_coherent, 'k-', label='Interferencia', linewidth=3)
    ax1.set_title('CASO COHERENTE: Frecuencias Iguales (f₁ = f₂)')
    ax1.set_xlabel('Posición (x)')
    ax1.set_ylabel('Amplitud')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(-3, 3)
    
    ax2.clear()
    ax2.plot(x, new_intensity_coherent_avg, 'g-', linewidth=3)
    ax2.set_title('Intensidad Promedio - COHERENTE\n(Patrón de interferencia VISIBLE)')
    ax2.set_xlabel('Posición (x)')
    ax2.set_ylabel('Intensidad')
    ax2.grid(True, alpha=0.3)
    ax2.fill_between(x, new_intensity_coherent_avg, alpha=0.3, color='green')
    
    ax3.clear()
    ax3.plot(x, wave1(x, t_snapshot, f1, phi1), 'b-', label=f'Onda 1 (f={f1} Hz, φ={phi1:.2f})', linewidth=2)
    ax3.plot(x, wave2(x, t_snapshot, new_f2_incoh, new_phi2), 'r-', label=f'Onda 2 (f={new_f2_incoh:.2f} Hz, φ={new_phi2:.2f})', linewidth=2)
    ax3.plot(x, new_pattern_incoherent, 'k-', label='Interferencia', linewidth=3)
    ax3.set_title('CASO INCOHERENTE: Frecuencias Diferentes (f₁ ≠ f₂)')
    ax3.set_xlabel('Posición (x)')
    ax3.set_ylabel('Amplitud')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim(-3, 3)
    
    ax4.clear()
    ax4.plot(x, new_intensity_incoherent_avg, 'm-', linewidth=3)
    ax4.set_title('Intensidad Promedio - INCOHERENTE\n(Patrón de interferencia NO VISIBLE)')
    ax4.set_xlabel('Posición (x)')
    ax4.set_ylabel('Intensidad')
    ax4.grid(True, alpha=0.3)
    ax4.fill_between(x, new_intensity_incoherent_avg, alpha=0.3, color='magenta')
    
    plt.draw()

slider_phi2.on_changed(update)
slider_f2.on_changed(update)

# Texto explicativo
fig.suptitle('SIMULACIÓN DE COHERENCIA TEMPORAL EN INTERFERENCIA\n' +
            'Izquierda: Frecuencias iguales (coherente) | Derecha: Frecuencias diferentes (incoherente)\n' +
            'Arriba: Ondas instantáneas | Abajo: Intensidad promediada en tiempo', 
            fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

# Imprimir explicación
print("="*80)
print("EXPLICACIÓN DE LA SIMULACIÓN:")
print("="*80)
print()
print("CASO COHERENTE (frecuencias iguales):")
print("- Las ondas mantienen una diferencia de fase constante")
print("- El patrón de interferencia es estable y visible")
print("- La intensidad promedio muestra franjas claras")
print()
print("CASO INCOHERENTE (frecuencias diferentes):")
print("- La diferencia de fase cambia constantemente")
print("- El patrón de interferencia fluctúa rápidamente")
print("- Al promediar en tiempo, las franjas desaparecen")
print("- Solo queda una intensidad uniforme")
print()
print("USO DE LOS SLIDERS:")
print("- Cambia la diferencia de fase φ₂ para ver cómo afecta ambos casos")
print("- Cambia la frecuencia f₂ para ver cómo la incoherencia destruye el patrón")
print("="*80)