# Exercice 9 - Le plus court trajet possible
# Objectif - Créer un algorithme qui est capable de déterminer le chemin le plus court entre 5 points.

import itertools
import numpy as np
from screen import afficher_animation
import tkinter as tk

#------------------Récupération de données---------------------------
def individual_data(nb_pts):
    data = [[0., 0., 0.]]
    for i in range(nb_pts):
        print("-" * 50)
        print(f"Entrez les valeurs (x, y et z) du point {i + 1}")
        x = float(input("X -> "))
        y = float(input("Y -> "))
        z = float(input("Z -> "))
        data.append([x, y, z])
    return data

#---------------------------Calcul de distances et permutations----------------------------------
def distance(data, un, deux):
    x1, y1, z1 = data[un][0], data[un][1], data[un][2]
    x2, y2, z2 = data[deux][0], data[deux][1], data[deux][2]
    temp = [(x2 - x1), (y2 - y1), (z2 - z1)]
    return ((temp[0] ** 2) + (temp[1] ** 2) + (temp[2] ** 2)) ** (1/2)

def permutations_centre(nb_pts):
    nombre_points = [_ for _ in range(1, nb_pts + 1)]
    return list(itertools.permutations(nombre_points, nb_pts))

def sommes_distances_centre(permutation, data):
    dist_somme = []
    dist_temp = 0.
    for i in range(len(permutation)):
        for j in range(len(permutation[i])):
            if j == 0:
                dist_temp += distance(data, 0, permutation[i][j])
                continue
            dist_temp += distance(data, permutation[i][j-1], permutation[i][j])
        dist_somme.append(dist_temp)
        dist_temp = 0.
    return dist_somme

#---------------------------Analyse et ordre--------------------------------------------------
def min_order(dist, permutations):
    min = None
    ordre_list = []
    for arg in dist:
        if min is None or arg <= min:
            min = arg
    for a in range(len(dist)):
        if min == dist[a]:
            ordre_list.append(a)
    return min, ordre_list

#--------------------------Programme principal-------------------------------------------
if __name__ == "__main__":
    nombre_points = int(input("Combien de points voulez-vous calculer (en plus du point 0) : "))
    coords = np.array(individual_data(nombre_points))
    perm = permutations_centre(nombre_points)
    dist_total = np.array(sommes_distances_centre(permutations_centre(nombre_points), coords))
    minimum, id_perm = min_order(dist_total, perm)

    print("-" * 50)
    print(f"La distance la plus courte est : {round(minimum, 3)} unités")
    print("Voici le(s) chemin(s) qui correspond(ent) à cela :")
    for elem in id_perm:
        print(f"P0 -> {" -> ".join([f"P{p}" for p in perm[elem]])}")

    root = tk.Tk()
    root.title("SpaceMap Go v.0.1.0")
    afficher_animation(root, coords, [perm[elem] for elem in id_perm])
    root.mainloop()