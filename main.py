# Exercice 9 - Le plus court trajet possible
# Objectif - Créer un algorithme qui est capable de déterminer le chemin le plus court entre 5 points.

import numpy as np

#Algorithme pour les permutations entre 2 points

def distance(data, un, deux):
    temp = [(data[deux][0]-data[un][0]), (data[deux][1]-data[un][1]), (data[deux][2]-data[un][2])]
    return ((temp[1] ** 2) + (temp[1] ** 2) + (temp[1] ** 2)) ** (1/2)

if __name__ == "__main__":
    coords = [[0, 0, 0]]
    while True:
        coords_temp_x = (float(input('Entrez votre valeur en x : ')))
        coords_temp_y = (float(input('Entrez votre valeur en y : ')))
        coords_temp_z = (float(input('Entrez votre valeur en z : ')))
        done = input('Écrivez « terminez » quand vous avez tous vos points : ')
        print('-' * 35)
        coords.append([coords_temp_x, coords_temp_y, coords_temp_z])
        if done.lower() == 'terminez':
            break
    #data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
    print(distance(coords, 1, 2))