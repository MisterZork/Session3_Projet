coords = [[0,0,0]]
while True:
    coords_temp_x = (float(input('Entrez votre valeur en x : ')))
    coords_temp_y = (float(input('Entrez votre valeur en y : ')))
    coords_temp_z = (float(input('Entrez votre valeur en z : ')))
    done = input('Écrivez « terminez » quand vous avez tous vos points : ')
    print('-' * 35)
    if done.lower() == 'terminez':
        break
    coords.append([coords_temp_x, coords_temp_y, coords_temp_z])
print(coords)

coords




