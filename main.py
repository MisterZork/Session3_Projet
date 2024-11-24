# Exercice 9 - Le plus court trajet possible
# Objectif - Créer un algorithme qui est capable de déterminer le chemin le plus court entre 5 points.

import itertools

import numpy as np


def individual_data(nb_pts):
    data = [[0., 0., 0.]]
    for i in range(nb_pts):
        print("-" * 30)
        print(f"Entrez les valeurs (x, y et z) du point {i + 1}")
        x = float(input("X -> "))
        y = float(input("Y -> "))
        z = float(input("Z -> "))
        data.append([x, y, z])
    return data

def multi_data(nb_pts):
    data = [[0., 0., 0.]]
    for i in range(nb_pts):
        print("-" * 30)
        x, y, z = input(f"Entrez les valeurs (x, y, z) du point {i + 1}").split(sep=", ")
        data.append([x, y, z])
    return data

def np_data(file):
    return np.genfromtxt(file, delimiter=",", skip_header=1)

def distance(data, un, deux):
    x1, y1, z1 = data[un][0], data[un][1], data[un][2]
    x2, y2, z2 = data[deux][0], data[deux][1], data[deux][2]
    temp = [(x2 - x1), (y2 - y1), (z2 - z1)]
    return ((temp[0] ** 2) + (temp[1] ** 2) + (temp[2] ** 2)) ** (1/2)


def permutations(nb_pts):
    nombre_points = [_ for _ in range(1, nb_pts + 1)]
    return list(itertools.permutations(nombre_points, nb_pts))
    # TODO - Modifier pour un code propriétaire


def sommes_distances(permutation, data):
    dist = []
    dist_temp = 0.
    for i in range(len(permutation)):
        for j in range(len(permutation[i])):
            dist_temp += distance(data, permutation[i][j], permutation[i][j + 1])
            # TODO - Trouver une meilleure solution pour ordonner les distances temporaires
        dist.append(dist_temp)
        dist_temp = 0.
    return dist



if __name__ == "__main__":
    nombre = int(input("Combien de points voulez-vous calculer (en plus du point 0) : "))
    coords = np.array(individual_data(nombre))
    print(coords)
    print(distance(coords, 1, 2))
    print(sommes_distances(permutations(nombre), coords))
print('daven')