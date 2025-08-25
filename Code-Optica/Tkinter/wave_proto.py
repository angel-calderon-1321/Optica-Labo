from tkinter import *
import numpy as np

class SinusoidalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sinusoidal Function Viewer")

        # Configura la amplitud y fase iniciales
        self.amplitude = DoubleVar(value=1.0)
        self.phase = DoubleVar(value=0.0)

        # Crear el canvas para la gráfica
        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().pack()

        # Crear los controles (sliders) para ajustar la amplitud y fase
        self.create_controls()

        # Dibujar la función sinusoidal inicial
        self.update_plot()

    def create_controls(self):
        # Control para la amplitud
        amplitude_label = Label(self.root, text="Amplitud:")
        amplitude_label.pack()
        amplitude_slider = Scale(
            self.root, from_=0, to=10, resolution=0.1, orient="horizontal", variable=self.amplitude, command=self.update_plot
        )
        amplitude_slider.pack()

        # Control para la fase
        phase_label = Label(self.root, text="Fase:")
        phase_label.pack()
        phase_slider = Scale(
            self.root, from_=0, to=2 * np.pi, resolution=0.1, orient="horizontal", variable=self.phase, command=self.update_plot
        )
        phase_slider.pack()

    def update_plot(self, *args):
        # Limpiar el canvas
        self.canvas.delete("all")

        # Obtener la amplitud y fase actuales
        amplitude = self.amplitude.get()
        phase = self.phase.get()

        # Dibujar la función sinusoidal
        # Matplotlib Figure
        fig, ax = plt.subplots()
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)
        line, = ax.plot(x, y)

        # Dibujar la línea de la función sinusoidal
        self.canvas.create_line(points, fill="blue", smooth=True)

# Crear la ventana principal
root = Tk()
app = SinusoidalApp(root)

root.mainloop()
