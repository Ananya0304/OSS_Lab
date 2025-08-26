import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix row by row (space-separated values):")
matrix = []
for i in range(rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix.append(row)

mat = np.array(matrix)

rank = np.linalg.matrix_rank(mat)
trace = np.trace(mat) if rows == cols else "Trace undefined for non-square matrix"
determinant = np.linalg.det(mat) if rows == cols else "Determinant undefined for non-square matrix"

print("\nMatrix:")
print(mat)
print(f"\nRank: {rank}")
print(f"Trace: {trace}")
print(f"Determinant: {determinant}")
