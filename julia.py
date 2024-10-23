import numpy as np

def generate_julia(c=-0.7 + 0.27015j, width=800, height=800, max_iter=100):
    x_min, x_max = -2.0, 2.0
    y_min, y_max = -2.0, 2.0
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    fractal = np.zeros(Z.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + c
        fractal[mask] += 1
    
    return fractal
