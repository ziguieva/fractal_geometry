import matplotlib.pyplot as plt

def generate_sierpinski(depth=5):
    def sierpinski(ax, p1, p2, p3, depth):
        if depth == 0:
            ax.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'b')
        else:
            mid1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            mid2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
            mid3 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)
            sierpinski(ax, p1, mid1, mid3, depth - 1)
            sierpinski(ax, mid1, p2, mid2, depth - 1)
            sierpinski(ax, mid3, mid2, p3, depth - 1)
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()
    
    p1 = [0, 0]
    p2 = [1, 0]
    p3 = [0.5, np.sqrt(3) / 2]
    
    sierpinski(ax, p1, p2, p3, depth)
    
    plt.show()
