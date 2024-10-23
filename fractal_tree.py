import matplotlib.pyplot as plt
import numpy as np

def fractal_tree(ax, x, y, angle, depth, length):
    if depth > 0:
        x2 = x + length * np.cos(angle)
        y2 = y + length * np.sin(angle)
        ax.plot([x, x2], [y, y2], 'b')
        fractal_tree(ax, x2, y2, angle - np.pi / 6, depth - 1, length * 0.7)
        fractal_tree(ax, x2, y2, angle + np.pi / 6, depth - 1, length * 0.7)

def generate_tree(depth=6):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()
    
    fractal_tree(ax, 0.5, 0, np.pi / 2, depth, 0.3)
    
    plt.show()
