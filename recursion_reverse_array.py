import time

def reverse_recursion(array: list) -> list:
    n = len(array)
    
    if n <= 1:
        return array.copy()
    
    print(array[n//2:], array[:n//2])
    
    return reverse_recursion(array[n//2:]) + reverse_recursion(array[:n//2])

def reverse_forloop(array: list) -> list:
    to_return: list = []

    for i in array:
        to_return.insert(0, i)

    return to_return


time1 = time.time()

for i in range(998):
    reverse_recursion([0] * i)

time2 = time.time()

for i in range(998):
    reverse_forloop([0] * i)

time3 = time.time()

print(f"Recursif: {time2-time1} s")
print(f"For-loop: {time3-time2} s")

print( reverse_recursion([0,1,2,3,4,5]) )
print( reverse_forloop([0,1,2,3,4,5]) )
