import time

def factorial_recursive(n: int) -> int:
    if n < 0 or not n.is_integer():
        raise ValueError('n should be a positive whole number')
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

def factorial_forloop(n: int) -> int:
    result = 1
    for i in range(n):
        result *= n - i
    return result

time1 = time.time()

for i in range(998):
    factorial_recursive(i)

time2 = time.time()

for i in range(998):
    factorial_forloop(i)

time3 = time.time()

print(f"Recursif: {time2-time1} s")
print(f"For-loop: {time3-time2} s")


# print( f'{factorial_recursive(998):,}' )
# print( f'{factorial_forloop(1100):,}' )
