# Sample matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Processed result matrix
result = []

for row in matrix:
    new_row = []
    for element in row:
        if element % 2 == 0:  # even
            new_row.append(element * 10)
        else:  # odd
            new_row.append(element * 7)
    result.append(new_row)

# Print output in matrix form
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nProcessed Matrix:")
for row in result:
    print(row)
