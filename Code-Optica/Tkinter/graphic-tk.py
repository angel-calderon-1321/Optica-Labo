import tkinter as tk
from tkinter import Scale
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_plot(amplitude, phase):
    x = np.linspace(0, 2 * np.pi, 100)
    y = amplitude * np.sin(x + phase)
    line1.set_ydata(y)
    canvas.draw()

def on_amplitude_change(val):
    amplitude = float(val)
    update_plot(amplitude, phase_scale.get())

def on_phase_change(val):
    phase = float(val)
    update_plot(amplitude_scale.get(), phase)

root = tk.Tk()
root.title("Sinusoidal Plotter")

# Matplotlib Figure
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
y1 = np.cos(x)
line1, = ax.plot(x, y)
#line2, = ax.plot(x,y1)  
ax.grid()


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Amplitude Scale
amplitude_scale = Scale(root, from_=0, to=10, resolution=0.1, orient='horizontal', label='Amplitud', command=on_amplitude_change)
amplitude_scale.set(1)
amplitude_scale.pack()

# Phase Scale
phase_scale = Scale(root, from_=0, to=2 * np.pi, resolution=0.1, orient='horizontal', label='Fase', command=on_phase_change)
phase_scale.set(0)
phase_scale.pack()

root.mainloop()
