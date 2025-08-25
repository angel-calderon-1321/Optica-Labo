def step(x): #función escalon
    return  np.heaviside(x,1)

def rect(x, width = 0.5): #función rectangulo
    return  np.where(np.abs(x) <= width, 1, 0)  