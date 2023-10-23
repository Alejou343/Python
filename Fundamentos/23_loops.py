matriz = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

print(matriz[0][0])                     # 1
print(matriz[1][1])                     # 5
print(matriz[2][2])                     # 9

# Ciclos anidados

for row in matriz:
    print(row)
    for column in row:
        print(column)                   # [1,2,3] 1, 2, 3 - [4,5,6] 4, 5, 6 - [7,8,9] 7, 8, 9