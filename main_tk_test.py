import tkinter as tk
from tkinter import ttk
from screen import afficher_animation
import numpy as np
import itertools

#------------------------Fonctions de calculs----------------------------------
def distance_calc(data, un, deux):
    x1, y1, z1 = data[un][0], data[un][1], data[un][2]
    x2, y2, z2 = data[deux][0], data[deux][1], data[deux][2]
    temp = [(x2 - x1), (y2 - y1), (z2 - z1)]
    return ((temp[0] ** 2) + (temp[1] ** 2) + (temp[2] ** 2)) ** (1/2)

def permutations_finder(nb_pts, bool_mode):
    if bool_mode is True:
        nombre_points = [_ for _ in range(0, nb_pts + 1)]
    else:
        nombre_points = [_ for _ in range(1, nb_pts + 1)]
    return list(itertools.permutations(nombre_points, nb_pts))

def sommes_distances_centre(permutation, data, bool_mode):
    dist_somme = []
    dist_temp = 0.
    if bool_mode is True:
        for i in range(len(permutation)):
            for j in range(len(permutation[i]) - 1):
                dist_temp += distance_calc(data. permutation)
    else:
        for i in range(len(permutation)):
            for j in range(len(permutation[i])):
                if j == 0:
                    dist_temp += distance_calc(data, 0, permutation[i][j])
                    continue
                dist_temp += distance_calc(data, permutation[i][j - 1], permutation[i][j])
            dist_somme.append(dist_temp)
            dist_temp = 0.
        return dist_somme

def min_order(distances, permutation):
    min = None
    ordre_list = []
    for arg in distances:
        if min is None or arg <= min:
            min = arg
    for a in range(len(distances)):
        if min == distances[a]:
            ordre_list.append(a)
    return min, ordre_list

#------------------------------Fonctions de GUI---------------------------
def calculer_chemin():
    nb_points = int(entry_nb_points.get())
    coords = [[0., 0., 0.]]
    for i in range(nb_points):
        x = float(entries_coords[i][0].get())
        y = float(entries_coords[i][1].get())
        z = float(entries_coords[i][2].get())
        coords.append([x, y, z])
    coords = np.array(coords)
    perm = permutations_finder(nb_points)
    dist_total = np.array(sommes_distances_centre(perm, coords))
    minimum, id_perm = min_order(dist_total, perm)
    result_text.set(f"Distance minimale: {minimum}\nOrdre: {id_perm}")

def ajouter_coords(nb, data_instant):
    for i in range(nb):
        data_view.insert("", tk.END, values=data_instant)


#--------------------------------GUI--------------------------------------
#Coeur du GUI -> Tk, Notebook et Treeview
data = np.zeros((1, 3))

main_screen = tk.Tk()
main_screen.title("SpaceMap Go - v. 1.1.0")
main_screen.geometry("800x600")
decal = ttk.Notebook(main_screen)
decal.pack(expand=True, fill="both", anchor="w")
data_view = ttk.Treeview(main_screen, columns=data, show="tree headings")
data_view.pack(expand=True, fill="both", anchor="e")
ajouter_coords(0, data)


#Séparation en 2 sections : Mise des points et affichage de screen.py (sous sectionné avec la vraie animation)
frame_input = ttk.LabelFrame(decal, text="Entrée des Points")
frame_input.pack(pady=20, padx=20, fill=tk.BOTH, expand=True, anchor="nw")
decal.add(frame_input, text="Inputs")
frame_animation = ttk.LabelFrame(decal, text="Animation 3D")
frame_animation.pack(pady=20, padx=20, fill=tk.BOTH, expand=True, anchor="ne")
decal.add(frame_animation, text="Affichage")
animate = ttk.LabelFrame(frame_animation, text="Affichage 3D")

tk.Label(frame_input, text="Nombre de points:").grid(row=0, column=0)
entry_nb_points = ttk.Entry(frame_input)
entry_nb_points.grid(row=0, column=1)
btn_calculer = ttk.Button(frame_input, text="Calculer Chemin", command=calculer_chemin)
btn_calculer.grid(row=1, column=1)

result_text = tk.StringVar()
label_result = ttk.Label(frame_animation, textvariable=result_text)
label_result.grid(pady=20)
btn_afficher_animation = ttk.Button(frame_animation, text="Afficher Animation",command=lambda: afficher_animation(frame_animation, entries_coords, permutations_finder(4, False)))
btn_afficher_animation.grid(pady=20)

entries_coords = []
def call_points(nb):
    for i in range(5):  # Limite à 5 points pour cet exemple
        tk.Label(frame_input, text=f"Point {i+1} (x, y, z):").grid(row=i, column=0)
        entry_x = tk.Entry(frame_input)
        entry_y = tk.Entry(frame_input)
        entry_z = tk.Entry(frame_input)
        entry_x.grid(row=i, column=1)
        entry_y.grid(row=i, column=2)
        entry_z.grid(row=i, column=3)









main_screen.mainloop()
#TODO - Réorganiser le code de manière ordonnée (en 2 sections -> Class de calculs et GUI)

#TODO - Régler la manière dont on récupère les valeurs des points (meilleur de faire un bouton pour ajouter des
# coordonnées et un bouton qui reset un ttk.Treeview

#TODO - Quand on fait l'appel de afficher_animation, on a soit un bouton qui fait automatiquement un cycle (et affiche
# d'une autre couleur le ou les chemins les plus courtes) ou on a 3 boutons (Flèche avant et arrière, qui incrémente
# frame_animation, ainsi qu'un bouton [chemin le plus court])

#TODO - Clear le widget qui gère