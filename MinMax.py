li=[[1,2,3,5,8,8],[8,3,2,3]]
min=li[0][0]
max=li[0][0]

for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j] < min:
            min = li[i][j]

        if li[i][j] > max:
            max = li[i][j]

print(min)
print(max)
