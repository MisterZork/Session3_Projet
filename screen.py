import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use("TkAgg")
plt.style.use('_mpl-gallery')

coordinates = [[0., 0., 0.],
                [1., 1., 1.],
                [2., 2., 2.],
                [2., 0., 1.],
                [1., 1., 0.]]

perm = [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3),
        (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1),
        (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

def afficher_animation(screen, coordinates, perm_data):
    fig = plt.Figure()
    ax = fig.add_subplot(111, autoscale_on=True, projection='3d')

    def update(num):
        ax.clear()
        perm = perm_data[num]
        xs = [coordinates[0][0]] + [coordinates[i][0] for i in perm]
        ys = [coordinates[0][1]] + [coordinates[i][1] for i in perm]
        zs = [coordinates[0][2]] + [coordinates[i][2] for i in perm]
        ax.scatter(0, 0, 0, color='red', s=100)
        for i, (xa, ya, za) in enumerate(coordinates):
            ax.text(xa, ya, za, f"P{i}", color='red')
        ax.plot(xs, ys, zs, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5)
        ax.set_xlabel('X', fontsize=12, color='red')
        ax.set_ylabel('Y', fontsize=12, color='green')
        ax.set_zlabel('Z', fontsize=12, color='blue')
        ax.set_title('Animation 3D avec Rotation', fontsize=15, color='purple')
        ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

    canvas = FigureCanvasTkAgg(fig, master=screen)

    ani = animation.FuncAnimation(fig, update, frames=len(perm_data), interval=1000, repeat=True, blit=False)
    #canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="NSWE")
    screen.grid_columnconfigure(0, weight=1)
    screen.grid_rowconfigure(0, weight=1)
    screen.ani = ani

if __name__ == "__main__":
    root = tk.Tk()
    afficher_animation(root, coordinates, perm)
    root.mainloop()