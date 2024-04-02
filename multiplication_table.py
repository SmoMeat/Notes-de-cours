from prettytable import PrettyTable

multiplication_table = PrettyTable()

def test(x):
    global n
    n = 10 + x

test(3)

del n

for i in range(1, 13):
    multiplication_table.add_row([i, 8 * i])

print(multiplication_table)