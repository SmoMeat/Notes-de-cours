import random

##############
# EXERCICE 1 #
##############

# lancer = 0
# pile = 0
# while pile < 5000:
#     if random.random() < 0.5:
#         pile += 1
#     lancer += 1

# print(lancer)

##############
# EXERCICE 2 #
##############
# n = 4
# odd_numbers = []
# for i in range(n):
#     odd_numbers.append(2*i + 1)

# print(sum(odd_numbers))

##############
# EXERCICE 3 #
##############

# number = 0
# while number <= 0 :
#     number = int(input('Entrez un nombre positif: '))

##############
# EXERCICE 4 #
##############

# positive_numbers = []
# number = 0

# while number != None:
#     if int(number) > 0:
#         positive_numbers.append(int(number))
#     number = prompt('Entrez un' + str(len(positive_numbers)+1) + 'nombre positif: ')

# print(sum(positive_numbers))

##############
# EXERCICE 5 #
##############

# positive_numbers = []
# number = 0

# while number != None:
#     if int(number) > 0:
#         positive_numbers.append(int(number))
#     number = prompt('Entrez un nombre positif: ')

# print('Min:', min(positive_numbers), 'Max:', max(positive_numbers),
#       'Average:', sum(positive_numbers)/len(positive_numbers))

##############
# EXERCICE 6 #
##############

# n = 20
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i, 'est un diviseur de', n)

##############
# EXERCICE 7 #
##############

# 2,3,5,7,11,13,17,19,23,29,31

# i = 2
# while i <= 31:
#     print(i)
#     i += 1 + (i>2) + 2*(i%6==1) + 4*(i==23)




##############
# EXERCICE 1 #
##############

# def pile_ou_face():
#     """
#     Returns: True si c'est pile et False si c'est face
#     """
#     if random.random() < 0.5:
#         return True
#     return False

##############
# EXERCICE 2 #
##############

# def lancer_des():
#     """Retourne le résultat d'un lancer de dés à 6 faces."""
#     return random.randint(1, 6)

##############
# EXERCICE 3 #
##############

# def evenement_aleatoire(num_of_outcome: int) -> int:
#     return random.randint(1, num_of_outcome)

##############
# EXERCICE 4 #
##############

# def lancer_n_des(num_of_dices) -> int:
#     sum = 0
#     for i in range(1, num_of_dices + 1):
#         sum += evenement_aleatoire(6)
#     return sum

# def lancer_2_des() -> int:
#     return lancer_n_des(2)

##############
# EXERCICE 5 #
##############

# def roulette():
#     return evenement_aleatoire(37)

##############
# EXERCICE 6 #
##############

# def jour_de_la_semaine(year, month, day) -> int:
#     return (23*month//9 + (year*12+month-3)//12 + (month+9)//12*4 +
#             (year*12+month-3)//12//4 - (year*12+month-3)//12//100 +
#             (year*12+month-3)//12//400 + day + 5) % 7 + 1

# def test_jour_de_la_semaine() -> None:
#     assert jour_de_la_semaine(2024, 2, 7) == 4
#     assert jour_de_la_semaine(2023, 11, 5) == 1
#     assert jour_de_la_semaine(1993, 6, 18) == 6

##############
# EXERCICE 7 #
##############

# def farenheit_to_celcius(temp):
#     return (temp - 32) * 5/9

# def celcius_to_farenheit(temp):
#     return (temp * 9/5) + 32

# def test_temp_conversion():
#     assert farenheit_to_celcius(32) == 0
#     assert celcius_to_farenheit(0) == 32
#     assert celcius_to_farenheit(100) == 212
