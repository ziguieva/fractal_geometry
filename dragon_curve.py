import matplotlib.pyplot as plt

def generate_dragon(iterations=10):
    x, y = [0], [0]
    for i in range(iterations):
        new_x, new_y = [], []
        for j in range(len(x) - 1):
            mid_x = (x[j] + x[j+1]) / 2
            mid_y = (y[j] + y[j+1]) / 2
            new_x.extend([x[j], mid_x, x[j+1]])
            new_y.extend([y[j], mid_y, y[j+1]])
        x, y = new_x, new_y
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_aspect('equal')
    plt.show()
