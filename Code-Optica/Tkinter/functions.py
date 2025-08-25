def update_plot(amplitude_sin, phase_sin, amplitude_cos, phase_cos):
    x = np.linspace(0, 2 * np.pi, 100)
    
    # Actualizar las dos curvas (seno y coseno) con sus respectivos parámetros
    y_sin = amplitude_sin * np.sin(x + phase_sin)
    y_cos = amplitude_cos * np.cos(x + phase_cos)
    
    line_sin.set_ydata(y_sin)
    line_cos.set_ydata(y_cos)
    
    canvas.draw()

def on_amplitude_sin_change(val):
    amplitude_sin = float(val)
    update_plot(amplitude_sin, phase_sin_scale.get(), amplitude_cos_scale.get(), phase_cos_scale.get())

def on_phase_sin_change(val):
    phase_sin = float(val)
    update_plot(amplitude_sin_scale.get(), phase_sin, amplitude_cos_scale.get(), phase_cos_scale.get())

def on_amplitude_cos_change(val):
    amplitude_cos = float(val)
    update_plot(amplitude_sin_scale.get(), phase_sin_scale.get(), amplitude_cos, phase_cos_scale.get())

def on_phase_cos_change(val):
    phase_cos = float(val)
    update_plot(amplitude_sin_scale.get(), phase_sin_scale.get(), amplitude_cos_scale.get(), phase_cos)