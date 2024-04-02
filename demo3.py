##############
# EXERCICE 1 #
##############

# Rep: les 4

##############
# EXERCICE 2 #
##############

# Rep: le 3e

##############
# EXERCICE 3 #
##############

# print("""
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# """)
# print(("x" * 40 + "\n") * 5)

##############
# EXERCICE 4 #
##############

# rep: 5)

##############
# EXERCICE 5 #
##############

# x = 6
# y = 5
# 1)
# print('ok') if (x >= 10 and x <= 20) else None
# 2)
# print('ok') if (x > 0 and x < 100) and (y > -x and y < x) else None
# 3)
# print('ok') if (x > 0 and x < 100) and not x in [50, 55] else None
# 4)
# print('ok') if (x % 10 == 0) else None
# 5)
# print('ok') if (y == 0) or (x % y == 0) else None
# 6)
# print('ok') if not x in [1, 3, 5, 7, 9] else None

##############
# EXERCICE 6 #
##############

# first_number = int(input('Entrez un premier nombre: '))
# second_number = int(input('Entrez un deuxieme nombre: '))

# if first_number < 0 or second_number < 0:
#     print('erreur')
# else:
#     if first_number % second_number == 0 and second_number != 1:
#         print(f'{first_number} et {second_number} sont des mutiples et ont comme facteur commun {first_number // second_number}')
#     elif second_number % first_number == 0 and first_number != 1:
#         print(f'{first_number} et {second_number} sont des mutiples et ont comme facteur commun {second_number // first_number}')
# ** OU UNE AUTRE FACON :
# else:
#     my_max = max(first_number, second_number)
#     my_min = min(first_number, second_number)
#     if (my_max % my_min == 0):
#         print(f'{my_max} et {my_min} sont des mutiples et ont comme facteur commun {my_max // my_min}')

##############
# EXERCICE 7 #
##############

# n = 10
# while n >= 1:
#     print(n)
#     n -= 1

##############
# EXERCICE 8 #
##############

# n = 1
# while n <= 10:
#     print(n**2)
#     n += 1

##############
# EXERCICE 9 #
##############

N = 81
i = 1

while i*i <= N:
    print(i)
    i += 1

###############
# EXERCICE 10 #
###############

# sum = 0
# i = 1

# while i <= 12367:
#     sum += 1/i
#     i += 1

# print(sum)

###############
# EXERCICE 11 #
###############

# sum = 0
# i = 1

# while sum < 10:
#     print(sum, i)
#     sum += 1/i
#     i += 1

# print(i)

###############
# EXERCICE 12 #
###############

# n = 27
# suite = [n]

# while True:
#     last_number = suite[-1]
#     if last_number == 1: break

#     if last_number % 2 == 0:
#         suite.append(last_number / 2)
#     else:
#         suite.append(last_number * 3 + 1)

# print(suite)







