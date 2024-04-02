import random
import time


def trier(liste):
    if len(liste) <= 1:
        return liste.copy()
    milieu = len(liste) // 2
    tri1 = trier( liste[:milieu] )
    tri2 = trier( liste[milieu:] )
    return fusion(tri1, tri2)

def fusion(liste1, liste2):
    resultat = []
    i = j = 0

    while i < len(liste1) and j < len(liste2):
        if liste1[i] < liste2[j]:
            resultat.append(liste1[i])
            i += 1
        else:
            resultat.append(liste2[j])
            j += 1
    
    while i < len(liste1):
        resultat.append(liste1[i])
        i += 1
    
    while j < len(liste2):
        resultat.append(liste2[j])
        j += 1
    
    return resultat

def sort_forloop(array: list) -> list:
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped:
            return array
    return array

my_list = [random.random() for _ in range(10000)]

time1 = time.time()

for i in range(1):
    trier(my_list)

time2 = time.time()

for i in range(1):
    sort_forloop(my_list)

time3 = time.time()

print(f"Recursif: {time2-time1} s")
print(f"For-loop: {time3-time2} s")

# my_list = [9, 3, 1, 7]
# print( trier(my_list) )
# print( sort_forloop(my_list) )