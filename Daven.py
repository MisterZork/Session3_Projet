
print('code pour trouver la plus petite distance entre tous les distance possibles')

list_des_distances=[5,6,9,500,7,4,80,1]

nb_list=len(list_des_distances)
for i in range (0,nb_list):
    condition = 0
    for j in range (0,nb_list) :
        if list_des_distances[i]>=list_des_distances[j]:
            condition=condition+1
    if condition==1:
        print('la plus petite distance est :',list_des_distances[i],'unités.')