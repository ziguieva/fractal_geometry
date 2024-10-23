import matplotlib.pyplot as plt

def koch_curve(ax, p1, p2, depth):
    if depth == 0:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b')
    else:
        delta_x = (p2[0] - p1[0]) / 3
        delta_y = (p2[1] - p1[1]) / 3
        p3 = [p1[0] + delta_x, p1[1] + delta_y]
        p5 = [p1[0] + 2 * delta_x, p1[1] + 2 * delta_y]
        p4 = [
            (p3[0] + p5[0]) / 2 - np.sqrt(3) * (p5[1] - p3[1]) / 6,
            (p3[1] + p5[1]) / 2 + np.sqrt(3) * (p5[0] - p3[0]) / 6
        ]
        koch_curve(ax, p1, p3, depth - 1)
        koch_curve(ax, p3, p4, depth - 1)
        koch_curve(ax, p4, p5, depth - 1)
        koch_curve(ax, p5, p2, depth - 1)

def generate_koch(depth=4):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()
    
    p1 = [0, 0]
    p2 = [1, 0]
    
    koch_curve(ax, p1, p2, depth)
    
    plt.show()
