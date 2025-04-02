x = [[1, 2],
     [4, 5],
     [7, 8]]
y = [[0, 0, 0],
     [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        y[j][i] = x[i][j]

print("Transpose of matrix:")
for res in y:
    print(res)
