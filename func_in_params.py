
def addition(a, *, b):
    print(f'a={a} et b={b}')
    return a + b

print(
    addition(2, b=3)
)
x = map(addition, ['1', '2', '3'], ['1', '2'])

for y in x:
    print(y)