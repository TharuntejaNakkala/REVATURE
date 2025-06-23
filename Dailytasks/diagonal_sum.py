"""Write a function that returns the sum of both the primary and secondary diagonals of a square matrix. If an element is in both diagonals (center of matrix), count it only once"""
def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]  
        if i != n - 1 - i:     
            total += matrix[i][n - 1 - i]
    return total

#Input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

output = diagonal_sum(matrix)
print("Diagonal Sum:", output)
