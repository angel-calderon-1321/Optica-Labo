import tkinter as tk
from tkinter import Scale
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_plot(amplitude1, phase1, amplitude2, phase2):
    x = np.linspace(0, 2 * np.pi, 100)
    
    # Actualizar las dos curvas (seno y coseno) con sus respectivos parámetros
    u1 = amplitude1 * np.cos(x + phase1)
    u2 = amplitude2 * np.cos(x + phase2)

    I1 = u1**2
    I2 = u2**2

    I = I1+I2+2*np.sqrt(I1*I2)*np.cos(phase1-phase2)

    line_u1.set_ydata(I1)
    line_u2.set_ydata(I2)
    line_I.set_ydata(I)
    
    canvas.draw()

def on_amplitude1_change(val):
    amplitude1 = float(val)
    update_plot(amplitude1, phase1_scale.get(), amplitude2_scale.get(), phase2_scale.get())

def on_phase1_change(val):
    phase1 = float(val)
    update_plot(amplitude1_scale.get(), phase1, amplitude2_scale.get(), phase2_scale.get())

def on_amplitude2_change(val):
    amplitude2 = float(val)
    update_plot(amplitude1_scale.get(), phase1_scale.get(), amplitude2, phase2_scale.get())

def on_phase2_change(val):
    phase2 = float(val)
    update_plot(amplitude1_scale.get(), phase1_scale.get(), amplitude2_scale.get(), phase2)

root = tk.Tk()
root.title("Sinusoidal y Cosenoidal Plotter Independiente")

# Figura de Matplotlib
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
u1 = np.sin(x)
u2 = np.cos(x)

I1 = u1**2
I2 = u2**2
I=I1+I2

line_u1, = ax.plot(x, I1, label="Wave u1")
line_u2, = ax.plot(x, I2, label="Wave u2")
line_I, = ax.plot(x,I, label="Intensity")

ax.set_ylim(-4,4)
ax.grid()
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=2)  # Colocar la gráfica arriba

# Escalas para la amplitud y fase del seno (lado izquierdo)
amplitude1_scale = Scale(root, from_=0, to=5, resolution=0.1, orient='horizontal', label='Amplitud u1', command=on_amplitude1_change)

amplitude1_scale.set(1)
amplitude1_scale.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

phase1_scale = Scale(root, from_=0, to=2 * np.pi, resolution=0.1, orient='horizontal', label='phase u1', command=on_phase1_change)

phase1_scale.set(0)
phase1_scale.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

# Escalas para la amplitud y fase del coseno (lado derecho)
amplitude2_scale = Scale(root, from_=0, to=5, resolution=0.1, orient='horizontal', label='Amplitud u2', command=on_amplitude2_change)

amplitude2_scale.set(1)
amplitude2_scale.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

phase2_scale = Scale(root, from_=0, to=2 * np.pi, resolution=0.1, orient='horizontal', label='phase u2', command=on_phase2_change)

phase2_scale.set(0)
phase2_scale.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

root.mainloop()
