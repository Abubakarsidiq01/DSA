matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Printing the matrix")
for row in matrix:
    print(row)

print("Printing the matrix in a single line")
for row in matrix:
    for val in row:
        print(val)

print("Printing the matrix in a single line")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

print("Printing the total of the matrix")
total = 0
for row in matrix:
    for val in row:
        total += val
print(total)

print("Printing the transposed matrix")
rows = len(matrix)
cols = len(matrix[0])
transposed = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transposed.append(new_row)
    print(new_row)
print(transposed)

print("Printing the diagonal of the matrix")
for i in range(len(matrix)):
    print(matrix[i][i])

print("Printing the diagonal of the matrix")
n = len(matrix)
for i in range(n):
    print(matrix[i][n - 1 - i])