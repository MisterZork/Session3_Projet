import numpy as np

coords = [[0, 0, 0]]
boo = input("Est-ce que vos valeurs se trouvent dans data.csv ? (O/N) \n->")
if boo.lower() == "o":
    coords = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
else:
    for i in range(4):
        coords_temp = [int(input(f"Entrez les coordonnées x, y et z du point {i + 1} : "))]
        coords.append(coords_temp)
        temp = coords[i+1]

    # Slice chaque string dans une boucle, où on vérifie l'index où se trouve la virgule
print(coords)