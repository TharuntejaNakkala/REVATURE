"""Print all prime numbers up to n in matrix number of columns."""
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter max number: "))
matrix = int(input("Enter matrix column size: "))

l1 = list(range(1, n))
res = []

for i in l1:
    if isprime(i):
        res.append(i)

for i in range(0, len(res), matrix):
    for j in range(matrix):
        if i + j < len(res):
            print(res[i + j], end=" ")
    print()
