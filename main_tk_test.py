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

def sommes_distances(permutation, data, bool_mode):
    dist_somme = []
    dist_temp = 0.
    if bool_mode is True:
        for i in range(len(permutation)):
            for j in range(len(permutation[i]) - 1):
                dist_temp += distance_calc(data, permutation[i][j], permutation[i][j+1])
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

def min_order(distances):
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
    coords = [[0., 0., 0.]]
    for entry_x, entry_y, entry_z in entries_coords:
        x = float(entry_x.get())
        y = float(entry_y.get())
        z = float(entry_z.get())
        coords.append([x, y, z])
    coords = np.array(coords)
    nb_points = len(coords) - 1
    perm = permutations_finder(nb_points, False)
    dist_total = np.array(sommes_distances(perm, coords, False))
    minimum, id_perm = min_order(dist_total)
    result_text.set(f"Distance minimale: {minimum}\nOrdre: {id_perm}")

def ajouter_coords(frame):
    row = len(entries_coords) + 1
    tk.Label(frame, text=f"Point {row} (x, y, z):").grid(row=row, column=0)
    entry_x = tk.Entry(frame)
    entry_y = tk.Entry(frame)
    entry_z = tk.Entry(frame)
    entry_x.grid(row=row, column=1)
    entry_y.grid(row=row, column=2)
    entry_z.grid(row=row, column=3)
    entries_coords.append((entry_x, entry_y, entry_z))

#--------------------------------GUI--------------------------------------
#Coeur du GUI -> Tk, Notebook et Treeview
data = np.zeros((1, 3))
entries_coords = []

main_screen = tk.Tk()
main_screen.title("SpaceMap Go - v. 1.1.0")
main_screen.geometry("800x600")
main_screen.grid_columnconfigure((0, 1), weight=2)
main_screen.grid_rowconfigure(0, weight=1)

decal = ttk.Notebook(main_screen)
decal.grid(row=0, column=0)
data_view = ttk.Treeview(main_screen, columns=("X", "Y", "Z"), show="headings")
data_view.heading("X", text="X")
data_view.heading("Y", text="Y")
data_view.heading("Z", text="Z")
data_view.grid(row=0, column=1, sticky="NSWE")

#Séparation en 2 sections : Mise des points et affichage de screen.py (sous sectionné avec la vraie animation)
frame_input = ttk.LabelFrame(decal, text="Entrée des Points")
frame_input.grid()

frame_animation = ttk.LabelFrame(decal, text="Animation 3D")
frame_animation.grid()

decal.add(frame_input, text="Inputs")
decal.add(frame_animation, text="Affichage")

btn_ajouter_point = ttk.Button(frame_input, text="Ajouter Point", command=ajouter_coords(frame_input))
btn_ajouter_point.grid(row=0, column=0)
btn_calculer = ttk.Button(frame_input, text="Calculer Chemin", command=calculer_chemin)
btn_calculer.grid(row=0, column=1)

result_text = tk.StringVar()
label_result = ttk.Label(frame_animation, textvariable=result_text)
label_result.grid(pady=20)
btn_afficher_animation = ttk.Button(frame_animation, text="Afficher Animation", command=lambda: afficher_animation(frame_animation, entries_coords, permutations_finder(4, False)))
btn_afficher_animation.grid(pady=20)

main_screen.mainloop()