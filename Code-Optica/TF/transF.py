import numpy as np
import matplotlib.pyplot as plt

# ==========================
# 1) SERIE DE FOURIER
# ==========================

# Definimos una onda cuadrada periódica
T = 2*np.pi       # periodo fundamental
t = np.linspace(-2*T, 2*T, 1000)

# Onda cuadrada ideal: 1 en (0,pi), -1 en (pi,2pi)
square_wave = np.sign(np.sin(t))

# Aproximación con serie de Fourier (N armónicos)
N = 15
approx = np.zeros_like(t)
for k in range(1, N+1, 2):  # solo armónicos impares
    approx += (4/np.pi) * (1/k) * np.sin(k*t)

# ==========================
# 2) TRANSFORMADA DE FOURIER
# ==========================

# Definimos una señal no periódica: pulso gaussiano
t2 = np.linspace(-10, 10, 2000)
gaussian = np.exp(-t2**2)

# Transformada de Fourier con numpy
freqs = np.fft.fftfreq(len(t2), d=(t2[1]-t2[0]))
spectrum = np.fft.fft(gaussian)

# ==========================
# GRÁFICOS
# ==========================

plt.figure(figsize=(12,8))

# Serie de Fourier
plt.subplot(2,2,1)
plt.plot(t, square_wave, label="Onda cuadrada ideal")
plt.title("Función periódica (onda cuadrada)")
plt.grid(); plt.legend()

plt.subplot(2,2,2)
plt.plot(t, approx, 'r', label=f"Aprox. con {N} armónicos")
plt.title("Serie de Fourier (armónicos discretos)")
plt.grid(); plt.legend()

# Transformada de Fourier
plt.subplot(2,2,3)
plt.plot(t2, gaussian, label="Pulso gaussiano")
plt.title("Función no periódica (pulso)")
plt.grid(); plt.legend()

plt.subplot(2,2,4)
plt.plot(np.fft.fftshift(freqs), np.abs(np.fft.fftshift(spectrum)), 'm')
plt.title("Transformada de Fourier (espectro continuo)")
plt.xlabel("Frecuencia"); plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()
plt.show()