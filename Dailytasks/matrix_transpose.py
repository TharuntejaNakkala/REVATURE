"""Print the transpose of a 1D sequence arranged as a matrix."""

n = int(input("Enter seq numbers: "))
l = list(range(1, n + 1))
res = []
matrixsize = int(input("Enter matrix dimension: "))

for i in range(matrixsize):
    for j in range(i, len(l), matrixsize):
        res.append(l[j])

for i in range(0, len(res), matrixsize):
    for j in range(matrixsize):
        print(res[i + j], end=' ')
    print()
# This code takes a sequence of numbers and prints it in a transposed matrix format based on the specified matrix dimension. The input sequence is generated from 1 to n, and the output is arranged in rows of the specified size. Each row contains elements spaced according to the matrix dimension, effectively transposing the original sequence into a matrix format.
