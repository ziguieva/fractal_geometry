import numpy as np

def generate_mandelbrot(width=800, height=800, max_iter=100):
    x_min, x_max = -2.5, 1.5
    y_min, y_max = -2.0, 2.0
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros(C.shape, dtype=complex)
    fractal = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + C[mask]
        fractal[mask] += 1
    
    return fractal
