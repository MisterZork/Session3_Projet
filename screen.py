import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use("TkAgg")
plt.style.use('_mpl-gallery')

#Mise en place de valeurs test (voir le départ de ce code pour comprendre [ligne 55])
test_coords = [[0., 0., 0.],
               [1., 1., 1.],
               [2., 2., 2.],
               [2., 0., 1.],
               [1., 1., 0.]]

test_perm = [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3),
             (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1),
             (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

def afficher_animation(screen, coords, perm_data):
    """Cette fonction met dans un écran tkinter un graphique 3D selon les coordonnées et les permutations à afficher"""
    fig = plt.Figure()
    ax = fig.add_subplot(111, autoscale_on=True, projection='3d') #Setup des settings de dimensions sur matplotlib

    def update(num):
        """Cette fonction change les coordonnées affichées selon le cycle du frame et des permutations données"""
        ax.clear()
        perm = perm_data[num]   #Changement des coordonnées selon la permutation choisie
        xs = [coords[0][0]] + [coords[i][0] for i in perm]
        ys = [coords[0][1]] + [coords[i][1] for i in perm]
        zs = [coords[0][2]] + [coords[i][2] for i in perm]

        #Affichage des points avec des noms spécifiques (et d'une autre couleur pour le point 0)
        ax.scatter(0, 0, 0, color='red', s=100)
        for i, (xa, ya, za) in enumerate(coords):
            ax.text(xa, ya, za, f"P{i}", color='red')

        #Affichage correct des axes et du titre du graphique
        ax.plot(xs, ys, zs, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5)
        ax.set_xlabel('X', fontsize=12, color='red')
        ax.set_ylabel('Y', fontsize=12, color='green')
        ax.set_zlabel('Z', fontsize=12, color='blue')
        ax.set_title('Animation 3D avec Rotation', fontsize=15, color='purple')

    #Affichage dans le GUI Tkinter
    canvas = FigureCanvasTkAgg(fig, master=screen)
    ani = animation.FuncAnimation(fig, update, frames=len(perm_data), interval=1000, repeat=True, blit=False)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="NSWE")
    screen.grid_columnconfigure(0, weight=1)
    screen.grid_rowconfigure(0, weight=1)
    screen.ani = ani

#Ceci est un test pour debug le code dans screen.py
if __name__ == "__main__":
    root = tk.Tk()
    afficher_animation(root, test_coords, test_perm)
    root.mainloop()